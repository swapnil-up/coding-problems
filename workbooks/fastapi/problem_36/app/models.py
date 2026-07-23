"""
Database models (SQLAlchemy ORM).
"""

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from datetime import datetime
from .database import Base

# TODO: Create User model
# Fields: id, email, hashed_password, created_at
class User(Base):
    pass  # Implement this

# TODO: Create Conversation model
# Fields: id, user_id (FK), title, created_at
# Relationship: user
class Conversation(Base):
    pass  # Implement this

# BONUS: Create Message model
# Fields: id, conversation_id (FK), content, role, created_at
# Relationship: conversation
