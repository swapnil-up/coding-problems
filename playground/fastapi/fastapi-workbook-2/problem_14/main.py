"""
PROBLEM 14: Protected Endpoints with JWT Validation
====================================================

LEARNING OBJECTIVES:
- Validate JWT tokens
- Create authentication dependency
- Protect endpoints with authentication
- Extract user from token

TASK:
Implement JWT validation and protected endpoints.

REQUIREMENTS:
- Create get_current_user dependency:
  - Extracts token from Authorization header
  - Validates token signature and expiration
  - Returns user email from token
  - Raises 401 if token invalid/expired

- GET /protected/me
  - Protected endpoint requiring valid token
  - Returns current user info
  - Returns: {"email": str, "user_id": int}

- GET /protected/conversations
  - Returns conversations for authenticated user only
  - Requires valid token
  - Filters by current user

PRODUCTION NOTES:
- **Token validation**: Always verify signature and expiration
- **Error handling**: Clear messages for expired vs invalid tokens
- **Performance**: Cache user lookups from tokens
- **Token blacklist**: For logout, maintain revoked tokens list
- **Refresh tokens**: Implement separate refresh flow (Problem 15)
- **Scope/permissions**: Add role-based access control
- **Rate limiting**: Per-user rate limits using token claims

AUTHENTICATION FLOW:
1. Client sends: Authorization: Bearer <token>
2. Server extracts and validates token
3. Server loads user from token claims
4. Endpoint executes with authenticated user

TOKEN ERRORS:
- Missing token → 401 "Not authenticated"
- Invalid signature → 401 "Invalid token"
- Expired token → 401 "Token expired"
- Malformed token → 401 "Invalid token"

EXAMPLE:
GET /protected/me
Headers: Authorization: Bearer eyJhbGc...

→ {
    "email": "alice@example.com",
    "user_id": 1
  }

HINTS:
- from fastapi import Depends, Header
- from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
- jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
- Use HTTPBearer for automatic token extraction
- Catch JWTError for invalid tokens
"""

from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import Session, sessionmaker, declarative_base
from datetime import datetime
from pydantic import BaseModel
from jose import JWTError, jwt
from typing import List

SECRET_KEY = "your-secret-key-change-in-production"
ALGORITHM = "HS256"

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

security = HTTPBearer()

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

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def init_db():
    Base.metadata.create_all(bind=engine)

class UserResponse(BaseModel):
    email: str
    user_id: int

class ConversationResponse(BaseModel):
    id: int
    user_id: int
    title: str
    created_at: datetime
    class Config:
        from_attributes = True

async def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_db)
) -> User:
    """
    Dependency to get current authenticated user from JWT.
    
    Args:
        credentials: JWT token from Authorization header
        db: Database session
        
    Returns:
        User object
        
    Raises:
        HTTPException 401 if token invalid or user not found
    """
    # TODO: Implement JWT validation
    # 1. Extract token from credentials
    # 2. Decode and validate token
    # 3. Extract email from "sub" claim
    # 4. Load user from database
    # 5. Raise 401 if any step fails
    # Your code here
    pass

app = FastAPI()

@app.on_event("startup")
def on_startup():
    init_db()

# TODO: Implement GET /protected/me
# Use get_current_user dependency
# Return user email and ID
# Your code here

# TODO: Implement GET /protected/conversations
# Use get_current_user dependency
# Return only conversations belonging to current user
# Your code here
