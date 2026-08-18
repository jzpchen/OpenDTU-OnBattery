#pragma once

#include <battery/HassIntegration.h>
#include <battery/litime/Stats.h>

namespace Batteries::LiTime {

class HassIntegration : public ::Batteries::HassIntegration {
public:
    explicit HassIntegration(std::shared_ptr<Stats> spStats);
    ~HassIntegration() = default;

protected:
    void publishSensors() const override;

private:
    std::shared_ptr<Stats> _spStats;
};

} // namespace Batteries::LiTime
