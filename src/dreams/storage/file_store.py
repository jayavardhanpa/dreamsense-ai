"""
File storage for dreamsense-ai.
"""

import logging
import csv
import json
from pathlib import Path
from typing import List, Dict
from dreams.models.dream_models import DreamData

logger = logging.getLogger(__name__)

class FileStore:
    def __init__(self, data_path: str = "./data"):
        self.data_path = Path(data_path)
        self.data_path.mkdir(exist_ok=True)

    def save_dream(self, dream: DreamData):
        """Save dream data to CSV"""
        file_path = self.data_path / "dreams.csv"
        logger.debug(f"Saving dream to {file_path}")
        with open(file_path, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([
                dream.timestamp.isoformat(),
                dream.text,
                json.dumps(dream.physiological_data or {})
            ])
        logger.info("Dream saved successfully")

    def load_dreams(self) -> List[DreamData]:
        """Load dreams from CSV"""
        dreams = []
        file_path = self.data_path / "dreams.csv"
        if file_path.exists():
            logger.debug(f"Loading dreams from {file_path}")
            with open(file_path, 'r') as f:
                reader = csv.reader(f)
                for row in reader:
                    dreams.append(DreamData(
                        timestamp=row[0],
                        text=row[1],
                        physiological_data=json.loads(row[2])
                    ))
            logger.info(f"Loaded {len(dreams)} dreams")
        else:
            logger.warning(f"Dreams file {file_path} does not exist")
        return dreams