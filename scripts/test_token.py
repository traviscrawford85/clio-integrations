from clio.token_store import get_access_token
import requests

token = get_access_token()
headers = {"Authorization": f"Bearer {token}"}

response = requests.get("https://app.clio.com/api/v4/users/who_am_i", headers=headers)
print(response.status_code)
print(response.json())
