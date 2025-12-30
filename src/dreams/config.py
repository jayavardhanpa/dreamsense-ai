"""
Configuration loader for dreamsense-ai.
"""

import os
import logging
from pathlib import Path
from typing import Dict, Any

logger = logging.getLogger(__name__)

class Config:
    def __init__(self, env: str = "dev"):
        self.env = env
        self._config = {}
        self.load_config()

    def load_config(self):
        """Load configuration from properties file"""
        config_file = Path(__file__).parent.parent.parent / "config" / f"{self.env}.properties"
        if config_file.exists():
            with open(config_file, 'r') as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith('#'):
                        key, value = line.split('=', 1)
                        self._config[key.strip()] = value.strip()
            logger.info(f"Loaded configuration from {config_file}")
        else:
            logger.warning(f"Configuration file {config_file} not found")

        # Override with environment variables
        for key, value in os.environ.items():
            self._config[key.lower()] = value
        logger.info("Configuration loaded and overridden with environment variables")

    def get(self, key: str, default: Any = None) -> Any:
        return self._config.get(key.lower(), default)

    def __getitem__(self, key: str) -> Any:
        return self._config[key.lower()]

def load_properties(config_path: str) -> Dict[str, str]:
    """Load properties from a file path"""
    props = {}
    with open(config_path, 'r') as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#'):
                key, value = line.split('=', 1)
                props[key.strip()] = value.strip()

    # Override with environment variables
    for key, value in os.environ.items():
        props[key] = value

    return props

def get_config_for_env(env: str) -> Dict[str, str]:
    """Get configuration for a specific environment"""
    config_file = Path.cwd() / "config" / f"{env}.properties"
    return load_properties(str(config_file))

config = Config()