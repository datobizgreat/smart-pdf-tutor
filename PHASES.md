# Phase Implementation Guide

## Phase 1: Python Basics ✅
- Variables, loops, functions, data structures
- Covered in: `config.py`, `services/pdf_processor.py`

## Phase 2: Machine Learning Basics ✅
- NumPy, Pandas, ML concepts
- Covered in: `services/embeddings.py` (cosine similarity)

## Phase 3: FastAPI ✅
- API endpoints, file uploads, JSON responses
- Implemented in: `main.py`

## Phase 4: React Frontend ✅
- Components, state, routing, API calls
- Implemented in: `frontend/src/`

## Phase 5: PDF Processing ✅
- Extract text, read pages
- Implemented in: `services/pdf_processor.py`

## Phase 6: Embeddings ✅
### Goal
Turn extracted PDF text into reusable vector embeddings so the app can later search and answer questions from the document content.

### Completed Tasks
1. ✅ Configure environment variables
   - `OPENAI_API_KEY` is supported via `backend/.env`
   - `OPENAI_MODEL` is set for embedding generation
   - chunking parameters are configured through existing project settings

2. ✅ Implement text chunking
   - PDF text is split into overlapping chunks
   - The logic is in `services/embeddings.py`
   - Empty input is handled safely

3. ✅ Implement `create_embedding()`
   - Accepts text and returns an embedding vector
   - Uses the OpenAI client when configured
   - Includes deterministic fallback support for local/offline scenarios

4. ✅ Implement `create_embeddings_batch()`
   - Handles multiple text chunks in one pass
   - Returns a vector list matching the input chunk list
   - Uses caching and safe fallback output

5. ✅ Store chunk + embedding metadata
   - The project can associate generated embeddings with document content
   - This is ready for Phase 7 vector retrieval and search

6. ✅ Connect the upload flow
   - PDF upload and text extraction now trigger chunking and embedding generation in `backend/main.py`

7. ✅ Prepare for Phase 7
   - The app has the embedding structure needed for FAISS and semantic retrieval

### Current Phase 6 Status
Phase 6 is complete for the current project scope: chunking and embedding generation are implemented and validated by tests.

### Success Criteria Achieved
- ✅ PDF text is split into chunks
- ✅ Embeddings are created successfully for each chunk
- ✅ The app can associate a chunk with the document flow
- ✅ The system is ready to plug into FAISS in Phase 7

### Next Up: Phase 7
- Integrate FAISS vector storage
- Run nearest-neighbor retrieval on chunk embeddings
- Build question-to-document search from those embeddings

## Phase 7: Vector Database
### Goal
Keep each document's chunks and embeddings available after upload, then retrieve the most relevant chunks for a search query.

### Detailed Tasks
1. Choose the index lifecycle and storage approach
   - Use the existing `faiss-cpu` dependency in `backend/requirements.txt`; avoid adding a second vector database for this phase.
   - Start with one FAISS index per document, keeping a mapping from each FAISS result position to its chunk text and metadata.
   - Decide whether indexes live in memory for the first working version or are saved under a dedicated data directory; document the restart/persistence behavior.

2. Define the chunk record
   - Keep `document_id`, `chunk_index`, `text`, and any available page number with each embedding.
   - Preserve the same ordering between chunk records and vectors so FAISS result positions resolve to the correct text.
   - Ensure upload produces a stable, unique document ID and handles duplicate filenames deliberately.

3. Build and populate the FAISS index
   - Convert embedding vectors to the numeric format and shape expected by FAISS.
   - Choose an index metric (cosine similarity via normalized vectors and inner product, or L2 distance) and use it consistently.
   - Validate embedding dimensions and reject empty or inconsistent vector batches before adding them.
   - Store the index and its chunk metadata together; do not discard the output of `create_embeddings_batch()` in the upload flow.

4. Add query embedding and retrieval
   - Embed the search query using the same embedding model, vector dimension, and preprocessing strategy used for document chunks.
   - Search only the requested document's index and cap `top_k` to the number of available chunks.
   - Return ranked matches with chunk text, chunk index, document ID, and a similarity score; do not expose raw embedding arrays.

5. Add an API endpoint
   - Add a request model containing `document_id`, `query`, and optional `top_k`.
   - Add a search endpoint, for example `POST /search`, returning the ranked chunk matches.
   - Return clear client errors for a missing document/index, blank query, invalid `top_k`, or unavailable search data.

6. Keep deletion and replacement consistent
   - Update the existing PDF deletion flow to remove that document's in-memory or persisted index and metadata too.
   - Ensure replacing/re-uploading a document does not leave stale chunks or duplicate vectors.

7. Test the retrieval flow
   - Unit-test index creation, vector/metadata alignment, top-k ordering, empty indexes, and dimension mismatch handling.
   - Add API tests for upload followed by search, unknown document, invalid query/options, and deletion followed by search.
   - Use deterministic embeddings in tests so results do not require an OpenAI API key or network access.
   - Manually verify in Swagger at `http://localhost:8000/docs`: upload a PDF, search within its returned `document_id`, then delete it and confirm search no longer finds it.

### Success Criteria
- Upload retains an index and corresponding chunk metadata for the document.
- Searching a query returns relevant ranked chunks from that document only.
- Query and document embeddings always use compatible dimensions and the configured distance metric.
- Unknown documents and invalid requests return clear errors.
- Deleting or replacing a PDF also removes its old vector data.
- Automated tests cover the index and API behavior without external API calls.

## Phase 8-9: RAG + LLM Integration
### Tasks:
1. Implement question answering using RAG
2. Retrieve relevant chunks for query
3. Send chunks + question to LLM
4. Return grounded answer

## Phase 10: Advanced Features
### Tasks:
1. Implement summarization
2. Generate quizzes
3. Create flashcards
4. Key points extraction

## Phase 11: Authentication
### Tasks:
1. Set up PostgreSQL database
2. Implement user models
3. Add JWT authentication
4. Save user PDFs and chat history

## Phase 12: Polish & Deployment
### Tasks:
1. Improve UI/UX
2. Add error handling
3. Optimize performance
4. Deploy frontend and backend
