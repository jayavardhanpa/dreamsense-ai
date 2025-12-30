"""
NLP pipeline orchestrator.
"""

import logging
from dreams.services.hf_client import HFClient
from dreams.services.embedding_service import EmbeddingService
import csv

logger = logging.getLogger(__name__)

class NLPPipeline:
    def __init__(self):
        self.hf_client = HFClient()
        self.embedding_service = EmbeddingService()

    def process_dream(self, dream_text: str):
        """Process dream text through NLP pipeline"""
        logger.info("Processing dream text through NLP pipeline")
        # Sentiment analysis
        sentiment = self.hf_client.analyze_text(dream_text)

        # Embedding
        embedding = self.embedding_service.get_embedding(dream_text)

        logger.info("NLP pipeline processing completed")
        return {
            "sentiment": sentiment,
            "embedding": embedding
        }

def process_text(text: str, hf_client):
    emotion_result = hf_client.classify_emotion(text)

    emotion = None
    if emotion_result and isinstance(emotion_result, list):
        emotion = emotion_result[0].get("label")

    embeddings = hf_client.embed([text])

    embedding = None
    if embeddings and len(embeddings) == 1:
        embedding = embeddings[0]

    return {
        "clean_text": text.strip(),
        "emotion": emotion,
        "embedding": embedding
    }


def process(input_file: str, output_file: str, hf_client, cfg):
    """Process dream data from CSV"""
    import csv
    with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
        reader = csv.DictReader(infile)
        writer = csv.writer(outfile)
        writer.writerow(['dream_text', 'emotion', 'sensory_modes', 'embedding'])
        for row in reader:
            result = process_text(row['dream_text'], hf_client)
            writer.writerow([
                row['dream_text'],
                result['emotion'],
                ','.join(result['sensory_modes']),
                ','.join(map(str, result['embedding']))
            ])

def process_csv(input_path: str, output_path: str, hf_client):
    logger.info(f"Starting CSV processing: {input_path} -> {output_path}")
    results = []

    with open(input_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        if "dream_text" not in reader.fieldnames:
            raise ValueError("Input CSV must contain 'dream_text' column")

        for row in reader:
            text = row["dream_text"]
            logger.debug(f"Processing text: {text[:50]}...")
            features = process_text(text, hf_client)
            results.append({
                "dream_text": text,
                **features
            })

    # write output
    with open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=results[0].keys()
        )
        writer.writeheader()
        writer.writerows(results)
    logger.info(f"CSV processing completed. Processed {len(results)} rows.")