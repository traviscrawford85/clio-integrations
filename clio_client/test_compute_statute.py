import os
import requests

BASE_URL = os.getenv("BASE_URL", "http://localhost:8000")

def test_compute_statute():
    matter_id = 12345
    url = f"{BASE_URL}/matters/{matter_id}/compute_statute.json"
    response = requests.post(url)
    print("Status:", response.status_code)
    try:
        print("Response:", response.json())
    except ValueError:
        print("Non-JSON Response:", response.text)

def test_webhook_listener():
    url = f"{BASE_URL}/webhook/matter_created"
    payload = {
        "data": {
            "id": 12345,
            "date_of_incident": "2022-01-01"
        }
    }
    response = requests.post(url, json=payload)
    print("Status:", response.status_code)
    try:
        print("Response:", response.json())
    except ValueError:
        print("Non-JSON Response:", response.text)

if __name__ == "__main__":
    test_compute_statute()
    test_webhook_listener()
