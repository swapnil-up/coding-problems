"""Tests for Problem 02: Path Parameters"""

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_greet_endpoint_exists():
    """Test that the greet endpoint exists"""
    response = client.get("/greet/Alice")
    assert response.status_code == 200


def test_greet_returns_correct_structure():
    """Test that response has correct structure"""
    response = client.get("/greet/Bob")
    data = response.json()
    assert "greeting" in data


def test_greet_alice():
    """Test greeting for Alice"""
    response = client.get("/greet/Alice")
    data = response.json()
    assert data["greeting"] == "Hello, Alice!"


def test_greet_bob():
    """Test greeting for Bob"""
    response = client.get("/greet/Bob")
    data = response.json()
    assert data["greeting"] == "Hello, Bob!"


def test_greet_with_special_characters():
    """Test greeting with special characters in name"""
    response = client.get("/greet/José")
    data = response.json()
    assert data["greeting"] == "Hello, José!"