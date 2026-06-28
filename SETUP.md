# Development Setup Guide

## Quick Start

### 1. Backend Quick Start

```bash
cd backend
python -m venv venv
venv\Scripts\activate  # Windows
# or source venv/bin/activate  # macOS/Linux
pip install -r requirements.txt
cp .env.example .env
python main.py
```

Backend will run on `http://localhost:8000`

### 2. Frontend Quick Start

```bash
cd frontend
npm install
npm start
```

Frontend will run on `http://localhost:3000`

## Important Files

### Backend
- `main.py` - FastAPI application entry point
- `config.py` - Configuration and environment variables
- `services/pdf_processor.py` - PDF text extraction logic
- `services/embeddings.py` - Vector embeddings (Phase 6)
- `services/llm_service.py` - LLM integration (Phase 9)

### Frontend
- `src/pages/Home.js` - Landing page with upload
- `src/pages/Chat.js` - Chat interface for Q&A
- `src/components/PDFUpload.js` - File upload component
- `src/components/Navigation.js` - Navigation bar

## Troubleshooting

### Backend Issues

**Import Error: No module named 'pypdf'**
```bash
pip install pypdf
```

**Port 8000 already in use**
```bash
# Change port in main.py or kill process using port 8000
```

**CORS Error when calling from frontend**
- Make sure backend is running on `http://localhost:8000`
- CORS is enabled in `main.py`

### Frontend Issues

**Dependencies not installing**
```bash
rm -rf node_modules package-lock.json
npm install
```

**React Router not working**
- Make sure you're using React Router v6

## Database Setup (For Phase 11)

```bash
# Install PostgreSQL
# Create database
createdb smartpdf

# Update DATABASE_URL in .env
```

## API Testing

Use Postman or curl to test endpoints:

```bash
# Test health
curl http://localhost:8000

# Upload PDF
curl -X POST -F "file=@test.pdf" http://localhost:8000/upload
```

## Next Phase: Embeddings (Phase 6)

To implement Phase 6:
1. Get OpenAI API key
2. Update `.env` with `OPENAI_API_KEY`
3. Implement `create_embedding()` in `services/embeddings.py`
4. Create FAISS index for storing embeddings

## Useful Resources

- FastAPI Docs: https://fastapi.tiangolo.com
- React Docs: https://react.dev
- PyPDF: https://github.com/py-pdf/pypdf
- OpenAI API: https://platform.openai.com/docs
