import json
import sys


def find_refs(data, path=''):
    if isinstance(data, dict):
        for key, value in data.items():
            new_path = f"{path}/{key}" if path else key
            if key == '$ref':
                print(f"{new_path}: {value}")
            find_refs(value, new_path)
    elif isinstance(data, list):
        for index, item in enumerate(data):
            new_path = f"{path}[{index}]"
            find_refs(item, new_path)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python find_refs.py openapi.json")
        sys.exit(1)

    json_file = sys.argv[1]
    with open(json_file, 'r') as f:
        data = json.load(f)

    find_refs(data)
