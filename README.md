# Claim Processing Pipeline

## Features
- FastAPI backend
- OCR-based PDF processing
- Multi-agent pipeline:
  - Segregator Agent
  - ID Agent
  - Discharge Summary Agent
  - Itemized Bill Agent

## API

POST /api/process

Form Data:
- claim_id: string
- file: PDF

## Run
uvicorn app.main:app --reload
