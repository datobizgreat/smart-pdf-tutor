# Smart PDF Tutor

An AI-powered web application that helps users learn from PDF documents through intelligent Q&A, summaries, quizzes, and flashcards.

## 🚀 Project Structure

```
smart-pdf-tutor/
├── backend/              # FastAPI backend
│   ├── main.py          # Main application
│   ├── config.py        # Configuration
│   ├── requirements.txt  # Python dependencies
│   ├── .env.example     # Environment variables template
│   └── services/        # Business logic
│       ├── pdf_processor.py    # PDF extraction
│       ├── embeddings.py       # Vector embeddings
│       └── llm_service.py      # LLM integration
├── frontend/            # React frontend
│   ├── src/
│   │   ├── pages/       # Page components
│   │   ├── components/  # Reusable components
│   │   └── App.js       # Main app
│   ├── package.json     # Node dependencies
│   └── public/          # Static files
└── docs/                # Documentation
```

## 📋 Prerequisites

- Python 3.9+
- Node.js 16+
- PostgreSQL (for Phase 11)
- OpenAI API key (for Phase 9)

## 🔧 Setup Instructions

### 1. Backend Setup

```bash
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Copy environment template
cp .env.example .env

# Update .env with your settings (especially OPENAI_API_KEY)
```

### 2. Frontend Setup

```bash
cd frontend

# Install dependencies
npm install

# Start development server
npm start
```

### 3. Run Backend

```bash
cd backend

# Activate virtual environment (if not already active)
source venv/bin/activate  # macOS/Linux
# or
venv\Scripts\activate  # Windows

# Run FastAPI server
python main.py
```

The API will be available at `http://localhost:8000`

## 📖 Current Phase: 1-3 (Basics)

✅ **Phase 1**: Python fundamentals covered in `config.py` and services  
✅ **Phase 2**: ML concepts implemented in embeddings service  
✅ **Phase 3**: FastAPI with basic endpoints for:
- PDF upload
- Text extraction
- Page retrieval

### Current Features:
- Upload PDF files
- Extract text from PDFs
- View extracted pages
- API endpoints for all basic operations

## 🎯 Next Steps (Phase 4+)

- **Phase 4**: Frontend React components (✓ Implemented)
- **Phase 5**: PDF text extraction (✓ Implemented)
- **Phase 6**: Embeddings and vector operations
- **Phase 7**: FAISS vector database integration
- **Phase 8-9**: RAG pipeline and LLM integration
- **Phase 10**: Quiz, summaries, flashcards
- **Phase 11**: User authentication and PostgreSQL
- **Phase 12**: UI polish and deployment

## 🧪 API Endpoints

### Current Endpoints:

- `POST /upload` - Upload a PDF file
- `GET /pdf/{document_id}/pages` - Get all pages from a document
- `DELETE /pdf/{document_id}` - Delete a uploaded PDF file from storage
- `POST /question` - Ask a question (placeholder for Phase 8-9)
- `POST /summarize/{document_id}` - Summarize document (placeholder)
- `POST /quiz/{document_id}` - Generate quiz (placeholder)

### Example Usage:

```bash
# Upload a PDF
curl -X POST -F "file=@document.pdf" http://localhost:8000/upload

# Get document pages
curl http://localhost:8000/pdf/document/pages

# Delete a PDF by document_id
curl -X DELETE http://localhost:8000/pdf/document

# Ask a question
curl -X POST -H "Content-Type: application/json" \
  -d '{"question": "What is...?", "document_id": "document"}' \
  http://localhost:8000/question
```

### Delete PDF in Postman

1. Open Postman.
2. Set the request method to `DELETE`.
3. Enter the URL:
   `http://localhost:8000/pdf/{document_id}`
4. Replace `{document_id}` with the uploaded document ID, such as `my_document`.
5. Click `Send`.

Example response:

```json
{
  "document_id": "my_document",
  "message": "PDF deleted successfully"
}
```

## 🔑 Environment Variables

Create a `.env` file in the `backend` directory:

```env
OPENAI_API_KEY=your_api_key_here
OPENAI_MODEL=gpt-3.5-turbo
DATABASE_URL=postgresql://user:password@localhost/smartpdf
CHUNK_SIZE=500
CHUNK_OVERLAP=50
DEBUG=False
```

## 📚 Learning Path

1. Start with Phase 1-2 concepts (Python basics, ML fundamentals)
2. Understand FastAPI in Phase 3
3. Learn React components in Phase 4
4. Implement PDF processing in Phase 5
5. Progress through phases gradually

## 🚀 Deployment

### Frontend (Vercel)
```bash
cd frontend
npm run build
# Deploy to Vercel
```

### Backend (Render/Railway)
- Push code to GitHub
- Connect repository to Render or Railway
- Set environment variables
- Deploy

## 📝 Notes

- This is a beginner-friendly project designed to teach full-stack AI development
- Start simple and add features gradually
- Each phase builds on the previous one
- Don't try to implement everything at once!

## 🤝 Contributing

Feel free to extend this project with additional features or improvements.

## 📄 License

MIT License

---

**Current Status**: Phase 1-3 Complete ✅  
**Last Updated**: June 2026
