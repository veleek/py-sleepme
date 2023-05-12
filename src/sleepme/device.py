from .config import SleepmeConfig
from .services import aiosleepme
from .models import DeviceInfo
from .models import DeviceState
from .models.DeviceState import DeviceControl
from .models.DeviceState import TemperatureUnit


class SleepmeDevice:
    """
    A strongly typed class to represent a Sleepme device.
    """

    def __init__(self, info: DeviceInfo, state: DeviceState, config: SleepmeConfig):
        self._config = config
        self.info = info
        self.state = state

    async def refresh_state(self):
        self.state = await aiosleepme.get_device_state(self.info.id, self._config)

    async def update_state(self, update: DeviceControl):
        await aiosleepme.update_device(self.info.id, update, self._config)

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
        await self.update_state(update)

    async def set_brightness(self, brightness: int):
        update = DeviceControl()
        update.brightness_level = brightness
        await self.update_state(update)
