from typing import Optional

import httpx

from ..config import SleepmeConfig
from ..config import HTTPException
from ..models import DeviceControl
from ..models import DeviceInfoList
from ..models import DeviceState
from ..models import UpdateResponse


async def get_devices(api_config_override: Optional[SleepmeConfig] = None) -> DeviceInfoList:
    async with get_client(api_config_override) as client:
        response = await client.request("get", httpx.URL("/devices"))

    if response.status_code != 200:
        raise HTTPException(response.status_code, f" failed with status code: {response.status_code}")

    return DeviceInfoList.parse_obj(response.json()) if response.json() is not None else DeviceInfoList(__root__=[])


async def get_device_state(device_id: str, api_config_override: Optional[SleepmeConfig] = None) -> DeviceState:
    async with get_client(api_config_override) as client:
        response = await client.request("get", httpx.URL(f"/devices/{device_id}"))

    if response.status_code != 200:
        raise HTTPException(response.status_code, f" failed with status code: {response.status_code}")

    return DeviceState(**response.json()) if response.json() is not None else DeviceState()


async def update_device(
    device_id: str, body: DeviceControl, api_config_override: Optional[SleepmeConfig] = None
) -> UpdateResponse:
    body_dict = body.dict(exclude_unset=True, exclude_none=True)

    async with get_client(api_config_override) as client:
        response = await client.request("patch", httpx.URL(f"/devices/{device_id}"), json=body_dict)

    if response.status_code != 200:
        raise HTTPException(
            response.status_code,
            f" failed with status code: {response.status_code}. {response.json()}",
        )

    return UpdateResponse(**response.json()) if response.json() is not None else UpdateResponse()


def get_client(api_config_override: Optional[SleepmeConfig] = None) -> httpx.AsyncClient:
    api_config = api_config_override if api_config_override else SleepmeConfig()

    return httpx.AsyncClient(
        base_url=api_config.base_path,
        proxies=api_config.proxies,
        verify=api_config.verify,
        headers={
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Authorization": f"Bearer { api_config.access_token }",
        },
    )
