"""
Metrics utility for dreamsense-ai.
"""

import logging
from typing import Dict, List
import numpy as np

logger = logging.getLogger(__name__)

class Metrics:
    @staticmethod
    def accuracy(predictions: List, labels: List) -> float:
        """Calculate accuracy"""
        acc = np.mean([p == l for p, l in zip(predictions, labels)])
        logger.debug(f"Calculated accuracy: {acc}")
        return acc

    @staticmethod
    def precision(predictions: List, labels: List) -> float:
        """Calculate precision"""
        tp = sum(1 for p, l in zip(predictions, labels) if p == 1 and l == 1)
        fp = sum(1 for p, l in zip(predictions, labels) if p == 1 and l == 0)
        prec = tp / (tp + fp) if (tp + fp) > 0 else 0
        logger.debug(f"Calculated precision: {prec}")
        return prec