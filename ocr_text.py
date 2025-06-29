import pytesseract
from pdf2image import convert_from_path
from PIL import Image

# Set path to Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Convert PDF pages to images
pages = convert_from_path("user-manual.pdf", 300)  # 300 dpi for good accuracy

# Run OCR on each image
for i, page in enumerate(pages, start=1):
    text = pytesseract.image_to_string(page)
    print(f"\n--- OCR Text from Page {i} ---\n")
    print(text)
 
