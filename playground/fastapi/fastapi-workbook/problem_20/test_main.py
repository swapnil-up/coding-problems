"""
Tests for Problem 20: Writing Tests for FastAPI

This file is INCOMPLETE. Your task is to fill in the test functions.

Each test function has a docstring explaining what it should test.
Write the code to implement each test.

HINTS:
- Use client.get(), client.post(), client.put(), client.delete()
- Check response.status_code
- Check response.json() for data
- Use assert statements to verify expectations
- Remember to reset the database between tests if needed
"""

from fastapi.testclient import TestClient
from main import app, todos_db, next_id
import pytest

client = TestClient(app)


@pytest.fixture(autouse=True)
def reset_database():
    """Reset database before each test"""
    todos_db.clear()
    # Reset next_id - this is tricky since it's global
    import main
    main.next_id = 1
    yield

def test_list_todos_empty():
    """Test that listing todos returns empty array when no todos exist"""
    response = client.get("/todos")
    assert response.status_code == 200
    assert response.json() == []

def test_create_todo():
    """Test creating a new todo"""
    response = client.post("/todos", json={"title": "Test", "completed": False})
    assert response.status_code == 201
    data = response.json()
    assert data["id"] == 1
    assert data["title"] == "Test"
    assert data["completed"] is False

def test_create_todo_defaults_completed_to_false():
    """Test that completed defaults to False if not provided"""
    # Sending only title, no 'completed' key
    response = client.post("/todos", json={"title": "Default Test"})
    assert response.status_code == 201
    assert response.json()["completed"] is False

def test_list_todos_returns_created_todos():
    """Test that listing todos returns previously created todos"""
    client.post("/todos", json={"title": "Todo 1"})
    client.post("/todos", json={"title": "Todo 2"})
    
    response = client.get("/todos")
    assert response.status_code == 200
    assert len(response.json()) == 2

def test_get_specific_todo():
    """Test getting a specific todo by ID"""
    create_res = client.post("/todos", json={"title": "Find Me"})
    todo_id = create_res.json()["id"]
    
    response = client.get(f"/todos/{todo_id}")
    assert response.status_code == 200
    assert response.json()["title"] == "Find Me"

def test_get_nonexistent_todo():
    """Test that getting non-existent todo returns 404"""
    response = client.get("/todos/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Todo not found"

def test_update_todo():
    """Test updating a todo"""
    create_res = client.post("/todos", json={"title": "Old Title", "completed": False})
    todo_id = create_res.json()["id"]
    
    response = client.put(f"/todos/{todo_id}", json={"title": "New Title", "completed": True})
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "New Title"
    assert data["completed"] is True

def test_update_nonexistent_todo():
    """Test that updating non-existent todo returns 404"""
    response = client.put("/todos/999", json={"title": "Ghost", "completed": True})
    assert response.status_code == 404

def test_delete_todo():
    """Test deleting a todo"""
    create_res = client.post("/todos", json={"title": "Delete Me"})
    todo_id = create_res.json()["id"]
    
    delete_res = client.delete(f"/todos/{todo_id}")
    assert delete_res.status_code == 204
    
    # Verify it is gone
    get_res = client.get(f"/todos/{todo_id}")
    assert get_res.status_code == 404

def test_delete_nonexistent_todo():
    """Test that deleting non-existent todo returns 404"""
    response = client.delete("/todos/999")
    assert response.status_code == 404

def test_create_multiple_todos_increments_id():
    """Test that creating multiple todos increments IDs"""
    res1 = client.post("/todos", json={"title": "T1"})
    res2 = client.post("/todos", json={"title": "T2"})
    res3 = client.post("/todos", json={"title": "T3"})
    
    assert res1.json()["id"] == 1
    assert res2.json()["id"] == 2
    assert res3.json()["id"] == 3

@pytest.mark.parametrize("title,completed", [
    ("Buy groceries", False),
    ("Finish homework", True),
    ("Call mom", False),
])
def test_create_various_todos(title, completed):
    """Test creating todos with various data"""
    response = client.post("/todos", json={"title": title, "completed": completed})
    assert response.status_code == 201
    assert response.json()["title"] == title
    assert response.json()["completed"] == completed

def test_create_todo_missing_title():
    """Test that creating todo without title returns validation error (422)"""
    response = client.post("/todos", json={"completed": True})
    assert response.status_code == 422