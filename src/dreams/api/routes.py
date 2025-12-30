"""
FastAPI routes for dreamsense-ai.
"""

import logging
from fastapi import FastAPI, HTTPException
from dreams.models.dream_models import DreamData
from dreams.services.nlp_pipeline import NLPPipeline

logger = logging.getLogger(__name__)

app = FastAPI(title="DreamSense AI API")
nlp_pipeline = NLPPipeline()

@app.post("/analyze-dream")
async def analyze_dream(dream: DreamData):
    """Analyze a dream"""
    try:
        logger.info(f"Analyzing dream: {dream.text[:50]}...")
        result = nlp_pipeline.process_dream(dream.text)
        logger.info("Dream analysis completed successfully")
        return {"analysis": result}
    except Exception as e:
        logger.error(f"Error analyzing dream: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))