from clio.token_store import get_access_token
from clio_client.openapi_client.api.custom_actions_api import CustomActionsApi
from clio_client.openapi_client.api_client import ApiClient
from clio_client.openapi_client.configuration import Configuration
from clio_client.openapi_client.models.custom_action_update_request import (
    CustomActionUpdateRequest,
)
from clio_client.openapi_client.models.custom_action_update_request_data import (
    CustomActionUpdateRequestData,
)


def _get_api() -> CustomActionsApi:
    token = get_access_token()  # Fetch the token using the imported function
    config = Configuration()
    config.api_key["Authorization"] = token  # just the token, no "Bearer"
    config.api_key_prefix["Authorization"] = "Bearer"
    return CustomActionsApi(ApiClient(config))


def list_custom_actions():
    return _get_api().custom_action_index().to_dict()


def get_custom_action(action_id: int):
    return _get_api().custom_action_show(id=action_id).to_dict()


def update_custom_action(action_id: int, label: str, target_url: str, ui_reference: str):
    payload = CustomActionUpdateRequest(
        data=CustomActionUpdateRequestData(
            label=label,
            target_url=target_url,
            ui_reference=ui_reference
        )
    )
    return _get_api().custom_action_update(id=action_id, custom_action_update_request=payload).to_dict()
