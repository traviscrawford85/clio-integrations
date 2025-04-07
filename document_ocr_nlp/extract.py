import argparse
import os
import yaml
import pdfplumber
import pytesseract
from pdf2image import convert_from_path
from PIL import Image
import re
import dateparser
import spacy
import json

nlp = spacy.load("en_core_web_sm")

# Load field config from YAML
def load_field_config(path="field_config.yml"):
    with open(path, "r") as f:
        return yaml.safe_load(f)["fields"]

# Dynamic extraction using field_config
def extract_fields(text, field_config):
    clio_fields = {}
    other_fields = {}
    lines = text.splitlines()

    # 1. Dynamic YAML pattern matching (as before)
    for field_key, label_patterns in field_config.items():
        found = False
        for line in lines:
            for label in label_patterns:
                if label.lower() in line.lower():
                    value = line.split(label)[-1].strip()
                    clio_fields[field_key] = value
                    found = True
                    break
            if found:
                break

    # 2. Regex pattern matching for harder fields
    # --- Date of Birth ---
    dob_match = re.search(r"\b(?:DOB|born)\s*[^\d]*([\w]+\s+\d{1,2},?\s+\d{4})", text, re.IGNORECASE)
    if dob_match and "Matter.Client.DateOfBirth" not in clio_fields:
        parsed_dob = dateparser.parse(dob_match.group(1))
        if parsed_dob:
            clio_fields["Matter.Client.DateOfBirth"] = str(parsed_dob.date())

    # --- Phone Number ---
    phone_match = re.search(r"(\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4})", text)
    if phone_match and "Contact.Client.Phone" not in clio_fields:
        clio_fields["Contact.Client.Phone"] = phone_match.group(1)

    # --- Email ---
    email_match = re.search(r"[\w\.-]+@[\w\.-]+\.\w+", text)
    if email_match and "Matter.Client.Email" not in clio_fields:
        clio_fields["Matter.Client.Email"] = email_match.group(0)

    # --- Address (loose detection) ---
    addr_match = re.search(r"\d{1,5}\s+[A-Za-z\s]+(?:Street|St|Ave|Road|Rd|Blvd|Ln|Drive|Dr)\b.*", text)
    if addr_match and "Matter.Client.Address" not in clio_fields:
        clio_fields["Matter.Client.Address"] = addr_match.group(0)

    # 3. NLP Entities (optional fallback)
    doc = nlp(text)
    for ent in doc.ents:
        if ent.label_ == "ORG":
            other_fields.setdefault("Matter.Custom.Provider", ent.text)
        if ent.label_ == "PERSON" and "Matter.Client.Name" not in clio_fields:
            clio_fields["Matter.Client.Name"] = ent.text

    return clio_fields, other_fields


def create_field_report(clio_fields, field_config):
    expected = set(field_config.keys())
    found = set(clio_fields.keys())
    missing = list(expected - found)
    return {
        "total_expected": len(expected),
        "matched": len(found),
        "missing_fields": missing
    }

def save_extracted_data(output_path, file_name, clio_fields, other_fields, field_report):
    base = os.path.splitext(os.path.basename(file_name))[0]
    output_file = os.path.join(output_path, f"{base}_extracted.json")
    with open(output_file, 'w') as f:
        json.dump({
            "clio_fields": clio_fields,
            "other_fields": other_fields,
            "field_report": field_report
        }, f, indent=2)
    print(f"💾 Output saved to: {output_file}")

def process_pdf_smart(pdf_path, output_path, field_config):
    with pdfplumber.open(pdf_path) as pdf:
        for i, page in enumerate(pdf.pages):
            print(f"\n--- Page {i + 1}: {pdf_path} ---")

            text = page.extract_text()
            if text and len(text.strip()) > 30:
                print("✅ Text-based PDF detected.")
            else:
                print("📷 Scanned PDF detected – applying OCR...")
                image = convert_from_path(pdf_path, first_page=i + 1, last_page=i + 1)[0]
                text = pytesseract.image_to_string(image)

            clio_fields, other_fields = extract_fields(text, field_config)
            field_report = create_field_report(clio_fields, field_config)

            print("🧾 Extracted Fields for Clio:")
            if clio_fields:
                for k, v in clio_fields.items():
                    print(f"✅ {k} → {v}")
            else:
                print("⚠️ No Clio-compatible fields were found.")

            if other_fields:
                print("\n📋 Other Fields Detected (Unmapped):")
                for k, v in other_fields.items():
                    print(f"- {k}: {v}")

            print(f"\n📊 Match Score: {field_report['matched']} / {field_report['total_expected']}")
            if field_report['missing_fields']:
                print("⚠️ Missing Fields:", ', '.join(field_report['missing_fields']))

            save_extracted_data(output_path, pdf_path, clio_fields, other_fields, field_report)

def process_image(file_path, output_path, field_config):
    text = pytesseract.image_to_string(Image.open(file_path))
    clio_fields, other_fields = extract_fields(text, field_config)
    field_report = create_field_report(clio_fields, field_config)

    print("🧾 Extracted Fields for Clio:")
    for k, v in clio_fields.items():
        print(f"✅ {k} → {v}")

    if other_fields:
        print("\n📋 Other Fields Detected (Unmapped):")
        for k, v in other_fields.items():
            print(f"- {k}: {v}")

    print(f"\n📊 Match Score: {field_report['matched']} / {field_report['total_expected']}")
    if field_report['missing_fields']:
        print("⚠️ Missing Fields:", ', '.join(field_report['missing_fields']))

    save_extracted_data(output_path, file_path, clio_fields, other_fields, field_report)

def batch_process_folder(folder_path, output_path, field_config):
    for filename in os.listdir(folder_path):
        full_path = os.path.join(folder_path, filename)
        if filename.lower().endswith(".pdf"):
            process_pdf_smart(full_path, output_path, field_config)
        elif filename.lower().endswith((".png", ".jpg", ".jpeg")):
            process_image(full_path, output_path, field_config)

def main():
    parser = argparse.ArgumentParser(description="Extract Clio-ready fields from scanned PDFs or images")
    parser.add_argument("--file", help="Path to a single PDF or image file")
    parser.add_argument("--folder", help="Path to a folder of PDFs/images to batch process")
    parser.add_argument("--output", default="output", help="Directory to save extracted .json files")
    parser.add_argument("--config", default="field_config.yml", help="Path to field config YAML")
    args = parser.parse_args()

    os.makedirs(args.output, exist_ok=True)
    field_config = load_field_config(args.config)

    if args.folder:
        batch_process_folder(args.folder, args.output, field_config)
    elif args.file:
        if args.file.lower().endswith(".pdf"):
            process_pdf_smart(args.file, args.output, field_config)
        else:
            process_image(args.file, args.output, field_config)
    else:
        print("⚠️ Please provide either --file or --folder argument.")

if __name__ == "__main__":
    main()
