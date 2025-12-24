"""
Pytest configuration and fixtures for dreamsense-ai.
"""

import pytest
import tempfile
import os
from pathlib import Path

@pytest.fixture
def sample_config():
    """Create a temporary config file for testing"""
    config_content = """# Test configuration
ENV=dev
LOG_LEVEL=DEBUG
HF_MODEL=test-model
DATABASE_URL=sqlite:///test.db
"""
    with tempfile.NamedTemporaryFile(mode='w', suffix='.properties', delete=False) as f:
        f.write(config_content)
        config_path = f.name

    yield config_path

    # Cleanup
    os.unlink(config_path)

@pytest.fixture
def sample_dream_text():
    """Sample dream text for testing"""
    return "I was flying over a city and felt free."