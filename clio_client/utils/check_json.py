import json


def check_json_load(path):
    try:
        with open(path, encoding='utf-8') as f:
            spec = json.load(f)
        print("✅ JSON loaded successfully.")
        print("Top-level keys:")
        for key in spec.keys():
            print(f"  - {key}")
    except Exception as e:
        print(f"❌ Failed to load JSON: {e}")

# Example usage:
# check_json_load("path/to/your_openapi.json")
