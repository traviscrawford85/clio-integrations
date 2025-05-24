
from datetime import datetime

from pydantic import BaseModel


class CalendarEventUpdateInputModel(BaseModel):
    subject: str | None = None
    location: str | None = None
    start_time: datetime | None = None
    end_time: datetime | None = None
    description: str | None = None
