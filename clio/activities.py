# Wrapper for Clio's activities API (activity_index, activity_create)
from clio_client.openapi_client.configuration import Configuration
from clio_client.openapi_client.api_client import ApiClient
from clio_client.openapi_client.api.activities_api import ActivitiesApi
from clio_client.token_store import get_access_token  # Custom function you'll implement