"""
PROBLEM 12: Error Handling with HTTPException
==============================================

LEARNING OBJECTIVES:
- Raise HTTPException for errors
- Use proper HTTP status codes
- Provide detailed error messages

TASK:
Create a user lookup endpoint with proper error handling.

REQUIREMENTS:
- Create a fake user database (dict):
  users_db = {
    1: {"id": 1, "name": "Alice", "email": "alice@example.com"},
    2: {"id": 2, "name": "Bob", "email": "bob@example.com"}
  }
- GET endpoint at "/users/{user_id}"
- If user exists, return user data
- If user not found, raise HTTPException:
  - status_code: 404
  - detail: "User not found"
- If user_id < 1, raise HTTPException:
  - status_code: 400
  - detail: "Invalid user ID"

EXAMPLE:
GET /users/1 → {"id": 1, "name": "Alice", "email": "alice@example.com"}
GET /users/999 → 404 error with "User not found"
GET /users/0 → 400 error with "Invalid user ID"

HINTS:
- from fastapi import HTTPException
- raise HTTPException(status_code=..., detail="...")
- Check user_id validity before database lookup
"""

from fastapi import FastAPI, HTTPException, status

app = FastAPI()

# Database of users
users_db = {
    1: {"id": 1, "name": "Alice", "email": "alice@example.com"},
    2: {"id": 2, "name": "Bob", "email": "bob@example.com"}
}


@app.get("/users/{user_id}")
def get_user(user_id:int):
    if user_id<1:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail= "Invalid user ID"
        )
    if users_db.get(user_id):
        return users_db.get(user_id)
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail= "User not found"
        )