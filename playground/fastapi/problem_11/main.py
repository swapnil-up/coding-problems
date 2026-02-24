"""
PROBLEM 11: Async Endpoints
============================

LEARNING OBJECTIVES:
- Use async/await in FastAPI endpoints
- Understand when to use async
- Work with async functions

TASK:
Create async endpoints that simulate I/O operations.

REQUIREMENTS:
- GET endpoint at "/slow-task"
  - Use async def
  - Use asyncio.sleep(0.1) to simulate slow operation
  - Returns: {"status": "completed", "duration": 0.1}
- GET endpoint at "/parallel-tasks"
  - Accepts count: int (query param, default=3, max=10)
  - Use asyncio.gather() to run count tasks in parallel
  - Each task does asyncio.sleep(0.1)
  - Returns: {"tasks_completed": count, "time_saved": "Tasks ran in parallel"}

EXAMPLE:
GET /slow-task
→ {"status": "completed", "duration": 0.1}

GET /parallel-tasks?count=5
→ {"tasks_completed": 5, "time_saved": "Tasks ran in parallel"}

HINTS:
- import asyncio
- Use async def instead of def
- Use await before async operations
- asyncio.gather(*tasks) runs tasks concurrently
"""

from fastapi import FastAPI, Query
import asyncio

app = FastAPI()

@app.get("/slow-task/")
async def slow_task():
    await asyncio.sleep(0.1)
    return{
        "status": "completed",
        "duration": 0.1
    }

@app.get("/parallel-tasks/")
async def parallel_task(count: int = Query(default=3, le=10)):
    tasks = [asyncio.sleep(0.1) for c in range(count)]
    await asyncio.gather(*tasks)
    return {"tasks_completed": count, "time_saved": "Tasks ran in parallel"}

