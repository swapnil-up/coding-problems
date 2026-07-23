"""
Database configuration and setup.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# TODO: Create database URL (use sqlite for now)
SQLALCHEMY_DATABASE_URL = "sqlite:///./chatbot.db"

# TODO: Create engine with appropriate settings
# For SQLite, use connect_args={"check_same_thread": False}
engine = None  # Replace with actual engine

# TODO: Create SessionLocal class for database sessions
SessionLocal = None  # Replace with sessionmaker(...)

# TODO: Create Base class for declarative models
Base = None  # Replace with declarative_base()
