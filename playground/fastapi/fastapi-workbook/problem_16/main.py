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

origins = ["http://localhost:3000", "http://localhost:8080", "http://127.0.0.1:8000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"]
)

class DataInput(BaseModel):
    value: str

@app.get("/public")
def public_func():
    return {"message": "Public endpoint"}
    
@app.post("/data")
def send_data(input: DataInput):
  return {"received": input.value}