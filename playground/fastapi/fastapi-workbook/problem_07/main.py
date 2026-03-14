"""
PROBLEM 07: Multiple Parameter Types
=====================================

LEARNING OBJECTIVES:
- Combine path, query, and body parameters in one endpoint
- Understand parameter precedence and FastAPI's type detection
- Handle complex endpoint signatures

TASK:
Create an endpoint that updates a user's profile using all parameter types.

REQUIREMENTS:
- Define UpdateProfile model with: bio (str, optional), website (str, optional)
- PUT endpoint at "/users/{user_id}/profile"
- Path parameter: user_id (int)
- Query parameter: notify (bool, default=False)
- Body: UpdateProfile model
- Returns: {
    "user_id": user_id,
    "updated": {profile data},
    "notification_sent": notify
  }

EXAMPLE:
PUT /users/123/profile?notify=true
Body: {"bio": "FastAPI developer", "website": "https://example.com"}
→ {
    "user_id": 123,
    "updated": {"bio": "FastAPI developer", "website": "https://example.com"},
    "notification_sent": true
  }

HINTS:
- Path parameters come first in function signature
- Then query parameters
- Body parameters (Pydantic models) come last
- FastAPI determines parameter type by position and type hints
"""

from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class UpdateProfile(BaseModel):
    bio: Optional[str] = None
    website: Optional[str] = None

@app.put("/users/{user_id}/profile")
def update_user(user_id: int, profile: UpdateProfile, notify: bool=False):
    return {
        "user_id": user_id,
        "updated": profile,
        "notification_sent": notify,
    }
