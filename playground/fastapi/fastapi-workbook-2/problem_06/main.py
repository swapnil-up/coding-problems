"""
PROBLEM 06: Server-Sent Events (SSE) for Streaming
===================================================

LEARNING OBJECTIVES:
- Understand Server-Sent Events protocol
- Implement streaming endpoints in FastAPI
- Use StreamingResponse
- Handle generator functions

TASK:
Create a streaming endpoint that sends data to clients in real-time.

REQUIREMENTS:
- GET /stream/count
  - Query param: max_count (default=10, max=100)
  - Streams numbers from 1 to max_count
  - Each number sent as a separate SSE event
  - 100ms delay between each number
  - Returns Content-Type: text/event-stream

- GET /stream/text
  - Query param: text (required)
  - Streams the text word by word
  - Each word sent as separate SSE event
  - 50ms delay between words
  - Returns Content-Type: text/event-stream

SSE MESSAGE FORMAT:
Each message should be formatted as:
data: {your_data}\n\n

Example:
data: hello\n\n
data: world\n\n

PRODUCTION NOTES:
- **Client disconnection**: Always check if client disconnected (FastAPI handles this)
- **Memory management**: Don't load entire response in memory before streaming
- **Timeouts**: Set reasonable timeouts (e.g., 30s max for a stream)
- **Error handling**: If generation fails mid-stream, send error event
- **Reconnection**: Clients may reconnect; handle this gracefully
- **CORS**: For frontend, ensure CORS allows streaming responses
- **Load balancing**: Sticky sessions may be needed with load balancers

WHY SSE vs WebSockets:
- SSE is simpler for server→client streaming (like LLM responses)
- WebSockets needed for bidirectional communication
- SSE works over HTTP, easier to deploy
- SSE auto-reconnects on connection loss

EXAMPLE:
GET /stream/count?max_count=3

Response (streaming):
data: 1

data: 2

data: 3

HINTS:
- from fastapi.responses import StreamingResponse
- Use async def generator functions
- yield f"data: {value}\n\n" for each event
- Use asyncio.sleep() for delays
- Return StreamingResponse(generator(), media_type="text/event-stream")
"""

from fastapi import FastAPI, Query
from fastapi.responses import StreamingResponse
import asyncio
from typing import AsyncGenerator

app = FastAPI()

# TODO: Implement async generator function for counting
async def count_generator(max_count: int) -> AsyncGenerator[str, None]:
    """
    Generate numbers from 1 to max_count with delays.
    
    Yields SSE-formatted messages.
    """
    for i in range(1, max_count + 1):
      await asyncio.sleep(0.1)
      yield f"data: {i}\n\n"

# TODO: Implement async generator function for text streaming
async def text_generator(text: str) -> AsyncGenerator[str, None]:
    """
    Stream text word by word.
    
    Yields SSE-formatted messages.
    """
    words = text.split()
    for word in words:
       await asyncio.sleep(0.05)
       yield f"data: {word}\n\n"

@app.get("/stream/count")
async def get_num(max_count: int=Query(default=10, le=100)):
  return StreamingResponse(count_generator(max_count), media_type="text/event-stream")

@app.get("/stream/text")
async def get_text(text: str):
   return StreamingResponse(text_generator(text), media_type="text/event-stream")