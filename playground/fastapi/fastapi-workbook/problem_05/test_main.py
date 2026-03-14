"""Tests for Problem 05: Response Models"""

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_register_user():
    """Test user registration"""
    response = client.post(
        "/register",
        json={
            "username": "alice",
            "email": "alice@example.com",
            "password": "secret123"
        }
    )
    assert response.status_code == 200


def test_password_not_in_response():
    """Test that password is excluded from response"""
    response = client.post(
        "/register",
        json={
            "username": "bob",
            "email": "bob@example.com",
            "password": "topsecret"
        }
    )
    data = response.json()
    assert "password" not in data


def test_username_in_response():
    """Test that username is in response"""
    response = client.post(
        "/register",
        json={
            "username": "charlie",
            "email": "charlie@example.com",
            "password": "pass123"
        }
    )
    data = response.json()
    assert data["username"] == "charlie"


def test_email_in_response():
    """Test that email is in response"""
    response = client.post(
        "/register",
        json={
            "username": "diana",
            "email": "diana@example.com",
            "password": "password"
        }
    )
    data = response.json()
    assert data["email"] == "diana@example.com"


def test_response_has_only_username_and_email():
    """Test that response contains only username and email"""
    response = client.post(
        "/register",
        json={
            "username": "eve",
            "email": "eve@example.com",
            "password": "secret"
        }
    )
    data = response.json()
    assert set(data.keys()) == {"username", "email"}