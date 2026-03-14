"""
PROBLEM 19: Logging, Monitoring, and Observability
===================================================

LEARNING OBJECTIVES:
- Implement comprehensive logging
- Add performance metrics
- Create health check endpoints
- Monitor application health

TASK:
Add production-grade logging and monitoring.

REQUIREMENTS:
1. Request/Response Logging Middleware:
   - Log every request with:
     * Method, path, status code
     * Duration (ms)
     * User agent
     * IP address (consider proxy headers)
   - Don't log sensitive data (tokens, passwords)

2. Health Check Endpoints:
   - GET /health
     * Basic liveness check
     * Returns: {"status": "healthy"}
   
   - GET /health/detailed
     * Database connectivity
     * Disk space
     * Memory usage
     * Returns: {
         "status": "healthy",
         "checks": {
           "database": "ok",
           "disk": "ok",
           "memory": "ok"
         }
       }

3. Metrics Endpoint:
   - GET /metrics
     * Request count
     * Average response time
     * Active connections
     * Error rate

4. Structured Logging:
   - JSON format for production
   - Include context (user_id, request_id)
   - Different log levels
   - Log rotation

PRODUCTION NOTES:
- **Don't log PII**: Mask emails, tokens, passwords
- **Performance**: Logging shouldn't slow down requests
- **Log rotation**: Prevent disk space issues
- **Centralized logging**: Ship to ELK, Splunk, Datadog
- **Metrics**: Use Prometheus, StatsD
- **Tracing**: Implement distributed tracing (Jaeger, Zipkin)
- **Alerting**: Alert on error rate, latency spikes
- **SLOs**: Define and track Service Level Objectives

WHAT TO LOG:
✓ Request start/end with duration
✓ Errors and exceptions
✓ Authentication events
✓ Database queries (slow queries)
✓ External API calls
✓ Business events (user signup, purchase)

WHAT NOT TO LOG:
✗ Passwords (plain or hashed)
✗ JWT tokens
✗ API keys
✗ Credit card numbers
✗ SSNs or other PII

HEALTH CHECK USES:
- Load balancer health checks
- Kubernetes liveness/readiness probes
- Monitoring systems
- Circuit breakers

EXAMPLE LOGS:
```json
{
  "timestamp": "2024-01-15T10:30:00Z",
  "level": "INFO",
  "message": "Request completed",
  "request_id": "abc-123",
  "method": "POST",
  "path": "/auth/login",
  "status_code": 200,
  "duration_ms": 45,
  "user_id": 123
}
```

HINTS:
- import time for duration measurement
- import psutil for system metrics
- structlog for structured logging
- Prometheus client library for metrics
"""

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import time
import psutil
import logging
from datetime import datetime
from pydantic import BaseModel
from typing import Dict
import json

# Configure structured logging
logging.basicConfig(
    level=logging.INFO,
    format='%(message)s'  # We'll use JSON
)
logger = logging.getLogger(__name__)

app = FastAPI()

# Metrics storage (in production, use Redis or Prometheus)
metrics = {
    "request_count": 0,
    "total_duration": 0.0,
    "error_count": 0
}

class HealthCheck(BaseModel):
    status: str

class DetailedHealthCheck(BaseModel):
    status: str
    checks: Dict[str, str]
    timestamp: datetime

class MetricsResponse(BaseModel):
    request_count: int
    avg_response_time_ms: float
    error_rate: float

# TODO: Logging middleware
@app.middleware("http")
async def logging_middleware(request: Request, call_next):
    """
    Log all requests with timing and context.
    
    Should log:
    - Request start
    - Request completion with duration
    - Errors
    
    Should mask sensitive data in URLs/headers.
    """
    # TODO: Implement request/response logging
    # 1. Record start time
    # 2. Process request
    # 3. Calculate duration
    # 4. Log structured JSON with context
    # 5. Update metrics
    # Your code here
    pass

def check_database_health() -> bool:
    """Check if database is accessible."""
    # TODO: Implement database health check
    # Try a simple query
    # Your code here
    pass

def check_disk_health() -> bool:
    """Check disk space availability."""
    # TODO: Implement disk space check
    # psutil.disk_usage('/')
    # Return False if >90% full
    # Your code here
    pass

def check_memory_health() -> bool:
    """Check memory usage."""
    # TODO: Implement memory check
    # psutil.virtual_memory()
    # Return False if >90% used
    # Your code here
    pass

# TODO: Implement GET /health
# Simple liveness check
# Your code here

# TODO: Implement GET /health/detailed
# Check database, disk, memory
# Return status for each
# Your code here

# TODO: Implement GET /metrics
# Return request_count, avg_response_time, error_rate
# Calculate from metrics dict
# Your code here
