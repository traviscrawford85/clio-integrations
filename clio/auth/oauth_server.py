# firm_clio/auth/oauth_server.py
import os
import time
import webbrowser
import requests
from flask import Flask, redirect, request
from clio_client.token_store import store_tokens

app: Flask = Flask(__name__)


def build_auth_url():
    redirect_uri = os.getenv("CLIO_REDIRECT_URI")
    print(f"🔗 Using redirect_uri: {redirect_uri}")
    return (
        f"https://app.clio.com/oauth/authorize?"
        f"client_id={os.getenv('CLIO_CLIENT_ID')}&"
        f"redirect_uri={redirect_uri}&"
        f"response_type=code&"
        f"scope=all"
    )


@app.route("/")
def home():
    return redirect(build_auth_url())


@app.route("/api/oauth/callback")
def callback():
    code = request.args.get("code")

    payload = {
        "grant_type": "authorization_code",
        "client_id": os.getenv("CLIO_CLIENT_ID"),
        "client_secret": os.getenv("CLIO_CLIENT_SECRET"),
        "redirect_uri": os.getenv("CLIO_REDIRECT_URI"),
        "code": code,
    }

    token_response = requests.post("https://app.clio.com/oauth/token", data=payload)

    if token_response.status_code != 200:
        return f"❌ Clio Authorization Error: {token_response.text}"

    tokens = token_response.json()
    tokens["expires_at"] = int(time.time()) + tokens.get("expires_in", 3600)

    # ✅ Store tokens in database using token_store.py
    store_tokens(
        access_token=tokens["access_token"],
        refresh_token=tokens["refresh_token"],
        expires_in=tokens["expires_in"]
    )

    # Optional: get user info to verify successful login
    headers = {"Authorization": f"Bearer {tokens['access_token']}"}
    user_info_resp = requests.get("https://app.clio.com/api/v4/users/who_am_i", headers=headers)

    if user_info_resp.status_code == 200:
        user_data = user_info_resp.json()
        print("👤 Logged in as:", user_data.get("data", {}).get("name", "Unknown"))
        print("🆔 User ID:", user_data.get("data", {}).get("id"))
        print("🏢 Account ID:", user_data.get("data", {}).get("account_id"))
    else:
        print("⚠️ Could not retrieve user info:", user_info_resp.text)

    return "✅ Clio Authorization Complete. Tokens saved to database!"


if __name__ == "__main__":
    if os.environ.get("WERKZEUG_RUN_MAIN") != "true":
        webbrowser.open("http://localhost:5000/")

    app.run(debug=True, port=5000)
