# firm_clio/auth/oauth_server.py

import os
import time
import json
import webbrowser
import requests

from flask import Flask, redirect, request

from clio.token_store import store_tokens

app = Flask(__name__)


def build_auth_url(state: str = "default") -> str:
    redirect_uri = os.getenv("CLIO_REDIRECT_URI")
    print(f"🔗 Using redirect_uri: {redirect_uri}")
    return (
        f"https://app.clio.com/oauth/authorize?"
        f"client_id={os.getenv('CLIO_CLIENT_ID')}&"
        f"redirect_uri={redirect_uri}&"
        f"response_type=code&"
        f"scope=all&"
        f"state={state}"
    )


@app.route("/")
def home():
    # Dynamically identify the user (e.g., from environment, session, or request arg)
    user_identifier = os.getenv("CLIO_USER_ID", "default_user")
    return redirect(build_auth_url(state=user_identifier))


@app.route("/api/oauth/callback")
def callback():
    code = request.args.get("code")
    state = request.args.get("state", "unknown_user")

    payload = {
        "grant_type": "authorization_code",
        "client_id": os.getenv("CLIO_CLIENT_ID"),
        "client_secret": os.getenv("CLIO_CLIENT_SECRET"),
        "redirect_uri": os.getenv("CLIO_REDIRECT_URI"),
        "code": code,
    }

    token_response = requests.post("https://app.clio.com/oauth/token", data=payload)

    if token_response.status_code != 200:
        return f"❌ Clio Authorization Error: {token_response.text}", 400

    tokens = token_response.json()
    tokens["expires_at"] = int(time.time()) + tokens.get("expires_in", 3600)

    # ✅ Store tokens in database using your centralized logic
    store_tokens(
        access_token=tokens["access_token"],
        refresh_token=tokens["refresh_token"],
        expires_in=tokens["expires_in"]
    )

    # Fetch and log user info to confirm successful authorization
    headers = {"Authorization": f"Bearer {tokens['access_token']}"}
    user_info_resp = requests.get("https://app.clio.com/api/v4/users/who_am_i", headers=headers)

    if user_info_resp.status_code == 200:
        user_data = user_info_resp.json()
        user_info = user_data.get("data", {})
        print("📦 Full user info response:\n", json.dumps(user_data, indent=2))

        print("👤 Logged in as:", user_info.get("name", "Unknown"))
        print("🆔 User ID:", user_info.get("id"))
        account_id = user_info.get("account_id") or user_info.get("account", {}).get("id")
        print("🏢 Account ID:", account_id)
    else:
        print("⚠️ Could not retrieve user info:", user_info_resp.text)

    return f"✅ Clio Authorization Complete for user '{state}'. Tokens saved to database!"


if __name__ == "__main__":
    if os.environ.get("WERKZEUG_RUN_MAIN") != "true":
        webbrowser.open("http://localhost:8001/")
    app.run(debug=True, port=8001)
