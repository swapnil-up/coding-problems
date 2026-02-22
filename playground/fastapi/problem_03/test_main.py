"""Tests for Problem 03: Query Parameters"""

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_search_with_all_params():
    """Test search with all parameters provided"""
    response = client.get("/search?q=python&limit=5&skip=10")
    assert response.status_code == 200
    data = response.json()
    assert data["query"] == "python"
    assert data["limit"] == 5
    assert data["skip"] == 10
    assert data["results_count"] == 5


def test_search_with_defaults():
    """Test search with default limit and skip"""
    response = client.get("/search?q=fastapi")
    data = response.json()
    assert data["query"] == "fastapi"
    assert data["limit"] == 10
    assert data["skip"] == 0
    assert data["results_count"] == 10


def test_search_with_custom_limit():
    """Test search with custom limit, default skip"""
    response = client.get("/search?q=api&limit=20")
    data = response.json()
    assert data["query"] == "api"
    assert data["limit"] == 20
    assert data["skip"] == 0


def test_search_requires_query():
    """Test that query parameter is required"""
    response = client.get("/search")
    assert response.status_code == 422  # Validation error


def test_limit_type_validation():
    """Test that limit is validated as integer"""
    response = client.get("/search?q=test&limit=5")
    data = response.json()
    assert isinstance(data["limit"], int)