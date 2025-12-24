"""
Logging configuration for dreamsense-ai.
"""

import logging
import sys
from pathlib import Path
from dreams.config import config

def setup_logging(cfg=None):
    """Setup centralized logging"""
    if cfg is None:
        from dreams.config import config as global_config
        cfg = global_config._config
    log_level = getattr(logging, cfg.get('logging.level', 'INFO'))
    log_file = cfg.get('logging.file', 'logs/app.log')

    # Create logs directory if it doesn't exist
    Path(log_file).parent.mkdir(exist_ok=True)

    logging.basicConfig(
        level=log_level,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler(sys.stdout)
        ]
    )

    logger = logging.getLogger(__name__)
    logger.info("Logging configured")