"""
Smart PDF Tutor - FastAPI Backend
Phase 1-3: Basic API with PDF upload and text extraction
"""

from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import os
from pathlib import Path
import shutil
from pydantic import BaseModel
from typing import List

# Local imports
from services.pdf_processor import PDFProcessor
from services.embeddings import EmbeddingsService
from config import settings

# Initialize FastAPI app
app = FastAPI(
    title="Smart PDF Tutor API",
    description="AI-powered PDF tutoring system",
    version="0.1.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize services
pdf_processor = PDFProcessor()
embeddings_service = EmbeddingsService()

# Create uploads directory if it doesn't exist
UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)


# ============ Models ============
class QuestionRequest(BaseModel):
    question: str
    document_id: str


class UploadResponse(BaseModel):
    document_id: str
    filename: str
    total_pages: int
    text_preview: str


# ============ Routes ============
@app.get("/")
async def root():
    """Root endpoint - API health check"""
    return {
        "message": "Smart PDF Tutor API",
        "status": "running",
        "version": "0.1.0"
    }


@app.post("/upload", response_model=UploadResponse)
async def upload_pdf(file: UploadFile = File(...)):
    """
    Phase 5: Upload and extract text from PDF
    """
    try:
        if not file.filename.lower().endswith('.pdf'):
            raise HTTPException(status_code=400, detail="File must be a PDF")

        # Save uploaded file
        file_path = UPLOAD_DIR / file.filename
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # Extract text from PDF
        extracted_data = pdf_processor.extract_text(str(file_path))

        # Generate document ID (in production, save to database)
        document_id = file.filename.replace('.pdf', '').replace(' ', '_')

        return UploadResponse(
            document_id=document_id,
            filename=file.filename,
            total_pages=extracted_data['total_pages'],
            text_preview=extracted_data['text_preview']
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/pdf/{document_id}/pages")
async def get_pdf_pages(document_id: str):
    """
    Phase 5: Get all pages from a PDF
    """
    try:
        # Find PDF file (in production, query from database)
        pdf_files = list(UPLOAD_DIR.glob("*.pdf"))
        target_pdf = None

        for pdf_file in pdf_files:
            if document_id in pdf_file.name:
                target_pdf = pdf_file
                break

        if not target_pdf:
            raise HTTPException(status_code=404, detail="PDF not found")

        pages = pdf_processor.get_pages(str(target_pdf))
        return {"document_id": document_id, "total_pages": len(pages), "pages": pages}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.delete("/pdf/{document_id}")
async def delete_pdf(document_id: str):
    """Delete a PDF uploaded to the server by document_id."""
    try:
        pdf_files = list(UPLOAD_DIR.glob("*.pdf"))
        target_pdf = None

        for pdf_file in pdf_files:
            if document_id == pdf_file.stem or document_id in pdf_file.name:
                target_pdf = pdf_file
                break

        if not target_pdf:
            raise HTTPException(status_code=404, detail="PDF not found")

        target_pdf.unlink()
        return {
            "document_id": document_id,
            "message": "PDF deleted successfully"
        }

    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/question")
async def ask_question(request: QuestionRequest):
    """
    Phase 8-9: Answer question based on PDF content
    Uses RAG pattern: retrieve relevant chunks + LLM answer
    """
    try:
        # TODO: Phase 6 - Retrieve embeddings from vector database
        # TODO: Phase 9 - Send to LLM with context
        
        return {
            "question": request.question,
            "answer": "RAG system not yet implemented. Coming in Phase 6-9.",
            "sources": []
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/summarize/{document_id}")
async def summarize_document(document_id: str):
    """
    Phase 10: Generate chapter summaries
    """
    return {
        "document_id": document_id,
        "summary": "Feature coming in Phase 10"
    }


@app.post("/quiz/{document_id}")
async def generate_quiz(document_id: str, num_questions: int = 5):
    """
    Phase 10: Generate quiz questions
    """
    return {
        "document_id": document_id,
        "quiz": "Feature coming in Phase 10"
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
