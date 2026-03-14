"""
PROBLEM 10: Class-Based Dependencies
=====================================

LEARNING OBJECTIVES:
- Create dependency classes
- Understand __call__ method for dependencies
- Use class instances as dependencies

TASK:
Create an authentication dependency using a class.

REQUIREMENTS:
- Create a class TokenValidator with:
  - __init__ that accepts required_role: str
  - __call__ that accepts token: str (from header)
  - Returns: {"token": token, "role": required_role, "valid": True}
  - For this exercise, just return valid=True (we're not doing real auth)
- GET endpoint at "/admin" using Depends(TokenValidator("admin"))
- GET endpoint at "/user" using Depends(TokenValidator("user"))
- Both return: {"message": "Access granted", "auth": {auth_info}}

EXAMPLE:
GET /admin?token=abc123
→ {
    "message": "Access granted",
    "auth": {"token": "abc123", "role": "admin", "valid": true}
  }

HINTS:
- Create a class with __init__ and __call__ methods
- __call__ makes the class instance callable like a function
- Use Query() to get token from query parameter in __call__
- Instantiate the class when using Depends: Depends(TokenValidator("admin"))
"""

from typing import Any, Optional

from fastapi import FastAPI, Depends, Header, Query

app = FastAPI()

class TokenValidator:
    def __init__(self, required_role: str):
        self.required_role = required_role
    
    def __call__(self, token: str = Query(...)):
        return {
           "token": token,
           "role": self.required_role,
           "valid": True,
           
        }
    
@app.get("/admin/")
def admin_login(token: str = Depends(TokenValidator("admin"))):
    return {
        "message": "Access granted",
        "auth": token
    }

@app.get("/user/")
def user_login(token: str = Depends(TokenValidator("user"))):
    return {
        "message": "Access granted",
        "auth": token
    }