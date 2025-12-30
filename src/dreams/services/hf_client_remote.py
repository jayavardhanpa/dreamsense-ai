"""
Remote HuggingFace client wrapper.
"""

import logging
import requests

logger = logging.getLogger(__name__)

class RemoteHFClient:
    def __init__(self, hf_token: str, model: str, base_url: str):
        self.hf_token = hf_token
        self.model = model
        self.base_url = base_url

    def classify_emotion(self, text: str):
        """Classify emotion in text via remote API"""
        logger.debug(f"Classifying emotion for text: {text[:50]}...")
        headers = {"Authorization": f"Bearer {self.hf_token}"}
        response = requests.post(f"{self.base_url}/models/{self.model}", json={"inputs": text}, headers=headers)
        result = response.json()
        logger.debug(f"Emotion classification result: {result}")
        return result

    def embed(self, texts: list):
        """Get embeddings for texts via remote API"""
        logger.debug(f"Embedding {len(texts)} texts")
        headers = {"Authorization": f"Bearer {self.hf_token}"}
        response = requests.post(f"{self.base_url}/models/{self.model}", json={"inputs": texts}, headers=headers)
        result = response.json()
        logger.debug(f"Embedding result shape: {len(result) if isinstance(result, list) else 'unknown'}")
        return result