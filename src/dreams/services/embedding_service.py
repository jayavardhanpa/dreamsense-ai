"""
Embedding service for text embeddings.
"""

import logging
from sentence_transformers import SentenceTransformer
import numpy as np
from typing import List

logger = logging.getLogger(__name__)

class EmbeddingService:
    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)

    def get_embedding(self, text: str) -> List[float]:
        """Get embedding for text"""
        logger.debug(f"Generating embedding for text: {text[:50]}...")
        embedding = self.model.encode(text).tolist()
        logger.debug(f"Embedding generated with dimension {len(embedding)}")
        return embedding