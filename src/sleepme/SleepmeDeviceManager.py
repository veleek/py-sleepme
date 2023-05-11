from typing import List
from sleepme.api_config import APIConfig

from sleepme.services import aiosleepme
from sleepme.services import sleepme
from sleepme.SleepmeDevice import SleepmeDevice


class SleepmeDeviceManager:
    devices: List[SleepmeDevice]

    def __init__(self, config: APIConfig):
        self._config = config
        self.devices: List[SleepmeDevice] = None

    def get_devices(self) -> List[SleepmeDevice]:
        if SleepmeDeviceManager.devices is None:
            deviceInfos = sleepme.get_devices(self._config)
            SleepmeDeviceManager.devices = [
                SleepmeDevice(device, sleepme.get_device_state(device.id, self._config)) for device in deviceInfos
            ]
        return SleepmeDeviceManager.devices

    def get_device(self, id: str) -> SleepmeDevice:
        devices = self.get_devices()
        device: SleepmeDevice | None = next((device for device in devices if device.info.id == id), None)

        if device is None:
            raise Exception(f"Device with id {id} not found")

        return device

    async def get_devices_async(self) -> List[SleepmeDevice]:
        if SleepmeDeviceManager.devices is None:
            deviceInfos = await aiosleepme.get_devices(self._config)
            SleepmeDeviceManager.devices = [
                SleepmeDevice(device, await aiosleepme.get_device_state(device.id, self._config)) for device in deviceInfos
            ]
        return SleepmeDeviceManager.devices

    async def get_device_async(self, id: str) -> SleepmeDevice:
        devices = await self.get_devices_async()
        device: SleepmeDevice | None = next((device for device in devices if device.info.id == id), None)

        if device is None:
            raise Exception(f"Device with id {id} not found")

        return device
