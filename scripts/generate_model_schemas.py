import importlib
import inspect
from pathlib import Path

import yaml

# Base directory and output directory
BASE_PACKAGE = "clio_client.openapi_client.models"
MODEL_DIR = Path("clio_client/openapi_client/models")
OUTPUT_DIR = Path("schemas")
OUTPUT_DIR.mkdir(exist_ok=True)

def dump_model_schemas_to_yaml():
    model_files = [
        f.stem for f in MODEL_DIR.glob("*.py")
        if f.name != "__init__.py"
    ]

    for model_name in model_files:
        module_path = f"{BASE_PACKAGE}.{model_name}"
        try:
            module = importlib.import_module(module_path)

            for name, obj in inspect.getmembers(module, inspect.isclass):
                if obj.__module__ == module_path and hasattr(obj, "model_json_schema"):
                    schema = obj.model_json_schema()
                    output_path = OUTPUT_DIR / f"{name}.yaml"
                    with open(output_path, "w") as f:
                        yaml.dump(schema, f, sort_keys=False)
        except Exception as e:
            print(f"❌ Failed to process {module_path}: {e}")

dump_model_schemas_to_yaml()
