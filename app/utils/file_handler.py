import os
import uuid

UPLOAD_DIR = "uploads"

def save_file(file):
    if not os.path.isdir(UPLOAD_DIR):
        os.makedirs(UPLOAD_DIR, exist_ok=True)

    # create unique filename
    unique_name = f"{uuid.uuid4()}_{file.filename}"
    file_path = os.path.join(UPLOAD_DIR, unique_name)

    with open(file_path, "wb") as f:
        f.write(file.file.read())

    return file_path
