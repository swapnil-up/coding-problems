"""
PROBLEM 20: Writing Tests for FastAPI
======================================

LEARNING OBJECTIVES:
- Write comprehensive tests for FastAPI apps
- Test different HTTP methods
- Test error cases
- Use fixtures and parametrization

TASK:
You are given a simple TODO API. Write comprehensive tests for it.

The API is already implemented below. Your job is to complete the test file.

API ENDPOINTS:
- GET /todos - List all todos
- POST /todos - Create a todo (body: {"title": str, "completed": bool})
- GET /todos/{todo_id} - Get specific todo
- PUT /todos/{todo_id} - Update todo
- DELETE /todos/{todo_id} - Delete todo

Your test file should test:
1. Creating todos
2. Listing todos
3. Getting specific todo
4. Updating todo
5. Deleting todo
6. Error cases (404, validation errors)
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class TodoCreate(BaseModel):
    title: str
    completed: bool = False

class Todo(BaseModel):
    id: int
    title: str
    completed: bool

# In-memory storage
todos_db = {}
next_id = 1

@app.get("/todos", response_model=List[Todo])
def list_todos():
    return list(todos_db.values())

@app.post("/todos", response_model=Todo, status_code=201)
def create_todo(todo: TodoCreate):
    global next_id
    new_todo = Todo(id=next_id, title=todo.title, completed=todo.completed)
    todos_db[next_id] = new_todo
    next_id += 1
    return new_todo

@app.get("/todos/{todo_id}", response_model=Todo)
def get_todo(todo_id: int):
    if todo_id not in todos_db:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todos_db[todo_id]

@app.put("/todos/{todo_id}", response_model=Todo)
def update_todo(todo_id: int, todo: TodoCreate):
    if todo_id not in todos_db:
        raise HTTPException(status_code=404, detail="Todo not found")
    updated_todo = Todo(id=todo_id, title=todo.title, completed=todo.completed)
    todos_db[todo_id] = updated_todo
    return updated_todo

@app.delete("/todos/{todo_id}", status_code=204)
def delete_todo(todo_id: int):
    if todo_id not in todos_db:
        raise HTTPException(status_code=404, detail="Todo not found")
    del todos_db[todo_id]
    return None
