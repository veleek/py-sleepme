from typing import List

from pydantic import BaseModel


class DeviceInfo(BaseModel):
    """
    Basic SleepMe device info returned by the get devices API.

    """

    id: str
    name: str
    attachments: List[str]
