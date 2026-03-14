"""
PROBLEM 13: JWT Login and Token Generation
===========================================

LEARNING OBJECTIVES:
- Generate JWT access tokens
- Implement login endpoint
- Set token expiration
- Understand JWT structure

TASK:
Build login endpoint that returns JWT tokens.

REQUIREMENTS:
- Install: python-jose[cryptography]

- POST /auth/login
  - Body: {"email": str, "password": str}
  - Verifies user exists and password matches
  - Generates JWT access token
  - Returns: {"access_token": str, "token_type": "bearer"}
  - Token expires in 30 minutes
  - Token contains: {"sub": email, "exp": expiration}

- Use from Problem 12:
  - Password verification with bcrypt
  - User model from database

PRODUCTION NOTES:
- **Secret key**: Use strong random secret, never commit to git
- **Environment variables**: Load secret from env
- **Token expiration**: Short for access tokens (15-30 min)
- **HTTPS only**: Never send tokens over HTTP
- **Secure storage**: Client should store in httpOnly cookies or secure storage
- **Token rotation**: Implement refresh tokens (Problem 15)
- **Revocation**: Need mechanism to revoke tokens (blacklist)
- **Claims**: Add user_id, roles, permissions to token
- **Algorithm**: Use RS256 for production (asymmetric)

JWT STRUCTURE:
- Header: {"alg": "HS256", "typ": "JWT"}
- Payload: {"sub": "user@example.com", "exp": 1234567890}
- Signature: HMACSHA256(base64(header) + "." + base64(payload), secret)

TOKEN LIFETIME:
- Access token: 30 minutes
- Refresh token: 7 days (Problem 15)

EXAMPLE:
POST /auth/login
{"email": "alice@example.com", "password": "SecurePass123"}

→ {
    "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
    "token_type": "bearer"
  }

HINTS:
- from jose import jwt
- from datetime import datetime, timedelta
- jwt.encode(claims, SECRET_KEY, algorithm="HS256")
- Set exp claim: datetime.utcnow() + timedelta(minutes=30)
"""

from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import Session, sessionmaker, declarative_base
from datetime import datetime, timedelta
from pydantic import BaseModel, EmailStr
from passlib.context import CryptContext
from jose import jwt
import os

# Configuration
SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key-change-in-production")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True)
    hashed_password = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def init_db():
    Base.metadata.create_all(bind=engine)

class LoginRequest(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify password against hash."""
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(data: dict, expires_delta: timedelta = None) -> str:
    """
    Create JWT access token.
    
    Args:
        data: Claims to encode in token
        expires_delta: Token lifetime (default: 30 minutes)
        
    Returns:
        Encoded JWT token
    """
    # TODO: Implement token creation
    # 1. Copy data to avoid modifying original
    # 2. Set expiration time
    # 3. Encode with JWT
    # 4. Return token string
    # Your code here
    pass

app = FastAPI()

@app.on_event("startup")
def on_startup():
    init_db()

# TODO: Implement POST /auth/login
# 1. Find user by email
# 2. Verify password
# 3. Generate access token with user email in "sub" claim
# 4. Return token response
# Raise 401 if credentials invalid
# Your code here
