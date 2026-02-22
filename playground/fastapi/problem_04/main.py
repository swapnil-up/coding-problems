"""
PROBLEM 04: Request Body
=========================

LEARNING OBJECTIVES:
- Accept JSON request bodies
- Use Pydantic models for request validation
- POST requests in FastAPI

TASK:
Create an endpoint that accepts user data via POST request.

REQUIREMENTS:
- Define a Pydantic model "User" with:
  - name: string (required)
  - email: string (required)
  - age: integer (optional, default=None)
- POST endpoint at "/users"
- Accepts User model in request body
- Returns: {
    "message": "User created",
    "user": {user data}
  }

EXAMPLE:
POST /users
Body: {"name": "Alice", "email": "alice@example.com", "age": 30}
→ {"message": "User created", "user": {"name": "Alice", "email": "alice@example.com", "age": 30}}

HINTS:
- Import BaseModel from pydantic
- Define a class that inherits from BaseModel
- Use the model as a type hint in the endpoint function
"""

from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class User(BaseModel):
    name: str
    email: str
    age: Optional[int] = None

@app.post("/users")
def create_user(user: User):
    return {
        "message": "User created",
        "user": user,
    }