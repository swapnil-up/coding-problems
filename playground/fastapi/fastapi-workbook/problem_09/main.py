"""
PROBLEM 09: Dependency Injection Basics
========================================

LEARNING OBJECTIVES:
- Understand FastAPI's dependency injection system
- Create reusable dependencies
- Use Depends() for parameter injection

TASK:
Create a pagination system using dependencies.

REQUIREMENTS:
- Create a dependency function common_parameters with:
  - skip: int (default=0, min=0)
  - limit: int (default=10, min=1, max=100)
  - Returns a dict: {"skip": skip, "limit": limit}
- GET endpoint at "/items" that uses this dependency
- Returns: {
    "pagination": {pagination params},
    "items": list of fake item IDs based on pagination
  }
- For items, return a list: [skip+1, skip+2, ..., skip+limit]

EXAMPLE:
GET /items?skip=5&limit=3
→ {
    "pagination": {"skip": 5, "limit": 3},
    "items": [6, 7, 8]
  }

HINTS:
- from fastapi import Depends
- Define a function that takes skip and limit parameters
- Use Depends(function_name) in the endpoint's parameters
- The function will be called automatically with query params
"""

from fastapi import FastAPI, Depends, Query
from pydantic import BaseModel, Field

app = FastAPI()

class common_params(BaseModel):
    skip: int = Field(default=0, ge=0)
    limit: int = Field(default=10, ge=1, le=100)

def pagination(skip: int = Query(default= 0, ge=0), limit: int = Query(default= 10, ge=1, le=100)):
    return {"skip": skip, "limit": limit}

@app.get("/items/")
def get_items(common_parameters: dict = Depends(pagination)):
    items = [common_parameters['skip']+i+1 for i in range(common_parameters["limit"])]
    return {
        "pagination": common_parameters,
        "items": items
    }