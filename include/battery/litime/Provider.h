#pragma once

#include <memory>
#include <HardwareSerial.h>
#include <battery/Provider.h>
#include <battery/litime/Stats.h>
#include <battery/litime/HassIntegration.h>

namespace Batteries::LiTime {

class Provider : public ::Batteries::Provider {
public:
    Provider();

    bool init() final;
    void deinit() final;
    void loop() final;
    std::shared_ptr<::Batteries::Stats> getStats() const final { return _stats; }
    std::shared_ptr<::Batteries::HassIntegration> getHassIntegration() final { return _hassIntegration; }

private:
    static char constexpr _serialPortOwner[] = "LiTime BMS";

    std::unique_ptr<HardwareSerial> _upSerial;
    std::shared_ptr<Stats> _stats;
    std::shared_ptr<HassIntegration> _hassIntegration;

    enum class Interface : unsigned {
        Invalid,
        Uart,
        Transceiver
    };

    Interface getInterface() const;
    void sendRequest(uint8_t pollInterval);

    int8_t _rxEnablePin = -1;
    int8_t _txEnablePin = -1;
    uint32_t _lastRequest = 0;

    uint8_t _rxBuf[128];
    size_t _rxLen = 0;
    uint32_t _lastRxByteTime = 0;
};

} // namespace Batteries::LiTime
