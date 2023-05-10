from sleepme.services import aiosleepme

from .models import DeviceInfo
from .models import DeviceState
from .models.DeviceState import DeviceControl
from .models.DeviceState import TemperatureUnit


class SleepmeDevice:
    """
    A strongly typed class to represent a Sleepme device.
    """

    def __init__(self, device: DeviceInfo, state: DeviceState):
        self.device = device
        self.state = state

    async def refresh_state(self):
        self.state = await aiosleepme.get_device_state(self.device.id)

    def get_temperature(self) -> float:
        if self.state.control.display_temperature_unit == TemperatureUnit.Celsius:
            return self.state.control.set_temperature_c or 0.0
        else:
            return self.state.control.set_temperature_f or 0

    async def set_temperature(self, temperature: float):
        update = DeviceControl()
        if self.state.control.display_temperature_unit == TemperatureUnit.Celsius:
            update.set_temperature_c = temperature
        else:
            update.set_temperature_f = int(temperature)

        await aiosleepme.update_device(self.device.id, update)

    async def set_brightness(self, brightness: int):
        update = DeviceControl()
        update.brightness_level = brightness
        await aiosleepme.update_device(self.device.id, update)
