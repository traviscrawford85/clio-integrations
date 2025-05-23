# Wrapper for Clio's notes API (note_index, note_create)
from clio_client.openapi_client.configuration import Configuration
from clio_client.openapi_client.api_client import ApiClient
from clio_client.openapi_client.api.notes_api import NotesApi
from clio_client.token_store import get_access_token  # Custom function you'll implementNotesApi