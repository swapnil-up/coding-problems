"""
PROBLEM 05: Transactions and Error Handling
============================================

LEARNING OBJECTIVES:
- Use database transactions correctly
- Implement rollback on errors
- Ensure atomic operations
- Handle database exceptions

TASK:
Create endpoints that demonstrate proper transaction handling.

REQUIREMENTS:

1. POST /conversations/with-message
   - Body: {"user_id": int, "title": str, "first_message": str}
   - Creates BOTH conversation AND first message in single transaction
   - If either fails, BOTH should be rolled back
   - Returns: {"conversation": {...}, "message": {...}}
   - Status: 201

2. DELETE /users/{user_id}/cascade
   - Deletes user AND all their conversations AND messages
   - Must be atomic (all or nothing)
   - Returns: {"deleted": {"user": int, "conversations": int, "messages": int}}
   - Status: 200

3. POST /messages/batch
   - Body: {"conversation_id": int, "messages": [{"content": str, "role": str}, ...]}
   - Creates multiple messages in single transaction
   - If ANY message fails validation, NONE are created
   - Returns: {"created": int, "messages": [...]}

TRANSACTION RULES:
- Use db.commit() only when ALL operations succeed
- Use db.rollback() on any error
- Use try/except/finally blocks
- Ensure session is always cleaned up

PRODUCTION NOTES:
- **ACID properties**: Understand Atomicity, Consistency, Isolation, Durability
- **Isolation levels**: Default is usually fine, but know when to adjust
- **Deadlocks**: Can happen with concurrent transactions; implement retry logic
- **Long transactions**: Keep transactions short to avoid locking
- **Read-only transactions**: Use for reporting to avoid locks
- **Savepoints**: For complex transactions with partial rollback
- **Two-phase commit**: For distributed transactions across databases
- **Connection pools**: Ensure transactions don't exhaust pool

TRANSACTION BEST PRACTICES:
1. Keep transactions as short as possible
2. Don't do I/O inside transactions (API calls, file operations)
3. Handle all exceptions properly
4. Always clean up (commit or rollback)
5. Use context managers when possible
6. Test rollback scenarios
7. Monitor for long-running transactions

EXAMPLE:
POST /conversations/with-message
{
  "user_id": 1,
  "title": "New Chat",
  "first_message": "Hello!"
}

Success case:
→ 201 {
    "conversation": {"id": 1, "title": "New Chat", ...},
    "message": {"id": 1, "content": "Hello!", ...}
  }

Error case (invalid user_id):
→ 404 Error, and NO conversation or message created

HINTS:
- Wrap multiple db operations in try/except
- Use db.rollback() in except block
- Use db.commit() only after all operations succeed
- Check foreign keys exist before creating records
"""

from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey, Text
from sqlalchemy.orm import Session, sessionmaker, relationship, declarative_base
from sqlalchemy.exc import SQLAlchemyError
from datetime import datetime
from pydantic import BaseModel
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
    messages = relationship("Message", back_populates="conversation", cascade="all, delete-orphan")

class Message(Base):
    __tablename__ = "messages"
    id = Column(Integer, primary_key=True, index=True)
    conversation_id = Column(Integer, ForeignKey("conversations.id"), index=True)
    content = Column(Text)
    role = Column(String(20))
    created_at = Column(DateTime, default=datetime.utcnow)
    conversation = relationship("Conversation", back_populates="messages")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def init_db():
    Base.metadata.create_all(bind=engine)

# Pydantic schemas
class ConversationWithMessageCreate(BaseModel):
    user_id: int
    title: str
    first_message: str

class MessageResponse(BaseModel):
    id: int
    conversation_id: int
    content: str
    role: str
    created_at: datetime
    
    class Config:
        from_attributes = True

class ConversationResponse(BaseModel):
    id: int
    user_id: int
    title: str
    created_at: datetime
    
    class Config:
        from_attributes = True

class ConversationWithMessageResponse(BaseModel):
    conversation: ConversationResponse
    message: MessageResponse

class BatchMessageCreate(BaseModel):
    content: str
    role: str

class BatchMessagesRequest(BaseModel):
    conversation_id: int
    messages: List[BatchMessageCreate]

class BatchMessagesResponse(BaseModel):
    created: int
    messages: List[MessageResponse]

class CascadeDeleteResponse(BaseModel):
    deleted: dict

app = FastAPI()

@app.on_event("startup")
def on_startup():
    init_db()

# TODO: Implement POST /conversations/with-message
# Use transaction to create both conversation and message
# Rollback if either fails
# Your code here

# TODO: Implement DELETE /users/{user_id}/cascade
# Delete user and all related data atomically
# Your code here

# TODO: Implement POST /messages/batch
# Create multiple messages in single transaction
# All or nothing - if any fails, rollback all
# Your code here
