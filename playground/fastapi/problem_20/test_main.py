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


# TODO: Implement this test
def test_list_todos_empty():
    """Test that listing todos returns empty array when no todos exist"""
    # Your code here
    pass


# TODO: Implement this test
def test_create_todo():
    """Test creating a new todo"""
    # Your code here
    # Hint: POST to /todos with {"title": "Test", "completed": false}
    # Check status code is 201
    # Check response has id, title, completed fields
    pass


# TODO: Implement this test
def test_create_todo_defaults_completed_to_false():
    """Test that completed defaults to False if not provided"""
    # Your code here
    pass


# TODO: Implement this test
def test_list_todos_returns_created_todos():
    """Test that listing todos returns previously created todos"""
    # Your code here
    # Hint: Create 2-3 todos, then GET /todos and check they're all there
    pass


# TODO: Implement this test
def test_get_specific_todo():
    """Test getting a specific todo by ID"""
    # Your code here
    # Hint: Create a todo, note its ID, then GET /todos/{id}
    pass


# TODO: Implement this test
def test_get_nonexistent_todo():
    """Test that getting non-existent todo returns 404"""
    # Your code here
    pass


# TODO: Implement this test
def test_update_todo():
    """Test updating a todo"""
    # Your code here
    # Hint: Create a todo, then PUT to /todos/{id} with new data
    pass


# TODO: Implement this test
def test_update_nonexistent_todo():
    """Test that updating non-existent todo returns 404"""
    # Your code here
    pass


# TODO: Implement this test
def test_delete_todo():
    """Test deleting a todo"""
    # Your code here
    # Hint: Create a todo, DELETE it, check status 204
    # Then try to GET it and should get 404
    pass


# TODO: Implement this test
def test_delete_nonexistent_todo():
    """Test that deleting non-existent todo returns 404"""
    # Your code here
    pass


# TODO: Implement this test
def test_create_multiple_todos_increments_id():
    """Test that creating multiple todos increments IDs"""
    # Your code here
    # Hint: Create 3 todos and check their IDs are 1, 2, 3
    pass


# BONUS TODO: Implement this test using parametrization
@pytest.mark.parametrize("title,completed", [
    ("Buy groceries", False),
    ("Finish homework", True),
    ("Call mom", False),
])
def test_create_various_todos(title, completed):
    """Test creating todos with various data"""
    # Your code here
    pass


# BONUS TODO: Test validation
def test_create_todo_missing_title():
    """Test that creating todo without title returns validation error"""
    # Your code here
    # Hint: POST with {} or {"completed": true} should fail
    pass
