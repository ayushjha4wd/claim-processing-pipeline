from pdf2image import convert_from_path
import pytesseract

def extract_pages(pdf_path):
    images = convert_from_path(pdf_path)
    pages = []

    for img in images:
        text = pytesseract.image_to_string(img)
        pages.append(text)

    return pages
