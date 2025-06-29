 
import fitz  # PyMuPDF

# Load your PDF
doc = fitz.open("user-manual.pdf")  # Replace with your actual file name

# 🧠 Extract metadata
metadata = doc.metadata
print("📄 PDF Metadata:")
for key, value in metadata.items():
    print(f"{key}: {value}")

# Loop through each page and extract text
for page_num, page in enumerate(doc, start=1):
    text = page.get_text()
    print(f"\n--- Page {page_num} ---\n")
    print(text)

# Close the document
doc.close()
