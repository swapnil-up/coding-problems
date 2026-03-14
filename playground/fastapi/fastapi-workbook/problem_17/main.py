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

class UserUpdate(BaseModel):
  name: Optional[str]=None
  email: Optional[str]=None
  age: Optional[int]=None

@app.patch("/users/{user_id}")
def update_user(user_id: int, user_update: UserUpdate):
  if user_id not in users_db:
    raise HTTPException(status_code=404, detail="User not found")
  updated = user_update.model_dump(exclude_unset=True)
  users_db[user_id].update(updated)
  return users_db[user_id]
