from pathlib import Path

API_FOLDER = Path("clio_client/openapi_client/api")
IMPORT_LINE = "from clio_client.openapi_client.api_response import ApiResponse\n"

def patch_api_response_imports():
    for py_file in API_FOLDER.glob("*.py"):
        with open(py_file) as f:
            lines = f.readlines()

        if any("ApiResponse[" in line for line in lines) and not any("import ApiResponse" in line for line in lines):
            print(f"📌 Patching {py_file.name}")
            # Insert after all existing imports
            insert_index = 0
            for i, line in enumerate(lines):
                if line.startswith("from") or line.startswith("import"):
                    insert_index = i + 1
            lines.insert(insert_index, IMPORT_LINE)

            with open(py_file, "w") as f:
                f.writelines(lines)

if __name__ == "__main__":
    patch_api_response_imports()
