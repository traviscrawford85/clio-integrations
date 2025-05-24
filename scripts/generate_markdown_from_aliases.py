from pathlib import Path

OUTPUT_FILE = Path("scripts/sdk_model_aliases.py")
MARKDOWN_DOC = Path("scripts/sdk_model_aliases.md")


def generate_markdown_from_aliases(alias_file: Path, markdown_file: Path):
    section = ""
    with open(alias_file) as f, open(markdown_file, "w") as out:
        out.write("# 🧾 Clio SDK Model Aliases\n")
        out.write("This file explains common SDK model types auto-discovered for use with Clio’s API.\n\n")

        for line in f:
            if line.startswith("#"):
                section = line.strip("# \n")
                out.write(f"## {section}\n\n")
                if "ID-only" in section:
                    out.write("- **Used for fields that only need an `id`, e.g. `group`, `responsible_attorney`.**\n\n")
                elif "ID + Name" in section:
                    out.write("- **Used when both `id` and `name` are present, typically in dropdown or lookup fields.**\n\n")
                elif "Enum" in section:
                    out.write("- **Used for fixed value sets like `status`, `type`, or `priority`.**\n\n")
            elif line.startswith("from"):
                parts = line.strip().split(" import ")
                module_path = parts[0].replace("from clio_client.openapi_client.models.", "")
                class_name, alias = parts[1].split(" as ")
                out.write(f"- `{alias}` → `{class_name}` from `{module_path}.py`\n")

        out.write("\n---\n*Generated automatically by `scan_sdk_model_aliases.py`.*\n")


# Generate markdown summary
generate_markdown_from_aliases(OUTPUT_FILE, MARKDOWN_DOC)
MARKDOWN_DOC.name
