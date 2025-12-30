"""
Pydantic models for dreamsense-ai.
"""

import logging
from pydantic import BaseModel
from typing import List, Optional, Dict
from datetime import datetime

logger = logging.getLogger(__name__)

class DreamData(BaseModel):
    text: str
    timestamp: datetime
    physiological_data: Optional[Dict[str, float]] = None

class DreamAnalysis(BaseModel):
    dream_id: str
    emotions: List[str]
    themes: List[str]
    embedding: List[float]

class DreamState(BaseModel):
    is_dreaming: bool
    confidence: float
    features: Dict[str, float]