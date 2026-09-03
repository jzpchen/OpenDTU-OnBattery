// SPDX-License-Identifier: GPL-2.0-or-later
#include <battery/litime/Provider.h>
#include <PinMapping.h>
#include <SerialPortManager.h>
#include <Configuration.h>
#include <LogHelper.h>
#include <cmath>
#include <cstdlib>
#include <cstring>

#undef TAG
static const char* TAG = "battery";
static const char* SUBTAG = "LiTime";

namespace Batteries::LiTime {

Provider::Provider()
    : _stats(std::make_shared<Stats>())
    , _hassIntegration(std::make_shared<HassIntegration>(_stats))
{
}

Provider::Interface Provider::getInterface() const
{
    auto const& config = Configuration.get();
    switch (config.Battery.Serial.Interface) {
        case 0: return Interface::Uart;
        case 1: return Interface::Transceiver;
        default: return Interface::Invalid;
    }
}

bool Provider::init()
{
    DTU_LOGI("Initializing LiTime RS-485 Provider (ComFlex / Golf Cart)...");

    const PinMapping_t& pin = PinMapping.get();
    if (pin.battery_rx <= GPIO_NUM_NC || pin.battery_tx <= GPIO_NUM_NC) {
        DTU_LOGE("Invalid RX/TX pin config");
        return false;
    }

    auto oHwSerialPort = SerialPortManager.allocatePort(_serialPortOwner);
    if (!oHwSerialPort) {
        DTU_LOGE("Failed to allocate HW UART port for LiTime");
        return false;
    }

    _upSerial = std::make_unique<HardwareSerial>(*oHwSerialPort);

    pinMode(pin.battery_rx, INPUT_PULLUP);
    _upSerial->end();
    _upSerial->begin(19200, SERIAL_8N1, pin.battery_rx, pin.battery_tx);
    _upSerial->flush();

    if (Interface::Transceiver == getInterface()) {
        _rxEnablePin = pin.battery_rxen;
        _txEnablePin = pin.battery_txen;
        if (_rxEnablePin >= 0) {
            pinMode(_rxEnablePin, OUTPUT);
            digitalWrite(_rxEnablePin, LOW);
        }
        if (_txEnablePin >= 0) {
            pinMode(_txEnablePin, OUTPUT);
            digitalWrite(_txEnablePin, LOW);
        }
    }

    _rxLen = 0;
    _lastRequest = 0;
    _infoQueried = false;
    _snQueried = false;
    DTU_LOGI("LiTime RS-485 Provider initialized @ 19200 baud (TX=%d, RX=%d)", pin.battery_tx, pin.battery_rx);
    return true;
}

void Provider::deinit()
{
    if (_upSerial) {
        _upSerial->end();
        _upSerial = nullptr;
    }
    SerialPortManager.freePort(_serialPortOwner);
}

void Provider::sendRequest(uint8_t pollInterval)
{
    if ((millis() - _lastRequest) < (pollInterval * 1000)) {
        return;
    }

    if (Interface::Transceiver == getInterface()) {
        digitalWrite(_rxEnablePin, HIGH);
        digitalWrite(_txEnablePin, HIGH);
    }

    // Command Frames:
    // CMD 0x13: Read 16 Cells, Pack V, Current, SoC, SoH, Temp, Ah (8 Bytes: 00 00 04 01 13 55 AA 17)
    // CMD 0x10: Read Serial Number (8 Bytes: 00 00 04 01 10 55 AA 14)
    // CMD 0x06: Read Hardware Model (8 Bytes: 00 00 04 01 06 55 AA 0A)
    static const uint8_t CMD_READ_CELLS[8] = { 0x00, 0x00, 0x04, 0x01, 0x13, 0x55, 0xAA, 0x17 };
    static const uint8_t CMD_READ_SN[8]    = { 0x00, 0x00, 0x04, 0x01, 0x10, 0x55, 0xAA, 0x14 };
    static const uint8_t CMD_READ_INFO[8]  = { 0x00, 0x00, 0x04, 0x01, 0x06, 0x55, 0xAA, 0x0A };

    // Query hardware model & serial number once at startup, then keep polling live telemetry
    if (!_infoQueried) {
        _upSerial->write(CMD_READ_INFO, sizeof(CMD_READ_INFO));
        _infoQueried = true;
    } else if (!_snQueried) {
        _upSerial->write(CMD_READ_SN, sizeof(CMD_READ_SN));
        _snQueried = true;
    } else {
        _upSerial->write(CMD_READ_CELLS, sizeof(CMD_READ_CELLS));
    }
    _upSerial->flush();

    if (Interface::Transceiver == getInterface()) {
        digitalWrite(_rxEnablePin, LOW);
        digitalWrite(_txEnablePin, LOW);
    }

    _lastRequest = millis();
}

void Provider::loop()
{
    auto const& config = Configuration.get();
    uint8_t pollInterval = config.Battery.Serial.PollingInterval;
    if (pollInterval == 0) { pollInterval = 1; }

    while (_upSerial->available()) {
        uint8_t b = _upSerial->read();
        if (_rxLen < sizeof(_rxBuf) - 1) {
            _rxBuf[_rxLen++] = b;
        }
        _lastRxByteTime = millis();
    }

    // Process frame when complete (after 30ms of silence or full buffer)
    if (_rxLen > 0 && (millis() - _lastRxByteTime >= 30)) {
        _rxBuf[_rxLen] = '\0';

        // 1. Check for 16-Cell & Telemetry Response: contains [0x93, 0x55, 0xAA]
        for (size_t i = 0; i + 3 <= _rxLen; i++) {
            if (_rxBuf[i] == 0x93 && _rxBuf[i + 1] == 0x55 && _rxBuf[i + 2] == 0xAA) {
                const uint8_t* p = &_rxBuf[i + 3];
                size_t payloadLen = _rxLen - (i + 3);

                if (payloadLen >= 86) {
                    // Total Pack Voltage (Bytes 5-8, uint32 LE in millivolts)
                    uint32_t packVoltageMv = p[5] | (static_cast<uint32_t>(p[6]) << 8) |
                                            (static_cast<uint32_t>(p[7]) << 16) |
                                            (static_cast<uint32_t>(p[8]) << 24);

                    // 16 Cells (Bytes 9-40, 16 x uint16 LE in millivolts)
                    std::map<uint8_t, uint16_t> cells;
                    uint16_t minMv = 65535;
                    uint16_t maxMv = 0;
                    for (uint8_t c = 0; c < 16; c++) {
                        uint16_t mv = p[9 + (c * 2)] | (static_cast<uint16_t>(p[10 + (c * 2)]) << 8);
                        cells.emplace(c + 1, mv);
                        if (mv < minMv) minMv = mv;
                        if (mv > maxMv) maxMv = mv;
                    }

                    // Pack Current (Bytes 41-42, signed int16 LE in milliamps: + for charge, - for discharge)
                    int16_t current16 = static_cast<int16_t>(p[41] | (static_cast<uint16_t>(p[42]) << 8));
                    int32_t currentMa = static_cast<int32_t>(current16);

                    // Temperature (Bytes 45-46: NTC Temp Sensor 1, uint16 LE in integer °C)
                    uint16_t rawTemp = p[45] | (static_cast<uint16_t>(p[46]) << 8);
                    int16_t tempC = static_cast<int16_t>(rawTemp);

                    // Rated Capacity (Bytes 57-58, uint16 LE in 0.01 Ah: 3000 = 30.00 Ah)
                    uint16_t rawRated = p[57] | (static_cast<uint16_t>(p[58]) << 8);
                    float totalAh = 30.0f;
                    if (rawRated > 500) {
                        totalAh = rawRated / 100.0f;
                    } else if (rawRated > 0) {
                        totalAh = static_cast<float>(rawRated);
                    }

                    // State of Charge (SoC) (Bytes 83-84, uint16 LE: e.g. 25 = 25%, 41 = 41%)
                    uint16_t rawSoc = p[83] | (static_cast<uint16_t>(p[84]) << 8);
                    uint8_t socPercent = (rawSoc <= 100) ? static_cast<uint8_t>(rawSoc) : 100;

                    // Remaining Capacity (Bytes 55-56, uint16 LE in 0.01 Ah: e.g. 1234 = 12.34 Ah, 750 = 7.50 Ah)
                    uint16_t rawRem = p[55] | (static_cast<uint16_t>(p[56]) << 8);
                    float remAh = 0.0f;
                    if (rawRem > 0 && rawRem <= (rawRated + 200)) {
                        remAh = rawRem / 100.0f;
                    } else {
                        remAh = totalAh * (socPercent / 100.0f);
                    }

                    DTU_LOGI("🔋 [LiTime] Live: %.3f V | %+.3f A (%+.1f W) | %u%% SoC | %.1f Ah/%.1f Ah | %d °C | 16 Cells (Delta: %u mV)",
                        packVoltageMv / 1000.0f,
                        currentMa / 1000.0f,
                        (packVoltageMv / 1000.0f) * (currentMa / 1000.0f),
                        socPercent,
                        remAh, totalAh,
                        tempC,
                        (maxMv > minMv) ? (maxMv - minMv) : 0);

                    _stats->updateTelemetry(packVoltageMv, socPercent, currentMa, remAh, totalAh, tempC, cells);
                    _stats->setStatus(0x80);
                    _stats->setUnitId(1);
                    break;
                }
            }
        }

        _rxLen = 0;
    }

    sendRequest(pollInterval);
}

} // namespace Batteries::LiTime



