from pdf2image import convert_from_path
import easyocr
import numpy as np

reader = easyocr.Reader(['en'])

def extract_pages(pdf_path):
    images = convert_from_path(pdf_path)
    pages = []

    for img in images:
        img_np = np.array(img)
        result = reader.readtext(img_np, detail=0)
        text = " ".join(result)
        pages.append(text)

    return pages
