import logging
from dreams.logging_config import setup_logging

def test_setup_logging(caplog):
    setup_logging()
    logger = logging.getLogger("dreams")
    logger.info("Test message")
    assert "Test message" in caplog.text