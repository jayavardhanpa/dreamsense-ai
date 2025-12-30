"""
Database connection and migrations for dreamsense-ai.
"""

import logging
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dreams.config import config

logger = logging.getLogger(__name__)

Base = declarative_base()

class Dream(Base):
    __tablename__ = 'dreams'
    id = Column(Integer, primary_key=True)
    text = Column(Text)
    timestamp = Column(DateTime)
    physiological_data = Column(Text)  # JSON string

class Database:
    def __init__(self):
        db_url = config.get('database.url', 'sqlite:///dreamsense.db')
        logger.info(f"Initializing database with URL: {db_url}")
        self.engine = create_engine(db_url)
        Base.metadata.create_all(self.engine)
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
        logger.info("Database initialized successfully")

    def get_session(self):
        return self.SessionLocal()

db = Database()