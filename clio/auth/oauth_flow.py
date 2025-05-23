# firm_clio/auth/oauth_flow.py
import os
import time
import requests
from clio_client.token_store import get_access_token, refresh_access_token, store_tokens

CLIO_TOKEN_URL = os.getenv("CLIO_TOKEN_URL", "https://app.clio.com/oauth/token")
CLIENT_ID = os.getenv("CLIO_CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIO_CLIENT_SECRET")


def refresh_clio_token_if_needed() -> str:
    try:
        # Will return valid token or auto-refresh
        return get_access_token()
    except Exception as e:
        print(f"⚠️ Token fetch/refresh failed: {e}")
        raise
