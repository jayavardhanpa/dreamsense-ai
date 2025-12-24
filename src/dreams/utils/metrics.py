"""
Metrics utility for dreamsense-ai.
"""

from typing import Dict, List
import numpy as np

class Metrics:
    @staticmethod
    def accuracy(predictions: List, labels: List) -> float:
        """Calculate accuracy"""
        return np.mean([p == l for p, l in zip(predictions, labels)])

    @staticmethod
    def precision(predictions: List, labels: List) -> float:
        """Calculate precision"""
        tp = sum(1 for p, l in zip(predictions, labels) if p == 1 and l == 1)
        fp = sum(1 for p, l in zip(predictions, labels) if p == 1 and l == 0)
        return tp / (tp + fp) if (tp + fp) > 0 else 0