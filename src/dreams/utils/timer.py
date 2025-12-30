"""
Timer utility for dreamsense-ai.
"""

import logging
import time
from contextlib import contextmanager

logger = logging.getLogger(__name__)

@contextmanager
def timer():
    """Context manager for timing code blocks"""
    start = time.time()
    try:
        yield
    finally:
        end = time.time()
        elapsed = end - start
        logger.info(f"Elapsed time: {elapsed:.2f} seconds")