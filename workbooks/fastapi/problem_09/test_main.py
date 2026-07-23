"""Tests for Problem 09: Dependency Injection Basics"""

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_default_pagination():
    """Test default pagination values"""
    response = client.get("/items")
    assert response.status_code == 200
    data = response.json()
    assert data["pagination"]["skip"] == 0
    assert data["pagination"]["limit"] == 10
    assert data["items"] == list(range(1, 11))


def test_custom_skip():
    """Test custom skip value"""
    response = client.get("/items?skip=5")
    data = response.json()
    assert data["pagination"]["skip"] == 5
    assert data["pagination"]["limit"] == 10
    assert data["items"] == list(range(6, 16))


def test_custom_limit():
    """Test custom limit value"""
    response = client.get("/items?limit=3")
    data = response.json()
    assert data["pagination"]["skip"] == 0
    assert data["pagination"]["limit"] == 3
    assert data["items"] == [1, 2, 3]


def test_custom_skip_and_limit():
    """Test both skip and limit"""
    response = client.get("/items?skip=10&limit=5")
    data = response.json()
    assert data["pagination"]["skip"] == 10
    assert data["pagination"]["limit"] == 5
    assert data["items"] == list(range(11, 16))


def test_limit_max_constraint():
    """Test that limit cannot exceed 100"""
    response = client.get("/items?limit=150")
    assert response.status_code == 422


def test_limit_min_constraint():
    """Test that limit must be at least 1"""
    response = client.get("/items?limit=0")
    assert response.status_code == 422


def test_skip_min_constraint():
    """Test that skip cannot be negative"""
    response = client.get("/items?skip=-1")
    assert response.status_code == 422


def test_edge_case_skip_large():
    """Test with large skip value"""
    response = client.get("/items?skip=1000&limit=2")
    data = response.json()
    assert data["items"] == [1001, 1002]