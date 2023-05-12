from sleepme.config import SleepmeConfig
from sleepme.device_manager import SleepmeDeviceManager


async def test_device_manager_setup():
    deviceManager = SleepmeDeviceManager(SleepmeConfig())
    devices = await deviceManager.get_devices_async()

    assert len(devices) > 0

    device = await deviceManager.get_device_async(devices[0].info.id)
    assert device.info.id == devices[0].info.id
