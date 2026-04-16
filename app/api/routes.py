from fastapi import APIRouter, UploadFile, File
from app.graph.workflow import run_workflow
import os

router = APIRouter()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/api/process")
async def process_claim(claim_id: str, file: UploadFile = File(...)):
    
    file_path = f"{UPLOAD_DIR}/{file.filename}"
    
    with open(file_path, "wb") as f:
        f.write(await file.read())

    result = run_workflow(file_path, claim_id)

    return result
