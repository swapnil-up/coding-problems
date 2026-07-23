"""Tests for Problem 19: Custom Validators"""

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_valid_signup():
    """Test valid signup data"""
    response = client.post(
        "/signup",
        json={
            "username": "johndoe",
            "password": "SecurePass123",
            "email": "john@example.com",
            "age": 25
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "Signup successful"
    assert data["username"] == "johndoe"


def test_username_too_short():
    """Test that short usernames are rejected"""
    response = client.post(
        "/signup",
        json={
            "username": "ab",
            "password": "SecurePass123",
            "email": "test@example.com",
            "age": 25
        }
    )
    assert response.status_code == 422


def test_username_too_long():
    """Test that long usernames are rejected"""
    response = client.post(
        "/signup",
        json={
            "username": "a" * 21,
            "password": "SecurePass123",
            "email": "test@example.com",
            "age": 25
        }
    )
    assert response.status_code == 422


def test_username_with_special_chars():
    """Test that usernames with special characters are rejected"""
    invalid_usernames = ["user@name", "user name", "user-name", "user.name"]
    for username in invalid_usernames:
        response = client.post(
            "/signup",
            json={
                "username": username,
                "password": "SecurePass123",
                "email": "test@example.com",
                "age": 25
            }
        )
        assert response.status_code == 422, f"Username '{username}' should be invalid"


def test_password_no_uppercase():
    """Test that password without uppercase is rejected"""
    response = client.post(
        "/signup",
        json={
            "username": "johndoe",
            "password": "securepass123",
            "email": "test@example.com",
            "age": 25
        }
    )
    assert response.status_code == 422


def test_password_no_lowercase():
    """Test that password without lowercase is rejected"""
    response = client.post(
        "/signup",
        json={
            "username": "johndoe",
            "password": "SECUREPASS123",
            "email": "test@example.com",
            "age": 25
        }
    )
    assert response.status_code == 422


def test_password_no_digit():
    """Test that password without digit is rejected"""
    response = client.post(
        "/signup",
        json={
            "username": "johndoe",
            "password": "SecurePassword",
            "email": "test@example.com",
            "age": 25
        }
    )
    assert response.status_code == 422


def test_password_too_short():
    """Test that short password is rejected"""
    response = client.post(
        "/signup",
        json={
            "username": "johndoe",
            "password": "Pass1",
            "email": "test@example.com",
            "age": 25
        }
    )
    assert response.status_code == 422


def test_age_too_young():
    """Test that age under 13 is rejected"""
    response = client.post(
        "/signup",
        json={
            "username": "johndoe",
            "password": "SecurePass123",
            "email": "test@example.com",
            "age": 12
        }
    )
    assert response.status_code == 422


def test_age_too_old():
    """Test that age over 120 is rejected"""
    response = client.post(
        "/signup",
        json={
            "username": "johndoe",
            "password": "SecurePass123",
            "email": "test@example.com",
            "age": 121
        }
    )
    assert response.status_code == 422


def test_valid_edge_cases():
    """Test valid edge case values"""
    # Minimum valid age
    response = client.post(
        "/signup",
        json={
            "username": "user13",
            "password": "ValidPass1",
            "email": "test@example.com",
            "age": 13
        }
    )
    assert response.status_code == 200
    
    # Maximum valid age
    response = client.post(
        "/signup",
        json={
            "username": "user120",
            "password": "ValidPass1",
            "email": "test2@example.com",
            "age": 120
        }
    )
    assert response.status_code == 200
