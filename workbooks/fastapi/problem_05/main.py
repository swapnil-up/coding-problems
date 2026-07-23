"""
PROBLEM 05: Response Models
============================

LEARNING OBJECTIVES:
- Use response_model to define response structure
- Filter sensitive data from responses
- Understand response model benefits

TASK:
Create endpoints that properly handle sensitive user data using response models.

REQUIREMENTS:
- Define UserCreate model with: username, email, password
- Define UserResponse model with: username, email (NO password)
- POST endpoint at "/register" that:
  - Accepts UserCreate
  - Uses response_model=UserResponse
  - Returns user data WITHOUT password

EXAMPLE:
POST /register
Body: {"username": "alice", "email": "alice@example.com", "password": "secret123"}
→ {"username": "alice", "email": "alice@example.com"}
(password should NOT be in response)

HINTS:
- Create two separate Pydantic models
- Use response_model parameter in the decorator
- You can return the UserCreate object; FastAPI will filter it to UserResponse
"""

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class UserCreate(BaseModel):
    username: str
    email: str
    password: str

class UserResponse(BaseModel):
    username: str
    email: str

@app.post("/register", response_model=UserResponse)
def register_user(user: UserCreate):
    return user