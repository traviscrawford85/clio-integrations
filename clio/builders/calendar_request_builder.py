# Input model for creating/updating calendar events
from datetime import date, datetime
from typing import Optional, Union

from pydantic import BaseModel

from clio_client.openapi_client.models.calendar_create_request import (
    CalendarCreateRequest,
)
from clio_client.openapi_client.models.calendar_create_request_data import (
    CalendarCreateRequestData,
)

from clio_client.openapi_client.models.calendar_entry_create_request_data_matter
from clio.api.models.sdk_model_aliases import CalendarBaseRefModel


class CalendarEventInputModel(BaseModel):
    subject: Optional[str] = None
    location: Optional[str] = None
    start_time: Optional[datetime] = None
    end_time: Optional[datetime] = None
    description: Optional[str] = None
    calendar_id: Optional[int] = None
    matter_id: Optional[int] = None


