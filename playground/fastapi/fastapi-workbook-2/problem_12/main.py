"""
PROBLEM 12: Password Hashing & Secure Registration
===================================================

LEARNING OBJECTIVES:
- Hash passwords securely with bcrypt
- Never store plain text passwords
- Validate password strength
- Handle duplicate email registration

TASK:
Implement secure user registration with password hashing.

REQUIREMENTS:
- Install passlib[bcrypt]
- Create password hashing utilities:
  - hash_password(password: str) -> str
  - verify_password(plain_password: str, hashed: str) -> bool

- POST /auth/register
  - Body: {"email": str, "password": str}
  - Validates password (min 8 chars, has uppercase, lowercase, digit)
  - Hashes password before storing
  - Returns: {"id": int, "email": str, "created_at": str}
  - Status: 201
  - Returns 400 if email already exists
  - Returns 422 if password too weak

- POST /auth/verify (for testing)
  - Body: {"email": str, "password": str}
  - Checks if password matches stored hash
  - Returns: {"valid": bool}

PRODUCTION NOTES:
- **NEVER log passwords**: Not in plain text, not hashed, never
- **Password policies**: Enforce min length, complexity
- **Rate limiting**: Prevent brute force attacks on registration
- **Email verification**: In production, verify email before activation
- **Password reset**: Always required in production
- **Bcrypt work factor**: Balance security vs performance (12-14 rounds typical)
- **Timing attacks**: Use constant-time comparison for password verification
- **Account enumeration**: Don't reveal if email exists (same error for wrong email/password)

PASSWORD SECURITY CHECKLIST:
✓ Use bcrypt (or argon2)
✓ Never store plain text
✓ Enforce minimum complexity
✓ Use random salt (bcrypt does this automatically)
✓ Don't log passwords
✓ Use HTTPS in production
✓ Implement rate limiting

EXAMPLE:
POST /auth/register
{"email": "alice@example.com", "password": "SecurePass123"}
→ 201 {"id": 1, "email": "alice@example.com", "created_at": "..."}

POST /auth/verify
{"email": "alice@example.com", "password": "SecurePass123"}
→ {"valid": true}

HINTS:
- from passlib.context import CryptContext
- pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
- Use pwd_context.hash() and pwd_context.verify()
- Check email uniqueness before attempting to create user
"""

from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import Session, sessionmaker, declarative_base
from datetime import datetime
from pydantic import BaseModel, EmailStr, Field
from passlib.context import CryptContext
import re

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Password hashing context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Models
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

# TODO: Implement password hashing utilities
def hash_password(password: str) -> str:
    """Hash a password using bcrypt."""
    # Your code here
    pass

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify a password against its hash."""
    # Your code here
    pass

def validate_password_strength(password: str) -> bool:
    """
    Validate password meets security requirements.
    
    Requirements:
    - At least 8 characters
    - Contains uppercase letter
    - Contains lowercase letter
    - Contains digit
    
    Returns True if valid, False otherwise.
    """
    # Your code here
    # Hint: Use len() and regex or any()/all() with char methods
    pass

# Pydantic schemas
class UserRegister(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=8)

class UserResponse(BaseModel):
    id: int
    email: str
    created_at: datetime
    
    class Config:
        from_attributes = True

class PasswordVerifyRequest(BaseModel):
    email: EmailStr
    password: str

class PasswordVerifyResponse(BaseModel):
    valid: bool

app = FastAPI()

@app.on_event("startup")
def on_startup():
    init_db()

# TODO: Implement POST /auth/register
# 1. Validate password strength
# 2. Check if email already exists
# 3. Hash password
# 4. Create user with hashed password
# 5. Return user (without password!)
# Your code here

# TODO: Implement POST /auth/verify (for testing password verification)
# 1. Find user by email
# 2. Verify password against hash
# 3. Return {"valid": True/False}
# Your code here
