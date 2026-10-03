"""
Unit tests for embeddings service
Phase 6 testing
"""

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from services.embeddings import EmbeddingsService


class TestEmbeddingsService(unittest.TestCase):

    def setUp(self):
        self.service = EmbeddingsService()

    def test_chunk_text(self):
        """Test chunking text into overlapping segments."""
        print("DEBUG: running test_chunk_text")
        text = "word " * 100
        print(f"DEBUG: text under test = {text[:80]}")

        chunks = self.service.chunk_text(text, chunk_size=20, overlap=5)

        print(f"DEBUG: chunk count = {len(chunks)}; first chunk length = {len(chunks[0]) if chunks else 0}")
        self.assertGreater(len(chunks), 0)
        self.assertLessEqual(len(chunks[0]), 20)
        self.assertTrue(all(len(chunk) <= 20 for chunk in chunks))

    def test_chunk_text_empty_input(self):
        """Empty input should return no chunks."""
        print("DEBUG: running test_chunk_text_empty_input")
        self.assertEqual(self.service.chunk_text("   "), [])
        self.assertEqual(self.service.chunk_text(""), [])

    def test_cosine_similarity(self):
        """Test cosine similarity calculation"""
        vec1 = [1, 0, 0]
        vec2 = [1, 0, 0]

        similarity = self.service.cosine_similarity(vec1, vec2)
        self.assertAlmostEqual(similarity, 1.0)

    def test_find_similar_chunks(self):
        """Test finding similar chunks"""
        query_embedding = [0.1] * 1536
        chunk_embeddings = [[0.1] * 1536 for _ in range(5)]

        indices = self.service.find_similar_chunks(query_embedding, chunk_embeddings, top_k=2)

        self.assertEqual(len(indices), 2)


if __name__ == '__main__':
    unittest.main()
