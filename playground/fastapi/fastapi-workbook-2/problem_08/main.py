"""
PROBLEM 08: Handling Client Disconnection in Streams
=====================================================

LEARNING OBJECTIVES:
- Detect when client disconnects during streaming
- Clean up resources properly
- Implement graceful degradation
- Monitor stream health

TASK:
Create streaming endpoints that handle client disconnection gracefully.

REQUIREMENTS:
- POST /stream/monitored
  - Body: {"duration_seconds": int}
  - Streams numbers for duration_seconds
  - Detects if client disconnects
  - Logs disconnection
  - Stops streaming when disconnected
  - Returns SSE events

- GET /stream/status
  - Returns stats about active streams
  - Returns: {"active_streams": int}

PRODUCTION NOTES:
- **Resource cleanup**: Always clean up on disconnection
- **Memory leaks**: Ensure generators are properly closed
- **Monitoring**: Track active streams, detect stuck streams
- **Timeouts**: Set maximum stream duration
- **Graceful shutdown**: Handle server shutdown with active streams
- **Database connections**: Close DB connections if stream fails
- **File handles**: Close file handles on disconnection
- **Background tasks**: Cancel background tasks on disconnect

WHY THIS MATTERS:
- Users close browsers mid-stream
- Network issues cause disconnects
- Must not leak resources
- Long-running streams need monitoring

EXAMPLE:
POST /stream/monitored {"duration_seconds": 30}
If client disconnects after 5 seconds, server stops streaming and cleans up.

HINTS:
- Use Request object to check if client disconnected
- request.is_disconnected() returns True if disconnected
- Wrap streaming logic in try/finally for cleanup
- Use asyncio.create_task() for background monitoring
"""

from fastapi import FastAPI, Request
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
import asyncio
from typing import AsyncGenerator
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

# Track active streams
active_streams = 0

class StreamRequest(BaseModel):
    duration_seconds: int

async def monitored_stream(
    request: Request,
    duration_seconds: int
) -> AsyncGenerator[str, None]:
    """
    Stream with client disconnection detection.
    
    Yields numbers every second for duration_seconds.
    Stops if client disconnects.
    Logs connection status.
    """
    global active_streams
    active_streams += 1
    
    try:
        logger.info(f"Stream started, active streams: {active_streams}")
        
        for i in range(duration_seconds):
            # TODO: Check if client disconnected
            # If disconnected, log and break
            # Your code here
            
            # TODO: Yield SSE event
            # Your code here
            
            await asyncio.sleep(1)
        
        logger.info("Stream completed successfully")
    
    except Exception as e:
        logger.error(f"Stream error: {e}")
        raise
    
    finally:
        # TODO: Decrement active_streams
        # Log stream ending
        # Your code here
        pass

# TODO: Implement POST /stream/monitored
# Use StreamingResponse with monitored_stream generator
# Your code here

# TODO: Implement GET /stream/status
# Return {"active_streams": active_streams}
# Your code here
