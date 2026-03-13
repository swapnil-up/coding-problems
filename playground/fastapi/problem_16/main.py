"""
PROBLEM 16: CORS (Cross-Origin Resource Sharing)
=================================================

LEARNING OBJECTIVES:
- Configure CORS in FastAPI
- Understand CORS middleware
- Allow specific origins and methods

TASK:
Set up CORS to allow requests from specific origins.

REQUIREMENTS:
- Add CORS middleware that allows:
  - Origins: ["http://localhost:3000", "http://localhost:8080"]
  - Methods: ["GET", "POST"]
  - Headers: ["*"]
  - Credentials: True
- GET endpoint at "/public"
  - Returns: {"message": "Public endpoint"}
- POST endpoint at "/data"
  - Body: {"value": str}
  - Returns: {"received": value}

EXAMPLE:
GET /public → {"message": "Public endpoint"}
POST /data {"value": "test"} → {"received": "test"}

Both should have CORS headers allowing the specified origins.

HINTS:
- from fastapi.middleware.cors import CORSMiddleware
- app.add_middleware(CORSMiddleware, ...)
- Use allow_origins, allow_credentials, allow_methods, allow_headers
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# TODO: Add CORS middleware with specified configuration
# Your code here

class DataInput(BaseModel):
    value: str

# TODO: Create GET endpoint at "/public"
# Your code here

# TODO: Create POST endpoint at "/data"
# Your code here
