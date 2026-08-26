#pragma once

#include <memory>
#include <map>
#include <battery/Stats.h>

namespace Batteries::LiTime {

class Stats : public ::Batteries::Stats {
public:
    Stats();

    void setStatus(uint8_t status);
    void setUnitId(uint8_t unitId);
    void updateTelemetry(uint32_t packVoltageMv, uint8_t socPercent, int32_t currentMa,
                         float remainAh, float totalAh, int16_t tempC,
                         std::map<uint8_t, uint16_t> const& cellVoltages);

    void getLiveViewData(JsonVariant& root) const override;
    void mqttPublish() const override;

protected:
    uint32_t getMaxAgeSeconds() const override { return 30; }

private:
    uint8_t _unitId = 1;
    uint8_t _status = 0x80;
    float _remainAh = 7.5f;
    float _totalAh = 30.0f;
    std::map<uint8_t, uint16_t> _cellVoltages;
};

} // namespace Batteries::LiTime
