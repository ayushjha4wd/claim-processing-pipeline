# 📄 Claim Processing Pipeline

## 🚀 Overview

This project implements a **Claim Processing Pipeline** using **FastAPI** and **LangGraph** to process medical PDF documents through a **multi-agent architecture**.

The system takes a PDF file as input, classifies its pages into document types, routes them to specialized agents, and returns structured JSON output.

---

## 🎯 Objective

Build an API service that:

* Accepts PDF claim documents
* Segregates pages into document types
* Processes them using multiple agents
* Returns structured extracted data

---

## 🧠 Architecture

The pipeline follows a **LangGraph-based workflow**:

```
START → Segregator → ID Agent → Discharge Agent → Bill Agent → END
```

### Components:

* **Segregator Agent** → Classifies document pages
* **ID Agent** → Extracts identity details
* **Discharge Agent** → Extracts medical summary
* **Billing Agent** → Computes billing information
* **Aggregator (within workflow)** → Combines results

---

## ⚙️ Tech Stack

* **FastAPI** → Backend API
* **LangGraph** → Workflow orchestration
* **PyPDF2** → PDF text extraction
* **Python** → Core logic

---

## 📁 Project Structure

```
claim-processing-pipeline/
│
├── app/
│   ├── main.py
│   ├── api/routes.py
│   ├── agents/
│   ├── graph/workflow.py
│   ├── services/pdf_service.py
│   └── utils/file_handler.py
│
├── uploads/
├── sample_data/
├── requirements.txt
└── README.md
```

---

## 🔄 Workflow Explanation

### 1. File Upload

User sends a PDF file via API.

### 2. PDF Processing

The PDF is converted into text using `PyPDF2`.

### 3. Segregator Agent

* Processes each page
* Classifies pages into document types:

  * identity_document
  * discharge_summary
  * itemized_bill

> ⚠️ Note: Currently uses keyword-based classification.
> Designed to support LLM-based classification in production.

---

### 4. Extraction Agents

Each agent processes only relevant pages:

#### 🪪 ID Agent

* Extracts:

  * Patient Name
  * Date of Birth

#### 🏥 Discharge Agent

* Extracts:

  * Diagnosis
  * Admission Date
  * Discharge Date

#### 💰 Billing Agent

* Calculates:

  * Total billing amount

---

### 5. LangGraph Orchestration

* Each agent is defined as a **node**
* State flows across nodes sequentially
* Ensures modular and scalable design

---

### 6. Aggregation

Outputs from all agents are combined into final JSON.

---

## 🌐 API Endpoint

### POST `/api/process`

### Request:

* `claim_id` (string)
* `file` (PDF)

### Example (cURL):

```
curl -X POST "https://claim-processing-pipeline-hpxp.onrender.com/api/process?claim_id=123" \
-F "file=@C:\Users\ASUS\Downloads\final_image_protected.pdf"
```

---

## 📤 Response Example

```json
{
  "claim_id": "123",
  "identity": {},
  "discharge_summary": {},
  "billing": {
    "total_amount": 0
  }
}
```

---

## 🚀 Deployment

Deployed on Render:

👉 https://claim-processing-pipeline-hpxp.onrender.com

---

## ⚠️ Limitations

* PDF text extraction is limited (image-based PDFs may return empty text)
* Segregator uses rule-based classification (not AI yet)

---

## 🔮 Future Improvements

* Integrate OCR (Tesseract / EasyOCR)
* Add LLM-based classification
* Improve extraction accuracy
* Add more document types and agents

---

## 💡 Key Highlights

* Modular multi-agent architecture
* LangGraph-based workflow orchestration
* Scalable and extensible design
* Cloud-deployed API

---

## 👤 Author

Ayush Kumar
