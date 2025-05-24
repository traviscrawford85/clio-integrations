# scripts/authorize_and_fetch_tokens.py

import http.server
import json
import os
import socketserver
import webbrowser
from datetime import datetime, timedelta
from urllib.parse import parse_qs, urlparse

import httpx
from dotenv import load_dotenv

load_dotenv()

PORT = 8001
CLIENT_ID = os.getenv("CLIO_CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIO_CLIENT_SECRET")
REDIRECT_URI = os.getenv("CLIO_REDIRECT_URI")
TOKEN_URL = os.getenv("CLIO_TOKEN_URL", "https://app.clio.com/oauth/token")
TOKEN_STORE_PATH = os.path.join(os.path.dirname(__file__), ".", "clio_client", "clio_token_store.json")

class ReusableTCPServer(socketserver.TCPServer):
    allow_reuse_address = True

def run_oauth_flow():
    auth_url = (
        f"https://app.clio.com/oauth/authorize"
        f"?response_type=code"
        f"&client_id={CLIENT_ID}"
        f"&redirect_uri={REDIRECT_URI}"
        f"&scope=all"
    )
    print("🌐 Opening browser for Clio OAuth...")
    webbrowser.open(auth_url)

    with ReusableTCPServer(("127.0.0.1", PORT), OAuthHandler) as httpd:
        print(f"⏳ Waiting for OAuth callback on port {PORT}...")
        httpd.handle_request()


class OAuthHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        query = parse_qs(urlparse(self.path).query)
        code = query.get("code", [None])[0]

        if not code:
            self.send_error(400, "Missing code in callback.")
            return

        resp = httpx.post(
            TOKEN_URL,
            data={
                "grant_type": "authorization_code",
                "client_id": CLIENT_ID,
                "client_secret": CLIENT_SECRET,
                "redirect_uri": REDIRECT_URI,
                "code": code,
            },
            headers={"Accept": "application/json"}
        )
        resp.raise_for_status()
        tokens = resp.json()
        tokens["expires_at"] = (datetime.utcnow() + timedelta(seconds=tokens["expires_in"])).isoformat()

        with open(TOKEN_STORE_PATH, "w") as f:
            json.dump(tokens, f, indent=2)

        self.send_response(200)
        self.end_headers()
        self.wfile.write("✅ Clio Authorization Complete! You can close this tab.".encode())

        print(f"✅ Access and refresh tokens saved to {TOKEN_STORE_PATH}")

# Duplicate run_oauth_flow removed to resolve function name conflict.

if __name__ == "__main__":
    run_oauth_flow()
