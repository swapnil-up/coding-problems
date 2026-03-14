"""
PROBLEM 15: Refresh Tokens and Token Rotation
==============================================

LEARNING OBJECTIVES:
- Implement refresh token flow
- Rotate tokens for security
- Store refresh tokens in database
- Handle token expiration gracefully

TASK:
Add refresh token functionality for long-lived sessions.

REQUIREMENTS:
- Add RefreshToken model:
  - id: Integer, primary key
  - token: String, unique, indexed
  - user_id: Integer, foreign key
  - expires_at: DateTime
  - created_at: DateTime
  - revoked: Boolean (default False)

- Modify login to return both tokens:
  POST /auth/login
  Returns: {
    "access_token": str (30 min),
    "refresh_token": str (7 days),
    "token_type": "bearer"
  }

- POST /auth/refresh
  - Body: {"refresh_token": str}
  - Validates refresh token
  - Generates new access token
  - Optionally rotates refresh token
  - Returns: {"access_token": str, "refresh_token": str}

- POST /auth/logout
  - Requires authentication
  - Revokes all refresh tokens for user
  - Returns: {"message": "Logged out successfully"}

PRODUCTION NOTES:
- **Token rotation**: Generate new refresh token on each use
- **Revocation**: Track revoked tokens in database
- **Cleanup**: Delete expired tokens regularly (cron job)
- **Security**: Refresh tokens are high-value targets
- **Storage**: Server-side storage only, never in localStorage
- **Token families**: Track token lineage to detect theft
- **Automatic logout**: Revoke all tokens if suspicious activity

TOKEN LIFETIMES:
- Access token: 30 minutes (short-lived)
- Refresh token: 7 days (long-lived)

REFRESH FLOW:
1. Access token expires
2. Client sends refresh token to /auth/refresh
3. Server validates refresh token
4. Server generates new access token (+ optional new refresh token)
5. Client uses new access token

SECURITY:
- Refresh tokens should be stored securely (httpOnly cookies)
- One refresh token can't be used twice (rotation)
- Detect stolen tokens via token families

EXAMPLE:
POST /auth/login
→ {
    "access_token": "eyJ...",
    "refresh_token": "eyJ...",
    "token_type": "bearer"
  }

POST /auth/refresh
{"refresh_token": "eyJ..."}
→ {
    "access_token": "eyJ...",
    "refresh_token": "eyJ..."
  }

HINTS:
- Refresh tokens are JWTs with longer expiration
- Store refresh token hash in database for validation
- Set revoked=True instead of deleting
"""

from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import Session, sessionmaker, declarative_base
from datetime import datetime, timedelta
from pydantic import BaseModel, EmailStr
from passlib.context import CryptContext
from jose import jwt, JWTError
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import secrets

SECRET_KEY = "your-secret-key-change-in-production"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
REFRESH_TOKEN_EXPIRE_DAYS = 7

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
security = HTTPBearer()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True)
    hashed_password = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

# TODO: Create RefreshToken model
# Your code here

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

class TokenResponse(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"

class RefreshRequest(BaseModel):
    refresh_token: str

def create_access_token(email: str) -> str:
    """Create short-lived access token."""
    # TODO: Implement (same as Problem 13)
    pass

def create_refresh_token(user_id: int, db: Session) -> str:
    """
    Create long-lived refresh token and store in database.
    
    Returns:
        Refresh token string
    """
    # TODO: Implement refresh token creation
    # 1. Generate unique token (can use secrets.token_urlsafe())
    # 2. Set expiration (7 days)
    # 3. Store in database
    # 4. Return token
    # Your code here
    pass

async def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_db)
) -> User:
    """Get current user from access token."""
    # TODO: Implement (same as Problem 14)
    pass

app = FastAPI()

@app.on_event("startup")
def on_startup():
    init_db()

# TODO: Implement POST /auth/login
# Return both access_token and refresh_token
# Your code here

# TODO: Implement POST /auth/refresh
# 1. Validate refresh token exists in database
# 2. Check not expired
# 3. Check not revoked
# 4. Generate new access token
# 5. Optionally generate new refresh token (rotation)
# 6. Mark old refresh token as revoked
# 7. Return new tokens
# Your code here

# TODO: Implement POST /auth/logout
# Revoke all refresh tokens for current user
# Your code here
