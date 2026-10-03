"""
Embeddings service - Phase 6
Handles text embeddings and vector operations
"""

from typing import List
import hashlib

import numpy as np
from openai import OpenAI

from config import settings


class EmbeddingsService:
    """
    Handle embeddings creation and similarity search.
    Falls back to deterministic vectors when an API key is missing or the
    OpenAI request fails during local development.
    """

    def __init__(self):
        """Initialize embeddings service"""
        self.client = OpenAI(api_key=settings.openai_api_key) if settings.openai_api_key else None
        self.embedding_model = settings.openai_model or "text-embedding-3-small"
        self.embeddings_cache = {}

    def _fallback_embedding(self, text: str) -> List[float]:
        """Create a deterministic embedding when OpenAI is unavailable."""
        if not text:
            return []

        digest = hashlib.sha256(text.encode("utf-8")).hexdigest()
        vector = []
        for i in range(1536):
            value = (int(digest[i % len(digest)], 16) + i * 13 + len(text)) % 1000
            vector.append(round(value / 1000.0, 6))
        return vector

    def chunk_text(self, text: str, chunk_size: int = 500, overlap: int = 50) -> List[str]:
        """Split text into overlapping chunks."""
        if not text or not text.strip():
            return []

        chunks = []
        start = 0

        while start < len(text):
            end = min(start + chunk_size, len(text))
            chunk = text[start:end].strip()
            if chunk:
                chunks.append(chunk)
            if end == len(text):
                break
            start += max(1, chunk_size - overlap)

        return chunks

    def create_embedding(self, text: str) -> List[float]:
        """Create an embedding for a single text value."""
        if not text or not text.strip():
            return []

        if text in self.embeddings_cache:
            return self.embeddings_cache[text]

        try:
            if self.client is None:
                raise ValueError("OpenAI API key is missing")

            response = self.client.embeddings.create(
                model=self.embedding_model,
                input=text
            )
            embedding = response.data[0].embedding
        except Exception:
            embedding = self._fallback_embedding(text)

        self.embeddings_cache[text] = embedding
        return embedding

    def create_embeddings_batch(self, texts: List[str]) -> List[List[float]]:
        """Create embeddings for multiple texts."""
        if not texts:
            return []

        if len(texts) == 1:
            return [self.create_embedding(texts[0])]

        try:
            if self.client is None:
                raise ValueError("OpenAI API key is missing")

            response = self.client.embeddings.create(
                model=self.embedding_model,
                input=texts
            )
            embeddings = [item.embedding for item in response.data]
        except Exception:
            embeddings = [self._fallback_embedding(text) for text in texts]

        for text, embedding in zip(texts, embeddings):
            self.embeddings_cache[text] = embedding

        return embeddings

    def cosine_similarity(self, vec1: List[float], vec2: List[float]) -> float:
        """
        Calculate cosine similarity between two vectors

        Args:
            vec1: First vector
            vec2: Second vector

        Returns:
            Similarity score (0-1)
        """
        vec1 = np.array(vec1)
        vec2 = np.array(vec2)

        if np.linalg.norm(vec1) == 0 or np.linalg.norm(vec2) == 0:
            return 0.0

        similarity = np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))
        return float(similarity)

    def find_similar_chunks(self, query_embedding: List[float], chunk_embeddings: List[List[float]], top_k: int = 5) -> List[int]:
        """
        Find top-k most similar chunks

        Args:
            query_embedding: Query embedding vector
            chunk_embeddings: List of chunk embeddings
            top_k: Number of top similar chunks to return

        Returns:
            Indices of top-k similar chunks
        """
        if not chunk_embeddings:
            return []

        similarities = []
        for idx, chunk_embedding in enumerate(chunk_embeddings):
            sim = self.cosine_similarity(query_embedding, chunk_embedding)
            similarities.append((idx, sim))

        similarities.sort(key=lambda x: x[1], reverse=True)
        return [idx for idx, _ in similarities[:top_k]]
