// SPDX-License-Identifier: GPL-2.0-or-later
#include <battery/litime/HassIntegration.h>

namespace Batteries::LiTime {

HassIntegration::HassIntegration(std::shared_ptr<Stats> spStats)
    : ::Batteries::HassIntegration(spStats)
    , _spStats(spStats)
{
}

void HassIntegration::publishSensors() const
{
    ::Batteries::HassIntegration::publishSensors();
}

} // namespace Batteries::LiTime
