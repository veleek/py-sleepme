from typing import List

from sleepme.services import aiosleepme, sleepme
from sleepme.SleepmeDevice import SleepmeDevice


class SleepmeDeviceManager:
    devices: List[SleepmeDevice]

    @staticmethod
    def get_devices() -> List[SleepmeDevice]:
        if SleepmeDeviceManager.devices is None:
            deviceInfos = sleepme.get_devices()
            SleepmeDeviceManager.devices = [
                SleepmeDevice(device, sleepme.get_device_state(device.id)) for device in deviceInfos
            ]
        return SleepmeDeviceManager.devices

    @staticmethod
    def get_device(id: str) -> SleepmeDevice:
        devices = SleepmeDeviceManager.get_devices()
        device: SleepmeDevice | None = next(
            (device for device in devices if device.device.id == id), None
        )

        if device is None:
            raise Exception(f"Device with id {id} not found")

        return device

    @staticmethod
    async def get_devices_async() -> List[SleepmeDevice]:
        if SleepmeDeviceManager.devices is None:
            deviceInfos = await aiosleepme.get_devices()
            SleepmeDeviceManager.devices = [
                SleepmeDevice(device, await aiosleepme.get_device_state(device.id))
                for device in deviceInfos
            ]
        return SleepmeDeviceManager.devices

    @staticmethod
    async def get_device_async(id: str) -> SleepmeDevice:
        devices = await SleepmeDeviceManager.get_devices_async()
        device: SleepmeDevice | None = next(
            (device for device in devices if device.device.id == id), None
        )

        if device is None:
            raise Exception(f"Device with id {id} not found")

        return device
