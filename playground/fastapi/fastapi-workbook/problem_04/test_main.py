"""Tests for Problem 04: Request Body"""

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_create_user_with_all_fields():
    """Test creating a user with all fields"""
    response = client.post(
        "/users",
        json={"name": "Alice", "email": "alice@example.com", "age": 30}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "User created"
    assert data["user"]["name"] == "Alice"
    assert data["user"]["email"] == "alice@example.com"
    assert data["user"]["age"] == 30


def test_create_user_without_age():
    """Test creating a user without optional age field"""
    response = client.post(
        "/users",
        json={"name": "Bob", "email": "bob@example.com"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["user"]["name"] == "Bob"
    assert data["user"]["email"] == "bob@example.com"
    assert data["user"]["age"] is None


def test_missing_required_field():
    """Test that missing required fields return validation error"""
    response = client.post(
        "/users",
        json={"name": "Charlie"}  # Missing email
    )
    assert response.status_code == 422


def test_invalid_age_type():
    """Test that invalid age type returns validation error"""
    response = client.post(
        "/users",
        json={"name": "David", "email": "david@example.com", "age": "thirty"}
    )
    assert response.status_code == 422