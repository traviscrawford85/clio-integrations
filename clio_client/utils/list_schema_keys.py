import json
import sys


def list_schema_keys(json_file, output_file):
    with open(json_file) as f:
        data = json.load(f)

    schemas = data.get('components', {}).get('schemas', {})
    schema_keys = list(schemas.keys())

    with open(output_file, 'w') as out_f:
        for key in schema_keys:
            out_f.write(key + '\n')

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python list_schema_keys.py openapi.json output.txt")
    else:
        json_file = sys.argv[1]
        output_file = sys.argv[2]
        list_schema_keys(json_file, output_file)
