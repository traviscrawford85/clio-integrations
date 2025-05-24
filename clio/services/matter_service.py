# clio/services/matter_service.py

from clio.builders.matter_request_builder import (
    MatterUpdateInputModel,
    build_full_update_request,
)
from clio.token_store import get_access_token
from clio_client.openapi_client.api.matters_api import MattersApi
from clio_client.openapi_client.api_client import ApiClient
from clio_client.openapi_client.configuration import Configuration


def update_matter_custom_field(matter_id: int, payload: MatterUpdateInputModel) -> dict:
    request = build_full_update_request(payload)

    config = Configuration()
    token = get_access_token()
    config.api_key["Authorization"] = token  # just the token, no "Bearer"
    config.api_key_prefix["Authorization"] = "Bearer"

    print("🔑 Using token:", token)
    print("🧪 Final Header Preview:")
    print(f"Authorization: {config.api_key_prefix['Authorization']} {config.api_key['Authorization']}")


    api = MattersApi(ApiClient(config))

    return api.matter_update(matter_id, matter_update_request=request).to_dict()
