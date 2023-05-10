from pprint import pprint

from sleepme.models.DeviceState import DeviceControl
from sleepme.models.DeviceState import TemperatureUnit
from sleepme.models.DeviceState import ThermalControlStatus
from sleepme.services.aiosleepme import get_device_state
from sleepme.services.aiosleepme import get_devices
from sleepme.services.aiosleepme import update_device


async def test_get_devices():
    devices = await get_devices()

    assert len(devices) > 0
    device = devices[0]
    assert device.id is not None
    assert device.name is not None
    assert device.attachments is not None
    assert len(device.attachments) > 0
    assert device.attachments[0] is not None
    pprint(device)


async def test_get_device():
    devices = await get_devices()
    device = await get_device_state(devices[0].id)

    pprint(device)
    assert device.control.display_temperature_unit == TemperatureUnit.Fahrenheit
    assert (
        device.control.thermal_control_status == ThermalControlStatus.Standby
        or device.control.thermal_control_status == ThermalControlStatus.Active
    )


async def test_update_device():
    devices = await get_devices()
    id = devices[0].id
    device = await get_device_state(id)

    device.control.display_temperature_unit = TemperatureUnit.Celsius
    device.control.thermal_control_status = ThermalControlStatus.Active

    update = DeviceControl(
        set_temperature_f=82,
    )

    pprint(update.dict(exclude_unset=True))
    pprint(update.dict(exclude_unset=True, by_alias=True))

    await update_device(id, update)
