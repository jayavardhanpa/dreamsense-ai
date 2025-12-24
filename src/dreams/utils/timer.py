"""
Timer utility for dreamsense-ai.
"""

import time
from contextlib import contextmanager

@contextmanager
def timer():
    """Context manager for timing code blocks"""
    start = time.time()
    try:
        yield
    finally:
        end = time.time()
        print(f"Elapsed time: {end - start:.2f} seconds")