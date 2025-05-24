import importlib
import inspect
from pathlib import Path

# Adjust these based on your actual SDK layout
BASE_PACKAGE = "clio_client.openapi_client.models"

def get_all_model_classes():
    model_path = Path("clio_client/openapi_client/models")
    module_names = [
        f"{BASE_PACKAGE}.{f.stem}"
        for f in model_path.glob("*.py")
        if f.name != "__init__.py"
    ]

    for module_name in module_names:
        try:
            module = importlib.import_module(module_name)
            for name, obj in inspect.getmembers(module, inspect.isclass):
                if obj.__module__ == module_name:
                    print(f"📦 {module_name}.{name}")
                    print("  Fields:", getattr(obj, "model_fields", "⚠️ Not a Pydantic model"))
                    print()
        except Exception as e:
            print(f"❌ Failed to import {module_name}: {e}")

if __name__ == "__main__":
    get_all_model_classes()
