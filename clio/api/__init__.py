from datetime import date
from typing import Optional

from pydantic import BaseModel


class UpdatePayloadModel(BaseModel):
    description: str | None = None
    status: str | None = None
    value: str
    custom_field_id: int | None = None
    custom_field_value_id: int | None = None
    responsible_staff: int | None = None
    close_date: date | None = None
    practice_area: str | None = None
    statute_of_limitations: date | None = None
    
