"""
Local HuggingFace client wrapper using transformers.
"""

import logging
from typing import List
from transformers import pipeline
from .hf_client import HFClient

logger = logging.getLogger(__name__)


class LocalHFClient(HFClient):
    def __init__(self, default_sentiment_model: str):
        """
        All configuration is injected.
        """
        self.default_sentiment_model = default_sentiment_model
        self._models = {}

    def _load_model(self, model_name: str, task: str):
        if model_name not in self._models:
            logger.info(
                "Loading HF model",
                extra={"model": model_name, "task": task}
            )
            self._models[model_name] = pipeline(task, model=model_name)
        return self._models[model_name]

    def analyze_text(
        self,
        text: str,
        model_name: str | None = None
    ):
        """
        Sentiment analysis.
        """
        model_name = model_name or self.default_sentiment_model
        model = self._load_model(model_name, "sentiment-analysis")
        return model(text)

    def classify_emotion(self, text: str):
        """
        Emotion classification (can later switch to better model).
        """
        # TEMP: placeholder logic
        logger.debug("Classifying emotion", extra={"text_len": len(text)})
        return [{"label": "joy", "score": 0.9}]

    def embed(self, texts: List[str]):
        """
        Embeddings (placeholder for Phase-1).
        """
        logger.debug("Generating embeddings", extra={"count": len(texts)})
        return [[0.1] * 384 for _ in texts]
