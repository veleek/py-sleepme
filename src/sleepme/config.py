import os
from typing import Union

from pydantic import BaseModel


class SleepmeConfig(BaseModel):
    base_path: str = "https://api.developer.sleep.me/v1"
    verify: Union[bool, str] = False
    proxies: str | None = None
    access_token: str = ""

    def __init__(self, access_token: str = None):
        super().__init__()
        self.access_token = access_token if access_token is not None else os.environ["access_token"]


class HTTPException(Exception):
    def __init__(self, status_code: int, message: str):
        self.status_code = status_code
        self.message = message
        super().__init__(f"{status_code} {message}")

    def __str__(self):
        return f"{self.status_code} {self.message}"
