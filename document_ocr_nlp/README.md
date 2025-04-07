# 🧠 OCR + NLP Clio Field Extractor

This Python tool extracts structured data from scanned medical records or legal documents using a hybrid **OCR + NLP** approach. It converts raw image or PDF input into Clio-compatible field mappings like `<<Matter.Client.Name>>`, `<<Matter.Custom.DateOfLoss>>`, and more.

---

## 🚀 What It Does

1. Uses **Tesseract OCR** to extract text from images or scanned PDFs
2. Applies **regex** and **spaCy NLP** to identify legal/medical metadata
3. Outputs key-value pairs mapped to Clio Matter fields
4. Supports both image files (`.png`, `.jpg`) and scanned PDFs (`.pdf`)

---

## 📂 Sample Output

```yaml
Matter.Client.Name: Jane Doe
Matter.Custom.DateOfLoss: 2025-03-28
Matter.Custom.Provider: Georgia Orthopedic Institute
```
## 🧰 Dependencies
Install required libraries:

```pip install -r requirements.txt
python -m spacy download en_core_web_sm
```
## 🧪 Usage

```python
process_file("sample_med_record.png")
```
```python
process_pdf("sample_scanned_form.pdf")
```
## 📈 Future Enhancements
* Map extracted data to Clio via API

* Add support for DOB, MRNs, CPT codes

* Confidence scoring on extracted fields

* Field mapping config file for custom docs

## 👤 Author - Travis Crawford

Built for use in law firms automating client matter data intake from medical records and scanned documents.