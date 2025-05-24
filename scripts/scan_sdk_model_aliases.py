import ast
from pathlib import Path

MODEL_DIR = Path("clio_client/openapi_client/models")
OUTPUT_FILE = Path("scripts/sdk_model_aliases.py")


def get_field_names(class_def: ast.ClassDef) -> set:
    return {
        stmt.target.id
        for stmt in class_def.body
        if isinstance(stmt, ast.AnnAssign) and isinstance(stmt.target, ast.Name)
    }


def get_class_category(fields: set, class_def: ast.ClassDef) -> str:
    if fields == {"id"}:
        return "id_only"
    elif {"id", "name"}.issubset(fields):
        return "id_and_name"
    elif is_enum_like(class_def):
        return "enum_like"
    return ""


def is_enum_like(class_def: ast.ClassDef) -> bool:
    # Heuristics: mostly constants or string values
    string_assigns = 0
    total_assigns = 0

    for stmt in class_def.body:
        if isinstance(stmt, ast.Assign):
            total_assigns += 1
            if isinstance(stmt.value, ast.Constant) and isinstance(stmt.value.value, str):
                string_assigns += 1

    return total_assigns > 0 and string_assigns == total_assigns


def find_wrapper_classes(model_dir: Path):
    categorized = {"id_only": [], "id_and_name": [], "enum_like": []}

    for py_file in model_dir.glob("*.py"):
        if py_file.name == "__init__.py":
            continue

        try:
            with open(py_file, encoding="utf-8") as f:
                tree = ast.parse(f.read(), filename=py_file.name)

            for node in ast.walk(tree):
                if isinstance(node, ast.ClassDef):
                    fields = get_field_names(node)
                    category = get_class_category(fields, node)
                    if category:
                        categorized[category].append((py_file.stem, node.name))

        except Exception as e:
            print(f"❌ Error in {py_file.name}: {e}")

    return categorized


def write_alias_file(categorized_classes: dict, output_file: Path):
    with open(output_file, "w") as out:
        out.write("# Auto-generated SDK model import aliases\n\n")

        if categorized_classes["id_only"]:
            out.write("# ID-only wrapper models\n")
            for module, cls in categorized_classes["id_only"]:
                out.write(f"from clio_client.openapi_client.models.{module} import {cls} as {cls}IdModel\n")
            out.write("\n")

        if categorized_classes["id_and_name"]:
            out.write("# ID + Name reference models\n")
            for module, cls in categorized_classes["id_and_name"]:
                out.write(f"from clio_client.openapi_client.models.{module} import {cls} as {cls}RefModel\n")
            out.write("\n")

        if categorized_classes["enum_like"]:
            out.write("# Enum-like models (constant values, likely for dropdowns or types)\n")
            for module, cls in categorized_classes["enum_like"]:
                out.write(f"from clio_client.openapi_client.models.{module} import {cls} as {cls}Enum\n")
            out.write("\n")


# Run the script logic
Path("scripts").mkdir(parents=True, exist_ok=True)
categorized = find_wrapper_classes(MODEL_DIR)
write_alias_file(categorized, OUTPUT_FILE)
OUTPUT_FILE.name
