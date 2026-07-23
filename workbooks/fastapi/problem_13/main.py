"""
PROBLEM 13: Status Codes and Response Types
============================================

LEARNING OBJECTIVES:
- Set custom status codes for responses
- Use status_code parameter in decorators
- Return appropriate codes for different operations

TASK:
Create CRUD endpoints with proper HTTP status codes.

REQUIREMENTS:
- Use a simple in-memory list: items = []
- POST "/items" - Create item (status 201)
  - Body: {"name": str}
  - Returns: {"id": auto_increment, "name": name}
  - Status code: 201
- DELETE "/items/{item_id}" - Delete item (status 204)
  - If found: delete and return status 204 with None
  - If not found: raise 404
  - Status code on success: 204

EXAMPLE:
POST /items {"name": "Test"} → 201 {"id": 1, "name": "Test"}
DELETE /items/1 → 204 (no content)
DELETE /items/999 → 404

HINTS:
- from fastapi import status
- Use status_code=status.HTTP_201_CREATED
- Use status_code=status.HTTP_204_NO_CONTENT
- For 204 responses, return None
- Use global variable or nonlocal for auto-increment ID
"""

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI()

# In-memory storage
items = []
next_id = 1

class ItemCreate(BaseModel):
    name: str

@app.post("/items", status_code=status.HTTP_201_CREATED)
def create_item(item: ItemCreate):
    global next_id
    new_item = {
        "id": next_id,
        "name": item.name
    }
    items.append(new_item)
    next_id += 1
    
    return new_item

@app.delete("/items/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(item_id: int):
    target_index = None
    for index, item in enumerate(items):
        if item["id"] == item_id:
            target_index = index
            break
    if target_index is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Item not found"
        )
    items.pop(target_index)
    return None