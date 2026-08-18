// SPDX-License-Identifier: GPL-2.0-or-later
#include <battery/litime/Stats.h>
#include <MqttSettings.h>
#include <Configuration.h>
#include <LogHelper.h>

namespace Batteries::LiTime {

Stats::Stats()
{
    setManufacturer("LiTime");
}

void Stats::setStatus(uint8_t status)
{
    _status = status;
}

void Stats::setUnitId(uint8_t unitId)
{
    _unitId = unitId;
}

void Stats::updateTelemetry(uint32_t packVoltageMv, uint8_t socPercent, int32_t currentMa,
                             uint32_t remainAh, uint32_t totalAh, int16_t tempC,
                             std::map<uint8_t, uint16_t> const& cellVoltages)
{
    uint32_t now = millis();
    setVoltage(packVoltageMv / 1000.0f, now);
    setSoC(socPercent, 0, now);
    setCurrent(currentMa / 1000.0f, 2, now);
    setTemperature(tempC, now);
    _remainAh = remainAh;
    _totalAh = totalAh;
    _cellVoltages = cellVoltages;
}

void Stats::getLiveViewData(JsonVariant& root) const
{
    ::Batteries::Stats::getLiveViewData(root);

    float voltage = getVoltage();
    float current = getChargeCurrent();
    addLiveViewValue(root, "power", current * voltage, "W", 2);
    addLiveViewValue(root, "capacityRemaining", static_cast<float>(_remainAh), "Ah", 1);
    addLiveViewValue(root, "capacityTotal", static_cast<float>(_totalAh), "Ah", 1);

    addLiveViewTextValue(root, "chargeEnabled", (_status & 0x80) ? "yes" : "no");
    addLiveViewTextValue(root, "dischargeEnabled", (_status & 0x80) ? "yes" : "no");

    if (!_cellVoltages.empty()) {
        uint16_t minMv = 65535;
        uint16_t maxMv = 0;
        uint32_t sumMv = 0;

        for (auto const& [cellNum, mv] : _cellVoltages) {
            char cellKey[20];
            snprintf(cellKey, sizeof(cellKey), "cell%02dVoltage", cellNum);
            addLiveViewInSection(root, "cells", cellKey, static_cast<float>(mv) / 1000.0f, "V", 3);

            if (mv < minMv) minMv = mv;
            if (mv > maxMv) maxMv = mv;
            sumMv += mv;
        }

        float avgV = (sumMv / static_cast<float>(_cellVoltages.size())) / 1000.0f;
        addLiveViewInSection(root, "cells", "cellMinVoltage", static_cast<float>(minMv) / 1000.0f, "V", 3);
        addLiveViewInSection(root, "cells", "cellAvgVoltage", avgV, "V", 3);
        addLiveViewInSection(root, "cells", "cellMaxVoltage", static_cast<float>(maxMv) / 1000.0f, "V", 3);
        addLiveViewInSection(root, "cells", "cellDiffVoltage", maxMv - minMv, "mV", 0);
    }
}

void Stats::mqttPublish() const
{
    ::Batteries::Stats::mqttPublish();
    MqttSettings.publish("battery/capacityRemaining", String(_remainAh));
    MqttSettings.publish("battery/capacityTotal", String(_totalAh));
    MqttSettings.publish("battery/statusFlag", String(_status));
}

} // namespace Batteries::LiTime
