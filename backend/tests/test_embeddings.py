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
