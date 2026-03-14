"""
PROBLEM 03: Messages with Pagination
=====================================

LEARNING OBJECTIVES:
- Add a Message model with multiple foreign keys
- Implement pagination for large datasets
- Use limit/offset pattern
- Understand N+1 query problems

TASK:
Create a Message model and implement paginated message listing.

REQUIREMENTS:
- Add Message model:
  - id: Integer, primary key
  - conversation_id: Integer, foreign key to Conversation
  - content: Text (can be long)
  - role: String (either "user" or "assistant")
  - created_at: DateTime, default=now
  - conversation: relationship to Conversation

- POST /messages
  - Body: {"conversation_id": int, "content": str, "role": str}
  - Creates a message
  - Returns: {"id": int, "conversation_id": int, "content": str, "role": str, "created_at": str}
  - Status: 201

- GET /conversations/{conversation_id}/messages
  - Query params:
    - limit: int (default=50, max=100)
    - offset: int (default=0)
  - Returns messages for a conversation, paginated
  - Ordered by created_at ASC (oldest first)
  - Returns: {
      "messages": [...],
      "total": int,
      "limit": int,
      "offset": int
    }

PRODUCTION NOTES:
- **Pagination is critical**: Chat histories can have 1000s of messages
- **Index conversation_id**: This will be queried constantly
- **N+1 queries**: Be aware when loading relationships (use joinedload if needed)
- **Message size limits**: Consider max content length (e.g., 10,000 chars)
- **Ordering**: Consistent ordering (by created_at) is important for UX
- **Cursor pagination**: For very large datasets, consider cursor-based pagination
- **Database choice**: For full-text search on messages, consider PostgreSQL

EXAMPLE:
POST /messages
{"conversation_id": 1, "content": "Hello!", "role": "user"}
→ 201 {"id": 1, "conversation_id": 1, "content": "Hello!", "role": "user", "created_at": "..."}

GET /conversations/1/messages?limit=10&offset=0
→ {
    "messages": [{...}, {...}, ...],
    "total": 25,
    "limit": 10,
    "offset": 0
  }

HINTS:
- Use Column(Text) for long content
- Use .limit() and .offset() on queries
- Use .count() to get total
- Validate role is either "user" or "assistant"
"""

from fastapi import FastAPI, Depends, HTTPException, status, Query
from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey, Text
from sqlalchemy.orm import Session, sessionmaker, relationship, declarative_base
from datetime import datetime
from pydantic import BaseModel, Field
from typing import List

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Models
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

# TODO: Create Message model
# Your code here

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def init_db():
    Base.metadata.create_all(bind=engine)

# Pydantic schemas
class MessageCreate(BaseModel):
    conversation_id: int
    content: str = Field(..., max_length=10000)
    role: str = Field(..., pattern="^(user|assistant)$")

class MessageResponse(BaseModel):
    id: int
    conversation_id: int
    content: str
    role: str
    created_at: datetime
    
    class Config:
        from_attributes = True

class MessageListResponse(BaseModel):
    messages: List[MessageResponse]
    total: int
    limit: int
    offset: int

app = FastAPI()

@app.on_event("startup")
def on_startup():
    init_db()

# TODO: Implement POST /messages (status_code=201)
# Validate that role is either "user" or "assistant"
# Your code here

# TODO: Implement GET /conversations/{conversation_id}/messages
# With pagination (limit, offset)
# Return total count, messages, limit, offset
# Order by created_at ASC
# Your code here
