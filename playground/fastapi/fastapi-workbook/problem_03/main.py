"""
PROBLEM 03: Query Parameters
=============================

LEARNING OBJECTIVES:
- Use query parameters in FastAPI
- Handle optional query parameters with defaults
- Type conversion and validation

TASK:
Create a search endpoint that accepts query parameters for filtering.

REQUIREMENTS:
- GET endpoint at "/search"
- Query parameters:
  - q: search query (required, string)
  - limit: max results (optional, default=10, integer)
  - skip: offset for pagination (optional, default=0, integer)
- Returns: {
    "query": q,
    "limit": limit,
    "skip": skip,
    "results_count": limit  # Just return the limit value as mock count
  }

EXAMPLE:
GET /search?q=python&limit=5&skip=10
→ {"query": "python", "limit": 5, "skip": 10, "results_count": 5}

HINTS:
- Query parameters are function arguments without being in the path
- Use default values: def endpoint(param: type = default)
- Type hints help FastAPI validate and convert values
"""

from fastapi import FastAPI

app = FastAPI()

@app.get("/search/")
async def search_params(q: str, limit: int=10, skip: int=0):
    return {
        "query": q,
        "limit": limit,
        "skip": skip,
        "results_count": limit
    }