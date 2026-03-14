"""
PROBLEM 18: Centralized Error Handling and Logging
===================================================

LEARNING OBJECTIVES:
- Create custom exception handlers
- Implement consistent error responses
- Add structured logging
- Track errors for debugging

TASK:
Implement centralized error handling with proper logging.

REQUIREMENTS:
1. Custom exception handlers:
   - Handle SQLAlchemy errors → 500
   - Handle ValidationError → 422
   - Handle all other exceptions → 500
   - Return consistent JSON format

2. Error response format:
   ```json
   {
     "error": {
       "code": "DATABASE_ERROR",
       "message": "User-friendly message",
       "detail": "Technical detail (dev mode only)",
       "request_id": "uuid"
     }
   }
   ```

3. Logging:
   - Log all errors with context
   - Include request ID for tracing
   - Structured JSON logging
   - Different log levels (DEBUG, INFO, ERROR)

4. Request ID middleware:
   - Generate unique ID for each request
   - Add to response headers
   - Include in all logs

PRODUCTION NOTES:
- **User-friendly messages**: Don't expose internal errors to users
- **Error tracking**: Integrate with Sentry, Rollbar, etc.
- **Request tracing**: Use request IDs to track user journeys
- **Log aggregation**: Send logs to ELK, Datadog, CloudWatch
- **Alerting**: Alert on error rate spikes
- **Error budgets**: Track error rates as SLOs
- **Sensitive data**: Never log passwords, tokens, PII

ERROR CODES:
- VALIDATION_ERROR: 422
- NOT_FOUND: 404
- UNAUTHORIZED: 401
- FORBIDDEN: 403
- DATABASE_ERROR: 500
- INTERNAL_ERROR: 500

LOGGING BEST PRACTICES:
- Structured logging (JSON)
- Correlation IDs
- Log levels (DEBUG/INFO/WARNING/ERROR/CRITICAL)
- Context (user_id, endpoint, etc.)
- Performance metrics
- Never log secrets

EXAMPLE:
GET /users/999
→ 404 {
  "error": {
    "code": "NOT_FOUND",
    "message": "User not found",
    "detail": "User with ID 999 does not exist",
    "request_id": "abc-123-def"
  }
}

HINTS:
- @app.exception_handler(Exception)
- from fastapi import Request
- import logging
- Use logging.getLogger(__name__)
- structlog for structured logging
"""

from fastapi import FastAPI, Request, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from sqlalchemy.exc import SQLAlchemyError
from pydantic import BaseModel
import logging
import uuid
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

app = FastAPI()

class ErrorResponse(BaseModel):
    code: str
    message: str
    detail: str = None
    request_id: str

class ErrorResponseWrapper(BaseModel):
    error: ErrorResponse

# TODO: Middleware to add request ID
@app.middleware("http")
async def add_request_id(request: Request, call_next):
    """Add unique request ID to each request."""
    # TODO: Implement request ID generation
    # 1. Generate UUID
    # 2. Add to request.state
    # 3. Process request
    # 4. Add to response headers
    # Your code here
    pass

# TODO: Exception handler for HTTPException
@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    """Handle FastAPI HTTPExceptions."""
    # TODO: Implement consistent error response
    # Your code here
    pass

# TODO: Exception handler for RequestValidationError
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    """Handle Pydantic validation errors."""
    # TODO: Implement validation error response
    # Your code here
    pass

# TODO: Exception handler for SQLAlchemyError
@app.exception_handler(SQLAlchemyError)
async def database_exception_handler(request: Request, exc: SQLAlchemyError):
    """Handle database errors."""
    # TODO: Implement database error response
    # Log error with context
    # Return user-friendly message
    # Your code here
    pass

# TODO: Exception handler for general Exception
@app.exception_handler(Exception)
async def general_exception_handler(request: Request, exc: Exception):
    """Catch-all handler for unexpected errors."""
    # TODO: Implement general error response
    # Log full traceback
    # Return generic error to user
    # Your code here
    pass

# Test endpoints
@app.get("/test/error")
def test_error():
    """Endpoint to test error handling."""
    raise Exception("This is a test error")

@app.get("/test/validation")
def test_validation(value: int):
    """Endpoint to test validation errors."""
    return {"value": value}

@app.get("/test/not-found")
def test_not_found():
    """Endpoint to test 404 errors."""
    raise HTTPException(status_code=404, detail="Resource not found")
