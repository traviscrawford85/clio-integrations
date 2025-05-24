import requests


# Register webhook with Clio API
def register_clio_webhook(callback_url: str, event_types: list[str], access_token: str):
    """
    Register a webhook with Clio's API.

    Args:
        callback_url (str): The endpoint Clio should send event payloads to.
        event_types (list[str]): A list of event types to subscribe to.
        access_token (str): OAuth access token for authenticating with Clio.
    """
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    data = {
        "data": {
            "callback_url": callback_url,
            "event_types": event_types
        }
    }
    response = requests.post("https://app.clio.com/api/v4/webhooks", json=data, headers=headers)

    if response.status_code == 201:
        print("✅ Webhook registered successfully.")
    else:
        print(f"❌ Failed to register webhook: {response.status_code} {response.text}")
