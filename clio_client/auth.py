import os
from datetime import datetime, timedelta

import requests
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.getenv("CLIO_CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIO_CLIENT_SECRET")
REDIRECT_URI = os.getenv("CLIO_REDIRECT_URI")
TOKEN_URL = "https://app.clio.com/oauth/token"

def refresh_token(token_data: dict) -> dict:
    refresh_token = token_data['refresh_token']

    response = requests.post(
        TOKEN_URL,
        data={
            'grant_type': 'refresh_token',
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET,
            'refresh_token': refresh_token,
            'redirect_uri': REDIRECT_URI,
        },
        headers={
            'Accept': 'application/json'
        }
    )

    if response.status_code != 200:
        raise Exception(f"Failed to refresh token: {response.text}")

    token_response = response.json()
    return {
        "access_token": token_response["access_token"],
        "refresh_token": token_response.get("refresh_token", refresh_token),
        "expires_at": (datetime.utcnow() + timedelta(seconds=token_response["expires_in"])).isoformat()
    }
