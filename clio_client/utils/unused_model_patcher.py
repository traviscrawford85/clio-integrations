import difflib
import json


def load_openapi(file_path):
    with open(file_path) as f:
        return json.load(f)

def find_unused_models(spec):
    models = set(spec.get('components', {}).get('schemas', {}).keys())
    refs = set()

    def recurse(obj):
        if isinstance(obj, dict):
            for k, v in obj.items():
                if k == '$ref' and isinstance(v, str):
                    ref = v.split('/')[-1]
                    refs.add(ref)
                else:
                    recurse(v)
        elif isinstance(obj, list):
            for item in obj:
                recurse(item)

    recurse(spec.get('paths', {}))
    return models - refs

def suggest_endpoints(model_name, paths):
    candidates = []
    for path in paths:
        if difflib.get_close_matches(model_name.lower(), [path.lower()]):
            candidates.append(path)
    return candidates

def generate_patch(unused_models, paths):
    patch = {'paths': {}}
    for model in unused_models:
        path = f"/generated/{model.lower()}.json"
        patch['paths'][path] = {
            "get": {
                "summary": f"Generated endpoint for {model}",
                "responses": {
                    "200": {
                        "description": "OK",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": f"#/components/schemas/{model}"
                                }
                            }
                        }
                    }
                }
            }
        }
    return patch

def main():
    spec = load_openapi('openapi_cleaned.json')
    unused = find_unused_models(spec)
    print(f"Unused models: {unused}")

    candidates = {model: suggest_endpoints(model, spec['paths'].keys()) for model in unused}
    print("Candidate endpoints:")
    for model, matches in candidates.items():
        print(f"{model}: {matches}")

    patch = generate_patch(unused, spec['paths'].keys())
    with open('openapi_patch.json', 'w') as f:
        json.dump(patch, f, indent=2)
    print("Generated patch saved as openapi_patch.json")

if __name__ == "__main__":
    main()
