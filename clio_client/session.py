from clio.token_store import get_access_token, store_tokens
from clio_client.openapi_client.api.contacts_api import ContactsApi
from clio_client.openapi_client.api.matters_api import MattersApi
from clio_client.openapi_client.api_client import ApiClient
from clio_client.openapi_client.configuration import Configuration
from clio_client.config import CLIO_API_HOST


class ClioSession:
    def __init__(self):
        print("🚀 Using ApiClient")
        self.api_client = self.create_api_client()
        self.matters_api = MattersApi(self.api_client)
        self.contacts_api = ContactsApi(self.api_client)

    def create_api_client(self) -> ApiClient:
        token = get_access_token()
        configuration = Configuration(
            host=CLIO_API_HOST
        )
        configuration.api_key["Authorization"] = token  # just the token
        configuration.api_key_prefix["Authorization"] = "Bearer"
        return ApiClient(configuration=configuration)

    def refresh_token_if_needed(self):
        # This is handled by get_access_token(), so nothing needed here.
        pass
