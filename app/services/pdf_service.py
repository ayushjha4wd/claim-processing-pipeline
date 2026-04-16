from PyPDF2 import PdfReader

def extract_pages(pdf_path):
    reader = PdfReader(pdf_path)
    pages = []

    for page in reader.pages:
        text = page.extract_text() or ""
        pages.append(text)

    return pages
