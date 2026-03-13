"""
PROBLEM 17: Optional Fields and Defaults
=========================================

LEARNING OBJECTIVES:
- Use Optional fields in Pydantic models
- Understand the difference between Optional and default values
- Handle partial updates (PATCH)

TASK:
Create a user update endpoint that handles partial updates.

REQUIREMENTS:
- User storage: users_db = {1: {"id": 1, "name": "Alice", "email": "alice@example.com", "age": 30}}
- Define UserUpdate model with ALL optional fields:
  - name: Optional[str] = None
  - email: Optional[str] = None
  - age: Optional[int] = None
- PATCH endpoint at "/users/{user_id}"
  - Accepts UserUpdate
  - Updates only provided fields
  - Returns updated user
  - Raises 404 if user not found

EXAMPLE:
PATCH /users/1 {"email": "newemail@example.com"}
→ {"id": 1, "name": "Alice", "email": "newemail@example.com", "age": 30}
(only email changed)

HINTS:
- from typing import Optional
- Use model.dict(exclude_unset=True) to get only provided fields
- Update user_db entry with new values
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# User database
users_db = {
    1: {"id": 1, "name": "Alice", "email": "alice@example.com", "age": 30}
}

# TODO: Define UserUpdate model with optional fields
# Your code here

# TODO: Create PATCH endpoint at "/users/{user_id}"
# Update only the fields that are provided
# Your code here
