from datetime import date
from enum import Enum

from pydantic import BaseModel

from clio_client.openapi_client.models.contact_update_request_data_custom_field_values_inner_custom_field import (
    ContactUpdateRequestDataCustomFieldValuesInnerCustomField,
)
from clio_client.openapi_client.models.matter_update_request import MatterUpdateRequest
from clio_client.openapi_client.models.matter_update_request_data import (
    MatterUpdateRequestData,
)
from clio_client.openapi_client.models.matter_update_request_data_custom_field_values_inner import (
    MatterUpdateRequestDataCustomFieldValuesInner,
)
from clio_client.openapi_client.models.matter_update_request_data_relationships_inner_contact import (
    MatterUpdateRequestDataRelationshipsInnerContact as MatterUpdateRequestDataResponsibleStaff,
)
from clio_client.openapi_client.models.matter_update_request_data_statute_of_limitations import (
    MatterUpdateRequestDataStatuteOfLimitations,
)


class MatterStatusEnum(str, Enum):
    open = "open"
    closed = "closed"
    pending = "pending"


class ResponsibleStaffModel(BaseModel):
    id: int


class PracticeAreaModel(BaseModel):
    id: int


class StatuteOfLimitationsModel(BaseModel):
    due_at: date


class CustomFieldValueModel(BaseModel):
    id: int | str
    value: str | int | float | bool
    custom_field: ContactUpdateRequestDataCustomFieldValuesInnerCustomField | None = None


class GroupModel(BaseModel):
    id: int


class MatterUpdateInputModel(BaseModel):
    description: str | None = None
    status: MatterStatusEnum | None = None  # <--- use enum here
    close_date: date | None = None
    open_date: date | None = None
    responsible_staff: ResponsibleStaffModel | None = None
    statute_of_limitations: StatuteOfLimitationsModel | None = None
    practice_area: PracticeAreaModel | None = None
    custom_field_values: list[CustomFieldValueModel] | None = None
    group: GroupModel | None = None


def build_full_update_request(input: MatterUpdateInputModel) -> MatterUpdateRequest:
    data_kwargs = {
        "description": input.description,
        "status": input.status,
        "close_date": input.close_date,
        "open_date": input.open_date,
    }

    if input.responsible_staff:
        data_kwargs["responsible_staff"] = MatterUpdateRequestDataResponsibleStaff(id=input.responsible_staff.id)

    if input.practice_area:
        data_kwargs["practice_area"] = {"id": input.practice_area.id}  # Pass as dict

    if input.group:
        data_kwargs["group"] = {"id": input.group.id}  # Pass as dict

    if input.statute_of_limitations:
        data_kwargs["statute_of_limitations"] = MatterUpdateRequestDataStatuteOfLimitations(
            due_at=input.statute_of_limitations.due_at
        )

    if input.custom_field_values:
        cf_values = []
        for cf in input.custom_field_values:
            kwargs = {"id": cf.id, "value": cf.value}
            if cf.custom_field:
                kwargs["custom_field"] = cf.custom_field
            cf_values.append(MatterUpdateRequestDataCustomFieldValuesInner(**kwargs))
        data_kwargs["custom_field_values"] = cf_values

    return MatterUpdateRequest(data=MatterUpdateRequestData(**data_kwargs))
