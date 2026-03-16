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
from sqlalchemy.pool import StaticPool
from sqlalchemy.orm import Session, sessionmaker, relationship, declarative_base
from datetime import datetime
from pydantic import BaseModel
import os

# Database setup
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "test.db")

SQLALCHEMY_DATABASE_URL = f"sqlite:///{db_path}"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread" : False},
    poolclass=StaticPool,
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class User(Base):
    __tablename__="users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, nullable=False, index=True)
    hashed_password = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.now)
    
    conversations = relationship("Conversation", back_populates="user")

class Conversation(Base): 
    __tablename__= "conversations"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    title = Column(String(255))
    created_at = Column(DateTime, default=datetime.now)
    user = relationship("User", back_populates="conversations")

def get_db():
    """
    Database session dependency.
    Yields a session and ensures it's closed after use.
    """
    db = SessionLocal()
    try: 
        yield db
    finally:
        db.close()

# Initialize database
def init_db():
    """Create all tables in the database."""
    Base.metadata.create_all(bind=engine)

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

@app.post("/users", response_model=UserResponse)
def create_user(user_data: UserCreate, db: Session = Depends(get_db)):
    new_user = User(
        email = user_data.email, 
        hashed_password = user_data.password
    )
    db.add(new_user)
    db.commit()
    

    db.refresh(new_user)
    return new_user