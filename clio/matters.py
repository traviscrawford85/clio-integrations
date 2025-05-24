from typing import Optional, Union

from clio.token_store import get_access_token
from clio_client.openapi_client.api.matters_api import MattersApi
from clio_client.openapi_client.api_client import ApiClient
from clio_client.openapi_client.configuration import Configuration
from clio_client.openapi_client.models.matter_update_request import MatterUpdateRequest
from clio_client.openapi_client.models.matter_update_request_data import MatterUpdateRequestData
from clio_client.openapi_client.models.matter_update_request_data_custom_field_values_inner import (
    MatterUpdateRequestDataCustomFieldValuesInner,
)
from clio_client.openapi_client.models.contact_update_request_data_custom_field_values_inner_custom_field import (
    ContactUpdateRequestDataCustomFieldValuesInnerCustomField,
)


def get_authenticated_api(api_cls):
    config = Configuration()
    config.host = "https://app.clio.com/api/v4"
    token = get_access_token()
    config.api_key["Authorization"] = token  # FIX: just the token
    config.api_key_prefix["Authorization"] = "Bearer"  # FIX: set prefix
    print("🔐 Final token used:", token)
    return api_cls(ApiClient(config))


def get_matter_by_id(matter_id: Union[int, str]) -> dict:
    """
    Retrieves a matter by ID.
    """
    if isinstance(matter_id, str):
        matter_id = int(matter_id)

    api = get_authenticated_api(MattersApi)
    response = api.matter_show(matter_id)
    return response.to_dict()


def list_matters(status: Optional[str] = None, practice_area: Optional[str] = None) -> list[dict]:
    """
    List matters optionally filtered by status or practice area.
    """
    api = get_authenticated_api(MattersApi)
    kwargs = {}

    if status:
        kwargs["status"] = status
    if practice_area:
        kwargs["practice_area"] = practice_area

    response = api.matter_index(**kwargs)
    return [m.to_dict() for m in response.data]


def update_matter_limitations_date(matter_id: int, limitations_date: str, custom_field_id: int):
    """
    Updates the 'limitations_date' custom field on a Clio matter.

    Args:
        matter_id: ID of the matter to update.
        limitations_date: ISO-formatted date string (YYYY-MM-DD).
        custom_field_id: The custom field definition ID to update.

    Returns:
        dict: Response from Clio API.
    """
    api = get_authenticated_api(MattersApi)

    # Build the custom field value entry
    custom_field_value = MatterUpdateRequestDataCustomFieldValuesInner(
        value=limitations_date,
        custom_field=ContactUpdateRequestDataCustomFieldValuesInnerCustomField(id=custom_field_id)
    )
    request_data = MatterUpdateRequestData(
        custom_field_values=[custom_field_value]
    )
    request = MatterUpdateRequest(data=request_data)

    response = api.matter_update(id=matter_id, matter_update_request=request)

    return response.to_dict()
