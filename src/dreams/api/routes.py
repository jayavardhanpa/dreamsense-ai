"""
FastAPI routes for dreamsense-ai.
"""

from fastapi import FastAPI, HTTPException
from dreams.models.dream_models import DreamData
from dreams.services.nlp_pipeline import NLPPipeline

app = FastAPI(title="DreamSense AI API")
nlp_pipeline = NLPPipeline()

@app.post("/analyze-dream")
async def analyze_dream(dream: DreamData):
    """Analyze a dream"""
    try:
        result = nlp_pipeline.process_dream(dream.text)
        return {"analysis": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))