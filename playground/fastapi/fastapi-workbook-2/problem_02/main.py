"""
PROBLEM 02: Conversation CRUD Operations
=========================================

LEARNING OBJECTIVES:
- Implement Create, Read, Update, Delete operations
- Use database sessions correctly
- Handle foreign key relationships
- Return appropriate HTTP status codes

TASK:
Build CRUD endpoints for conversations.

REQUIREMENTS:
- Copy your database setup and models from Problem 01
- Create the following endpoints:

  POST /conversations
  - Body: {"user_id": int, "title": str}
  - Creates a new conversation
  - Returns: {"id": int, "user_id": int, "title": str, "created_at": str}
  - Status: 201

  GET /conversations
  - Query param: user_id (optional, filters by user)
  - Returns list of conversations
  - Returns: [{"id": int, "user_id": int, "title": str, "created_at": str}, ...]

  GET /conversations/{conversation_id}
  - Returns single conversation
  - Returns 404 if not found

  PUT /conversations/{conversation_id}
  - Body: {"title": str}
  - Updates conversation title
  - Returns updated conversation
  - Returns 404 if not found

  DELETE /conversations/{conversation_id}
  - Deletes conversation
  - Returns 204 No Content
  - Returns 404 if not found

PRODUCTION NOTES:
- **Authorization**: In production, verify user owns the conversation before update/delete
- **Soft Deletes**: Consider soft deletes (deleted_at field) instead of hard deletes
- **Cascading**: When user is deleted, what happens to conversations? Define this explicitly
- **Validation**: Check that user_id exists before creating conversation
- **Idempotency**: DELETE should return 204 even if resource already deleted (idempotent)

EXAMPLE:
POST /conversations {"user_id": 1, "title": "My Chat"}
→ 201 {"id": 1, "user_id": 1, "title": "My Chat", "created_at": "..."}

GET /conversations?user_id=1
→ [{"id": 1, "user_id": 1, "title": "My Chat", "created_at": "..."}, ...]

HINTS:
- Use db.query(Model).filter(...).first() for single records
- Use db.query(Model).filter(...).all() for multiple records
- Use db.add(), db.commit(), db.refresh() for creation
- Use db.delete() for deletion
- Raise HTTPException(status_code=404) when not found
"""

from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import Session, sessionmaker, relationship, declarative_base
from datetime import datetime
from pydantic import BaseModel
from typing import List, Optional

# Database setup (same as Problem 01)
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Models (same as Problem 01)
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True)
    hashed_password = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

class Conversation(Base):
    __tablename__ = "conversations"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), index=True)
    title = Column(String(255))
    created_at = Column(DateTime, default=datetime.utcnow)
    user = relationship("User")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def init_db():
    Base.metadata.create_all(bind=engine)

# Pydantic schemas
class ConversationCreate(BaseModel):
    user_id: int
    title: str

class ConversationUpdate(BaseModel):
    title: str

class ConversationResponse(BaseModel):
    id: int
    user_id: int
    title: str
    created_at: datetime
    
    class Config:
        from_attributes = True

# FastAPI app
app = FastAPI()

@app.on_event("startup")
def on_startup():
    init_db()

# TODO: Implement POST /conversations (status_code=201)
# Your code here

# TODO: Implement GET /conversations with optional user_id filter
# Your code here

# TODO: Implement GET /conversations/{conversation_id}
# Raise 404 if not found
# Your code here

# TODO: Implement PUT /conversations/{conversation_id}
# Raise 404 if not found
# Your code here

# TODO: Implement DELETE /conversations/{conversation_id} (status_code=204)
# Raise 404 if not found
# Your code here
