from typing import List

from pydantic import BaseModel


class DeviceInfo(BaseModel):
    """
    Basic SleepMe device info returned by the get devices API.

    """

    id: str
    name: str
    attachments: List[str]


class DeviceInfoList(BaseModel):
    """
    DeviceList model

    """

    __root__: List[DeviceInfo]

    def __iter__(self):
        return iter(self.__root__)

    def __getitem__(self, item):
        return self.__root__[item]

    def __len__(self):
        return len(self.__root__)
