import pytesseract
import pdfplumber
from PIL import Image
import spacy
import re
import dateparser
from pdf2image import convert_from_path

# Load NLP model
nlp = spacy.load("en_core_web_sm")

def extract_fields(text):
    data = {}

    # Extract Patient Name
    name_match = re.search(r"(Patient Name|Name):\s*(.+)", text, re.IGNORECASE)
    if name_match:
        data["Matter.Client.Name"] = name_match.group(2).strip()

    # Extract Date of Loss
    dol_match = re.search(r"(Date of (Incident|Loss)):\s*([\d/.-]+)", text, re.IGNORECASE)
    if dol_match:
        parsed_date = dateparser.parse(dol_match.group(3))
        if parsed_date:
            data["Matter.Custom.DateOfLoss"] = str(parsed_date.date())

    # NLP: Named Entities
    doc = nlp(text)
    for ent in doc.ents:
        if ent.label_ == "ORG":
            data.setdefault("Matter.Custom.Provider", ent.text)

    return data

# Load image or PDF page
def process_file(image_path):
    text = pytesseract.image_to_string(Image.open(image_path))
    fields = extract_fields(text)
    print("🧾 Extracted Fields for Clio:")
    for key, value in fields.items():
        print(f"{key}: {value}")

# Example usage (PDF to image → image to OCR)
def process_pdf(pdf_path):
    images = convert_from_path(pdf_path)
    for i, image in enumerate(images):
        print(f"\n--- Page {i+1} ---")
        image.save("page_temp.png")
        process_file("page_temp.png")

# Use it
# process_file("sample_med_record.png")
# OR
# process_pdf("sample_scanned_form.pdf")
