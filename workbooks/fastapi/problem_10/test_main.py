"""Tests for Problem 10: Class-Based Dependencies"""

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_admin_endpoint():
    """Test admin endpoint with token"""
    response = client.get("/admin?token=admin_token_123")
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "Access granted"
    assert data["auth"]["token"] == "admin_token_123"
    assert data["auth"]["role"] == "admin"
    assert data["auth"]["valid"] is True


def test_user_endpoint():
    """Test user endpoint with token"""
    response = client.get("/user?token=user_token_456")
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "Access granted"
    assert data["auth"]["token"] == "user_token_456"
    assert data["auth"]["role"] == "user"
    assert data["auth"]["valid"] is True


def test_admin_requires_token():
    """Test that admin endpoint requires token"""
    response = client.get("/admin")
    assert response.status_code == 422


def test_user_requires_token():
    """Test that user endpoint requires token"""
    response = client.get("/user")
    assert response.status_code == 422


def test_different_tokens_admin():
    """Test admin endpoint with different tokens"""
    tokens = ["token1", "xyz789", "secret_key"]
    for token in tokens:
        response = client.get(f"/admin?token={token}")
        data = response.json()
        assert data["auth"]["token"] == token
        assert data["auth"]["role"] == "admin"


def test_different_tokens_user():
    """Test user endpoint with different tokens"""
    tokens = ["user_a", "user_b", "test123"]
    for token in tokens:
        response = client.get(f"/user?token={token}")
        data = response.json()
        assert data["auth"]["token"] == token
        assert data["auth"]["role"] == "user"