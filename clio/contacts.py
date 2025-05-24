# Wrapper for Clio's contacts API (contact_index, contact_show)
from clio.token_store import get_access_token
from clio_client.openapi_client.api.contacts_api import ContactsApi
from clio_client.openapi_client.api_client import ApiClient
from clio_client.openapi_client.configuration import Configuration

def get_contacts_api() -> ContactsApi:
    token = get_access_token()
    config = Configuration()
    config.api_key["Authorization"] = token  # just the token, no "Bearer"
    config.api_key_prefix["Authorization"] = "Bearer"
    return ContactsApi(ApiClient(config))

def get_contact_by_id(contact_id: str):
    api = get_contacts_api()
    return api.contact_show(contact_id)  # Use the correct method name from SDK

def get_contacts():
    api = get_contacts_api()
    return api.contact_index()  # Returns all contacts

# If you want to filter by client name or practice area, do it in Python:
def get_contacts_by_client_name(client_name: str):
    api = get_contacts_api()
    contacts = api.contact_index().data
    return [c for c in contacts if getattr(c, "name", None) == client_name]

def get_contacts_by_practice_area(practice_area: str):
    api = get_contacts_api()
    contacts = api.contact_index().data
    return [c for c in contacts if getattr(c, "practice_area", None) == practice_area]


