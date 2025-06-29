
# 📄 Smart PDF Reader v0.1

A Python-based tool that extracts text and metadata from PDF files — with optional OCR support for scanned/image-based PDFs.

---

## 🚀 Features

- ✅ Extracts plain text from each page of a PDF
- 🧠 Displays metadata (title, author, creation date, etc.)
- 🔍 Optional OCR support using Tesseract for image-based/scanned PDFs
- 📦 Clean Git structure with `.gitignore` and virtual environment support

---

## 🛠 Technologies Used

- Python 3.x
- [PyMuPDF (fitz)](https://pymupdf.readthedocs.io/en/latest/) – PDF parsing
- [pdf2image](https://github.com/Belval/pdf2image) – PDF to image conversion
- [pytesseract](https://github.com/madmaze/pytesseract) – OCR engine (Google Tesseract)
- [Pillow](https://python-pillow.org/) – Image processing

---

## ⚙️ How to Run

1. **Clone this repository**
   
   ```bash
   git clone https://github.com/YOUR_USERNAME/smart-pdf-reader.git
   cd smart-pdf-reader
   
3. **Create and activate virtual environment**
   ```bash
   python -m venv venv
   venv\Scripts\activate  # On Windows

4. **Install dependencies**
   ```bash
   
   pip install -r requirements.txt
5. **Run the main script to extract text**
   ```bash
   
   python extract_text.py
6. **(Optional) Run OCR on scanned PDFs:**
   ```bash
   
   python ocr_text.py

---

## 📂 File Structure
  ```graphql
  
    smart-pdf-reader/
    ├── extract_text.py      # Extract text + metadata from normal PDFs
    ├── ocr_text.py          # OCR for scanned PDFs
    ├── sample.pdf           # Your test PDF
    ├── .gitignore           # Ignores venv, cache files, etc.
    └── README.md            # You're here!
  ```
---

## ✅ Example Output

📄 PDF Metadata:  
title: Machine Learning Notes  
author: Piyush Singhal  
creationDate: D:20240625123000  
  
--- Page 1 ---  
This is sample extracted text from the first page...  
  
---

## 💡 Future Improvements
- Add GUI using Tkinter or Streamlit

- Keyword-based search inside PDFs

- Summarization or question-answering over PDF content

- Upload multiple PDFs and create a cross-document search engine

---

## 👨‍💻 Author
- Piyush Singhal
- [GitHub Profile](https://github.com/singhalpiyush17)

---

## 📜 License
- This project is open-source under the MIT License.
