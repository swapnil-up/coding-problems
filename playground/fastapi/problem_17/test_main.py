"""Tests for Problem 17: Optional Fields and Defaults"""

from fastapi.testclient import TestClient
from main import app, users_db

client = TestClient(app)


def setup_function():
    """Reset user database before each test"""
    users_db.clear()
    users_db[1] = {"id": 1, "name": "Alice", "email": "alice@example.com", "age": 30}


def test_update_only_email():
    """Test updating only email field"""
    response = client.patch(
        "/users/1",
        json={"email": "newemail@example.com"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["email"] == "newemail@example.com"
    assert data["name"] == "Alice"  # Unchanged
    assert data["age"] == 30  # Unchanged


def test_update_only_name():
    """Test updating only name field"""
    response = client.patch(
        "/users/1",
        json={"name": "Alicia"}
    )
    data = response.json()
    assert data["name"] == "Alicia"
    assert data["email"] == "alice@example.com"  # Unchanged
    assert data["age"] == 30  # Unchanged


def test_update_only_age():
    """Test updating only age field"""
    response = client.patch(
        "/users/1",
        json={"age": 31}
    )
    data = response.json()
    assert data["age"] == 31
    assert data["name"] == "Alice"  # Unchanged
    assert data["email"] == "alice@example.com"  # Unchanged


def test_update_multiple_fields():
    """Test updating multiple fields at once"""
    response = client.patch(
        "/users/1",
        json={"name": "Bob", "age": 25}
    )
    data = response.json()
    assert data["name"] == "Bob"
    assert data["age"] == 25
    assert data["email"] == "alice@example.com"  # Unchanged


def test_update_all_fields():
    """Test updating all fields"""
    response = client.patch(
        "/users/1",
        json={
            "name": "Charlie",
            "email": "charlie@example.com",
            "age": 35
        }
    )
    data = response.json()
    assert data["name"] == "Charlie"
    assert data["email"] == "charlie@example.com"
    assert data["age"] == 35


def test_update_with_empty_body():
    """Test update with no fields changes nothing"""
    response = client.patch("/users/1", json={})
    data = response.json()
    assert data["name"] == "Alice"
    assert data["email"] == "alice@example.com"
    assert data["age"] == 30


def test_update_non_existent_user():
    """Test updating non-existent user returns 404"""
    response = client.patch(
        "/users/999",
        json={"name": "Nobody"}
    )
    assert response.status_code == 404


def test_changes_persist():
    """Test that changes persist across requests"""
    # First update
    client.patch("/users/1", json={"name": "Updated"})
    
    # Second update should see the first change
    response = client.patch("/users/1", json={"age": 40})
    data = response.json()
    assert data["name"] == "Updated"  # From first update
    assert data["age"] == 40  # From second update
