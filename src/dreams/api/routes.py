"""
FastAPI routes for dreamsense-ai.
"""

import logging
import time
from fastapi import FastAPI, HTTPException, Request, Response
from dreams.models.dream_models import DreamData
from dreams.services.nlp_pipeline import NLPPipeline
from dreams.logging_config import setup_logging

setup_logging()

logger = logging.getLogger(__name__)

app = FastAPI(title="DreamSense AI API")
nlp_pipeline = NLPPipeline()

@app.middleware("http")
async def log_requests(request: Request, call_next):
    start_time = time.time()
    logger.info(f"Request: {request.method} {request.url}")
    response = await call_next(request)
    process_time = time.time() - start_time
    logger.info(f"Response: {response.status_code} - {process_time:.4f}s")
    return response

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