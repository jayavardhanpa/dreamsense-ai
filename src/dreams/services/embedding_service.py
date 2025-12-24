"""
Embedding service for text embeddings.
"""

from sentence_transformers import SentenceTransformer
import numpy as np

class EmbeddingService:
    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)

    def get_embedding(self, text: str) -> List[float]:
        """Get embedding for text"""
        return self.model.encode(text).tolist()