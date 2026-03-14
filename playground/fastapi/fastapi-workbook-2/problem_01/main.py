"""
PROBLEM 01: SQLAlchemy Models & Database Setup
===============================================

LEARNING OBJECTIVES:
- Set up SQLAlchemy with FastAPI
- Define database models with relationships
- Create database tables
- Understand declarative_base and sessions

TASK:
Set up a database with User and Conversation models.

REQUIREMENTS:
- Create database.py with:
  - SQLAlchemy engine setup (SQLite for now)
  - SessionLocal factory
  - Base declarative class
  - get_db() dependency function

- Create models.py with:
  - User model:
    - id: Integer, primary key
    - email: String(255), unique, indexed
    - hashed_password: String
    - created_at: DateTime, default=now
  
  - Conversation model:
    - id: Integer, primary key
    - user_id: Integer, foreign key to User
    - title: String(255)
    - created_at: DateTime, default=now
    - user: relationship to User

- Create init_db() function to create all tables

- POST endpoint at "/users" to create a user
  - Input: {"email": str, "password": str}
  - Returns: {"id": int, "email": str, "created_at": str}

PRODUCTION NOTES:
- Never log passwords or hashed passwords
- Use connection pooling in production (SQLAlchemy does this by default)
- Always index foreign keys and frequently queried columns
- Use UTC for all timestamps
- Close database sessions properly (dependency handles this)

EXAMPLE:
POST /users {"email": "alice@example.com", "password": "temp123"}
→ {"id": 1, "email": "alice@example.com", "created_at": "2024-01-01T00:00:00"}

HINTS:
- from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
- from sqlalchemy.orm import sessionmaker, relationship, declarative_base
- Use datetime.utcnow for timestamps
- Don't hash passwords yet (that's Problem 12), just store as-is for now
"""

from fastapi import FastAPI, Depends
from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import Session, sessionmaker, relationship, declarative_base
from datetime import datetime
from pydantic import BaseModel

# Database setup
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

# TODO: Create engine
# Your code here

# TODO: Create SessionLocal class
# Your code here

# TODO: Create Base class
# Your code here

# Database models
# TODO: Create User model
# Your code here

# TODO: Create Conversation model
# Your code here

# Dependency
def get_db():
    """
    Database session dependency.
    Yields a session and ensures it's closed after use.
    """
    # TODO: Implement this
    # Hint: Use try/finally to ensure session closes
    pass

# Initialize database
def init_db():
    """Create all tables in the database."""
    # TODO: Implement this
    # Hint: Base.metadata.create_all(bind=engine)
    pass

# Pydantic schemas
class UserCreate(BaseModel):
    email: str
    password: str

class UserResponse(BaseModel):
    id: int
    email: str
    created_at: datetime
    
    class Config:
        from_attributes = True  # Allows conversion from ORM model

# FastAPI app
app = FastAPI()

# Create tables on startup
@app.on_event("startup")
def on_startup():
    init_db()

# TODO: Create POST endpoint at "/users"
# Use get_db dependency to get database session
# Create User instance, add to session, commit, refresh
# Return the user
# Your code here
