from typing import Optional

from pydantic import BaseModel, Field


class UpdateRequest(BaseModel):
    """
    Update Request model

    """

    thermal_control_status: Optional[str] = Field(
        alias="thermal_control_status", default=None
    )

    set_temperature_f: Optional[float] = Field(alias="set_temperature_f", default=None)

    set_temperature_c: Optional[float] = Field(alias="set_temperature_c", default=None)

    display_temperature_unit: Optional[str] = Field(
        alias="display_temperature_unit", default=None
    )

    time_zone: Optional[str] = Field(alias="time_zone", default=None)
