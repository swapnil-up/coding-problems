"""Tests for Problem 12: Error Handling with HTTPException"""

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_get_existing_user_1():
    """Test getting user 1"""
    response = client.get("/users/1")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert data["name"] == "Alice"
    assert data["email"] == "alice@example.com"


def test_get_existing_user_2():
    """Test getting user 2"""
    response = client.get("/users/2")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 2
    assert data["name"] == "Bob"


def test_user_not_found():
    """Test 404 for non-existent user"""
    response = client.get("/users/999")
    assert response.status_code == 404
    data = response.json()
    assert data["detail"] == "User not found"


def test_another_non_existent_user():
    """Test 404 for another non-existent user"""
    response = client.get("/users/42")
    assert response.status_code == 404


def test_invalid_user_id_zero():
    """Test 400 for user ID = 0"""
    response = client.get("/users/0")
    assert response.status_code == 400
    data = response.json()
    assert data["detail"] == "Invalid user ID"


def test_invalid_user_id_negative():
    """Test 400 for negative user ID"""
    response = client.get("/users/-1")
    assert response.status_code == 400
    data = response.json()
    assert data["detail"] == "Invalid user ID"


def test_invalid_user_id_large_negative():
    """Test 400 for large negative user ID"""
    response = client.get("/users/-999")
    assert response.status_code == 400