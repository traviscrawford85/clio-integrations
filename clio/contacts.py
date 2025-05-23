# Wrapper for Clio's contacts API (contact_index, contact_show)
# This module provides functions to interact with Clio's contacts API endpoints.
# It includes functions to retrieve a list of contacts and to get details of a specific contact.
# The functions handle API requests, response parsing, and error handling.

from clio_client.openapi_client.configuration import Configuration
from clio_client.openapi_client.api_client import ApiClient
from clio_client.openapi_client.api.contacts_api import ContactsApi
from clio_client.token_store import get_access_token  # Custom function you'll implement

def get_authenticated_api(api_cls):
    """
    Factory to return an authenticated API instance.
    """
    token = get_access_token()
    config = Configuration()
    config.api_key["Authorization"] = f"Bearer {token}"
    return api_cls(ApiClient(config))

def _get_api() -> ContactsApi:
    config = Configuration()
    config.api_key["Authorization"] = f"Bearer {get_access_token()}"
    return ContactsApi(ApiClient(config))

def get_contact_by_id(contact_id: str):
    api = get_authenticated_api(ContactsApi)
    return api.get_contact(contact_id)


def get_contacts_by_client_name(client_name: str):
    api = get_authenticated_api(ContactsApi)
    return api.get_contacts_by_client_name(client_name)


def get_contacts_by_practice_area(practice_area: str):
    api = get_authenticated_api(ContactsApi)
    return api.get_contacts_by_practice_area(practice_area)


