from enum import Enum
from typing import Optional

from pydantic import BaseModel
from pydantic import Field


class DeviceAbout(BaseModel):
    """
    DeviceAbout model
    """

    firmware_version: Optional[str] = Field(alias="firmware_version", default=None)
    ip_address: Optional[str] = Field(alias="ip_address", default=None)
    lan_address: Optional[str] = Field(alias="lan_address", default=None)
    mac_address: Optional[str] = Field(alias="mac_address", default=None)
    model: Optional[str] = Field(alias="model", default=None)
    serial_number: Optional[str] = Field(alias="serial_number", default=None)


class TemperatureUnit(Enum):
    Celsius = "c"
    Fahrenheit = "f"


class ThermalControlStatus(Enum):
    Unknown = "unknown"
    Active = "active"
    Standby = "standby"


class DeviceControl(BaseModel):
    """
    DeviceControl model
    """

    brightness_level: Optional[int] = Field(alias="brightness_level", default=None)
    display_temperature_unit: Optional[TemperatureUnit] = Field(alias="display_temperature_unit", default=None)
    set_temperature_c: Optional[float] = Field(alias="set_temperature_c", default=None)
    set_temperature_f: Optional[int] = Field(alias="set_temperature_f", default=None)
    thermal_control_status: Optional[ThermalControlStatus] = Field(alias="thermal_control_status", default=None)
    time_zone: Optional[str] = Field(alias="time_zone", default=None)


class DeviceStatus(BaseModel):
    """
    DeviceStatus model
    """

    is_connected: Optional[bool] = Field(alias="is_connected", default=None)
    is_water_low: Optional[bool] = Field(alias="is_water_low", default=None)
    water_level: Optional[int] = Field(alias="water_level", default=None)
    water_temperature_c: Optional[float] = Field(alias="water_temperature_c", default=None)
    water_temperature_f: Optional[float] = Field(alias="water_temperature_f", default=None)


class DeviceState(BaseModel):
    """
    Status model

    """

    about: DeviceAbout = Field(alias="about", default=None)

    control: DeviceControl = Field(alias="control", default=None)

    status: DeviceStatus = Field(alias="status", default=None)
