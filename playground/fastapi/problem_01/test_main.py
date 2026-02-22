"""Tests for Problem 01: Hello FastAPI"""

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_root_endpoint_exists():
    """Test that the root endpoint exists"""
    response = client.get("/")
    assert response.status_code == 200


def test_root_returns_json():
    """Test that the response is JSON"""
    response = client.get("/")
    assert response.headers["content-type"] == "application/json"


def test_root_returns_correct_message():
    """Test that the correct message is returned"""
    response = client.get("/")
    data = response.json()
    assert "message" in data
    assert data["message"] == "Hello, FastAPI!"


def test_app_is_fastapi_instance():
    """Test that app is a FastAPI instance"""
    from fastapi import FastAPI
    assert isinstance(app, FastAPI)