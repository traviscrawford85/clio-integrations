from clio_client.openapi_client.configuration import Configuration
from clio_client.openapi_client.api_client import ApiClient
from clio_client.openapi_client.api.matters_api import MattersApi
from clio_client.token_store import get_access_token  # Custom function you'll implement


def get_authenticated_api(api_cls):
    """
    Factory to return an authenticated API instance.
    """
    token = get_access_token()
    config = Configuration()
    config.api_key["Authorization"] = f"Bearer {token}"
    return api_cls(ApiClient(config))

def _get_api() -> MattersApi:
    config = Configuration()
    config.api_key["Authorization"] = f"Bearer {get_access_token()}"
    return MattersApi(ApiClient(config))

def get_matter_by_id(matter_id: str):
    api = get_authenticated_api(MattersApi)
    return api.get_matter(matter_id)


def get_matter_by_display_number(display_number: str):
    api = get_authenticated_api(MattersApi)
    return api.get_matter_by_display_number(display_number)


def get_matters_by_client_name(client_name: str):
    api = get_authenticated_api(MattersApi)
    return api.get_matters_by_client_name(client_name)


def get_matters_by_status(status: str):
    api = get_authenticated_api(MattersApi)
    return api.get_matters_by_status(status)


def get_matters_by_practice_area(practice_area: str):
    api = get_authenticated_api(MattersApi)
    return api.get_matters_by_practice_area(practice_area)


def update_matter_limitations_date(matter_id: str, limitations_date: str):
    api = get_authenticated_api(MattersApi)
    update_payload = {
        "custom_fields": {
            "limitations_date": limitations_date
        }
    }
    return api.update_matter(matter_id, update_payload)
