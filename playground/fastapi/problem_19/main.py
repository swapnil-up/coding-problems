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

app = FastAPI()

# TODO: Define SignupData model with custom validators
# Your code here

# TODO: Create POST endpoint at "/signup"
# Your code here
