"""
Top-level application factory for dreamsense-ai.
"""

from dreams.config import config
from dreams.logging_config import setup_logging

def create_app():
    """Create and configure the application"""
    setup_logging()

    # Here you would initialize your app, e.g., FastAPI, Flask, etc.
    # For now, return a simple object
    class App:
        def run(self):
            print("DreamSense AI is running...")

    return App()