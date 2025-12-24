from abc import ABC, abstractmethod
from typing import List, Any


class HFClient(ABC):

    @abstractmethod
    def classify_emotion(self, text: str) -> Any:
        pass

    @abstractmethod
    def embed(self, texts: List[str]) -> Any:
        pass
