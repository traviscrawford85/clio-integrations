# builders/matter_view_model.py
from datetime import date

from pydantic import BaseModel


class CustomFieldModel(BaseModel):
    id: int | str
    value: str | int | float | bool
    field_name: str | None = None  # extracted from nested "custom_field.name"


class MatterViewModel(BaseModel):
    id: int
    display_name: str | None
    display_number: str | None
    custom_field_values: list[CustomFieldModel] | None
    created_at: date | None
    updated_at: date | None

def parse_matter_sdk_response(sdk_data: dict) -> MatterViewModel:
    cf_values = []
    for cf in sdk_data.get("custom_field_values", []):
        cf_values.append(CustomFieldModel(
            id=cf.get("id"),
            value=cf.get("value"),
            field_name=cf.get("custom_field", {}).get("name")
        ))

    return MatterViewModel(
        id=sdk_data["id"],
        display_name=sdk_data.get("display_name"),
        display_number=sdk_data.get("display_number"),
        custom_field_values=cf_values,
        created_at=sdk_data.get("created_at"),
        updated_at=sdk_data.get("updated_at")
    )