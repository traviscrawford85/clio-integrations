
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


def build_update_request(
    description: str | None = None,
    status: str | None = None,
    *,
    value: str,
    custom_field_id: int | None = None,
    custom_field_value_id: int | None = None,
) -> MatterUpdateRequest:
    """
    Build a MatterUpdateRequest with custom field update.
    Provide either:
      - custom_field_id (for assigning a new value)
      - custom_field_value_id (for updating an existing one)
    """

    if custom_field_id is None and custom_field_value_id is None:
        raise ValueError("You must provide either a custom_field_id or custom_field_value_id.")

    if custom_field_id is not None:
        custom_field_obj = ContactUpdateRequestDataCustomFieldValuesInnerCustomField(id=custom_field_id)
        cf = MatterUpdateRequestDataCustomFieldValuesInner(
            custom_field=custom_field_obj,
            value=value
        )
    else:
        cf = MatterUpdateRequestDataCustomFieldValuesInner(
            id=custom_field_value_id,
            value=value
        )

    data = MatterUpdateRequestData(
        description=description,
        status=status,
        custom_field_values=[cf]
    )

    return MatterUpdateRequest(data=data)
