import json
import os
from datetime import datetime, timedelta

from clio_client.openapi_client import ApiClient, Configuration
from clio_client.openapi_client.api import ContactsApi, MattersApi

from .auth import refresh_token
from .config import CLIO_API_HOST, TOKEN_STORE_PATH


class ClioSession:
    def __init__(self, token_store_path: str = TOKEN_STORE_PATH):
        self.token_store_path = token_store_path
        self.token_data = self.load_token()
        self.api_client = self.create_api_client(self.token_data)
        self.matters_api = MattersApi(self.api_client)
        self.contacts_api = ContactsApi(self.api_client)
        self.ensure_valid_token()

    def load_token(self) -> dict:
        if not os.path.exists(self.token_store_path):
            raise FileNotFoundError(f"Token store not found at {self.token_store_path}")
        with open(self.token_store_path, 'r') as f:
            return json.load(f)

    def save_token(self, token_data: dict):
        with open(self.token_store_path, 'w') as f:
            json.dump(token_data, f, indent=2)

    def create_api_client(self, token_data: dict) -> ApiClient:
        configuration = Configuration(
            host=CLIO_API_HOST,
            access_token=token_data['access_token']
        )
        return ApiClient(configuration=configuration)

    def token_expired(self) -> bool:
        expires_at_str = self.token_data.get('expires_at')
        if not expires_at_str:
            return True
        
        expires_at = datetime.fromisoformat(expires_at_str)
        return datetime.utcnow() >= (expires_at - timedelta(minutes=2))

    def ensure_valid_token(self):
        if self.token_expired():
            print("Access token expired. Refreshing...")
            new_token_data = refresh_token(self.token_data)
            self.token_data = new_token_data
            self.save_token(new_token_data)
            self.api_client = self.create_api_client(new_token_data)
            self.matters_api = MattersApi(self.api_client)
            self.contacts_api = ContactsApi(self.api_client)
