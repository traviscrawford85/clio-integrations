# clio-integration/auth/oauth_flow.py

import os
import time
import requests
from datetime import datetime, timedelta

from clio.token_store import store_tokens, get_stored_token_data

CLIO_TOKEN_URL = os.getenv("CLIO_TOKEN_URL", "https://app.clio.com/oauth/token")
CLIENT_ID = os.getenv("CLIO_CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIO_CLIENT_SECRET")
REDIRECT_URI = os.getenv("CLIO_REDIRECT_URI")



