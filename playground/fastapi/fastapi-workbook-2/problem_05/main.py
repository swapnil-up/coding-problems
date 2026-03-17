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

class ConversationBatchRequest(BaseModel):
    user_id: int
    titles: List[str]

app = FastAPI()

@app.on_event("startup")
def on_startup():
    init_db()

@app.post("/conversations/with-message", response_model=ConversationWithMessageResponse, status_code=status.HTTP_201_CREATED)
def new_convo_msg(payload: ConversationWithMessageCreate, db: Session=Depends(get_db)):
    try:
        user = db.query(User).filter(User.id==payload.user_id).first()
        if user is None:
            raise HTTPException(status_code=404, detail="Conversation not found")

        convo = Conversation(user_id=payload.user_id, title=payload.title)
        db.add(convo)
        db.flush()

        msg = Message(conversation_id = convo.id, content= payload.first_message)
        db.add(msg)
        db.commit()
        db.refresh(convo)
        db.refresh(msg)
        return {"conversation": convo,"message": msg}
    except HTTPException:
        db.rollback()
        raise
    except Exception:
        db.rollback()
        raise HTTPException(status_code=400, detail="Transaction failed")

@app.delete("/users/{user_id}/cascade", response_model=CascadeDeleteResponse, status_code=200)
def delete_user_data(user_id: int, db: Session=Depends(get_db)):
    try:
        target = db.query(User).filter(User.id==user_id).first()
        if not target:
            raise HTTPException(status_code=404, detail="Not Found")
        convo_id = [c.id for c in db.query(Conversation).filter(Conversation.user_id==user_id).all()]
        msg_count = db.query(Message).filter(Message.conversation_id.in_(convo_id)).count()
        convo_count = len(convo_id)
        db.delete(target)
        db.commit()
        return {
            "deleted": {
                "user": 1,
                "conversations": convo_count,
                "messages": msg_count
            }
        }
    except HTTPException:
        db.rollback()
        raise
    except Exception:
        db.rollback()
        raise HTTPException(status_code=400, detail="Transaction failed")


@app.post("/messages/conversation", status_code=201)
def batch_msg(batch:BatchMessagesRequest, db:Session=Depends(get_db)):
    try:
        convo = db.query(Conversation).filter(Conversation.id == batch.conversation_id).first()
        if not convo:
            raise HTTPException(status_code=404, detail="Conversation not found")
        new_msg = []
        for msg in batch.messages:
            if msg.role not in ["user", "assistant"]:
                 raise HTTPException(status_code=422, detail="Invalid role")
            message=Message(
                conversation_id = batch.conversation_id,
                content=msg.content,
                role=msg.role
            )
            db.add(message)
            new_msg.append(message)
        db.commit()
        for m in new_msg: db.refresh(m)
        return new_msg
    except HTTPException:
        db.rollback()
        raise
    except Exception:
        db.rollback()
        raise HTTPException(status_code=400, detail="Transaction failed")

@app.post("/conversations/batch", status_code=201)
def batch_create_convos(payload: ConversationBatchRequest, db: Session = Depends(get_db)):
    try:
        user = db.query(User).filter(User.id == payload.user_id).first()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")

        new_convos = []
        for title in payload.titles:
            convo = Conversation(user_id=payload.user_id, title=title)
            db.add(convo)
            new_convos.append(convo)
        
        db.commit()
        for c in new_convos: db.refresh(c)
        return new_convos
    except HTTPException:
        db.rollback()
        raise
    except Exception:
        db.rollback()
        raise HTTPException(status_code=400, detail="Transaction failed")
    
