"""
PROBLEM 19: Custom Validators
==============================

LEARNING OBJECTIVES:
- Create custom field validators in Pydantic
- Use @field_validator decorator
- Implement complex validation logic

TASK:
Create a signup endpoint with custom validation rules.

REQUIREMENTS:
- Define SignupData model with custom validators:
  - username: str, must be alphanumeric only, 3-20 chars
  - password: str, must contain at least one uppercase, one lowercase, one digit, min 8 chars
  - email: str (basic validation is automatic with EmailStr)
  - age: int, must be between 13 and 120
- Use @field_validator for username, password, and age validation
- POST endpoint at "/signup"
  - Accepts SignupData
  - Returns: {"message": "Signup successful", "username": username}

EXAMPLE:
POST /signup
{
  "username": "johndoe",
  "password": "SecurePass123",
  "email": "john@example.com",
  "age": 25
}
→ {"message": "Signup successful", "username": "johndoe"}

HINTS:
- from pydantic import field_validator, ValidationError
- Use @field_validator('field_name') before a method
- Raise ValueError with custom message if validation fails
- Method signature: def validate_field(cls, value): ...
- Return value if valid
"""

from fastapi import FastAPI
from pydantic import BaseModel, field_validator, EmailStr
import re

app = FastAPI()

class SignupData(BaseModel):
  username: str
  password: str
  email: EmailStr
  age: int 

  @field_validator('username')
  def validate_username(cls, v:str)-> str:
    if len(v)<3 or len(v)>20:
      raise ValueError('Username must be between 3 and 20 characters')
    if not v.isalnum():
      raise ValueError("Username must be alphanumeric")
    return v
  
  @field_validator('password')
  def validate_password(cls, v:str)->str:
    regex_pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$"
    if not re.fullmatch(regex_pattern, v):
      raise ValueError('must contain at least one uppercase, one lowercase, one digit, min 8 chars')
    return v

  @field_validator('age')
  def validate_age(cls, v:int)->int:
    if v<13 or v>120:
      raise ValueError("must be between 13 and 120")
    return v

@app.post("/signup")
def user_signup(signup: SignupData):
  return {
    "message": "Signup successful",
    "username": signup.username
  }
