"""
PROBLEM 15: Middleware
=======================

LEARNING OBJECTIVES:
- Create custom middleware
- Process requests before/after endpoint execution
- Add custom headers

TASK:
Create middleware that adds timing and custom headers to responses.

REQUIREMENTS:
- Create middleware that:
  - Adds header "X-Process-Time" with request processing time
  - Adds header "X-Custom-Header" with value "FastAPI-Workbook"
  - Works for all endpoints
- GET endpoint at "/test"
  - Returns: {"message": "Middleware test"}

EXAMPLE:
GET /test
Response headers should include:
- X-Process-Time: 0.001 (or similar)
- X-Custom-Header: FastAPI-Workbook

HINTS:
- Use @app.middleware("http")
- Middleware function signature: async def middleware(request, call_next)
- Use time.time() to measure duration
- Add headers: response.headers["X-Header-Name"] = "value"
- Remember to call: response = await call_next(request)
"""

from fastapi import FastAPI, Request
import time

app = FastAPI()

# TODO: Create middleware that adds timing and custom header
# Your code here

# TODO: Create GET endpoint at "/test"
# Your code here
