from pathlib import Path

API_FOLDER = Path("clio_client/openapi_client/api")

COMMON_IMPORTS = {
    "ApiResponse[": "from clio_client.openapi_client.api_response import ApiResponse\n",
    "List[": "from typing import List\n",
    "Dict[": "from typing import Dict\n",
    "Optional[": "from typing import Optional\n",
    "Union[": "from typing import Union\n",
    "datetime": "from datetime import datetime\n",
    "date": "from datetime import date\n",
}

def patch_codegen_imports():
    for py_file in API_FOLDER.glob("*.py"):
        with open(py_file, "r") as f:
            lines = f.readlines()

        needs_patch = False
        existing_imports = "".join(lines)

        new_imports = []
        for token, import_line in COMMON_IMPORTS.items():
            if token in "".join(lines) and import_line not in existing_imports:
                new_imports.append(import_line)
                needs_patch = True

        if needs_patch:
            print(f"📌 Patching {py_file.name}")
            # Find where to insert imports
            insert_index = 0
            for i, line in enumerate(lines):
                if line.startswith("from") or line.startswith("import"):
                    insert_index = i + 1
            lines[insert_index:insert_index] = new_imports

            with open(py_file, "w") as f:
                f.writelines(lines)

if __name__ == "__main__":
    patch_codegen_imports()
