"""Tests for Problem 07: Multiple Parameter Types"""

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_update_with_all_parameters():
    """Test update with path, query, and body parameters"""
    response = client.put(
        "/users/123/profile?notify=true",
        json={"bio": "FastAPI developer", "website": "https://example.com"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["user_id"] == 123
    assert data["updated"]["bio"] == "FastAPI developer"
    assert data["updated"]["website"] == "https://example.com"
    assert data["notification_sent"] is True


def test_update_without_notify():
    """Test that notify defaults to False"""
    response = client.put(
        "/users/456/profile",
        json={"bio": "Python enthusiast"}
    )
    data = response.json()
    assert data["user_id"] == 456
    assert data["notification_sent"] is False


def test_update_with_only_bio():
    """Test updating only bio field"""
    response = client.put(
        "/users/789/profile",
        json={"bio": "New bio"}
    )
    data = response.json()
    assert data["updated"]["bio"] == "New bio"
    assert "website" in data["updated"]


def test_update_with_only_website():
    """Test updating only website field"""
    response = client.put(
        "/users/111/profile",
        json={"website": "https://newsite.com"}
    )
    data = response.json()
    assert data["updated"]["website"] == "https://newsite.com"
    assert "bio" in data["updated"]


def test_different_user_ids():
    """Test that different user IDs are handled correctly"""
    for user_id in [1, 42, 999]:
        response = client.put(
            f"/users/{user_id}/profile",
            json={"bio": "Test"}
        )
        data = response.json()
        assert data["user_id"] == user_id


def test_notify_true():
    """Test notify=true"""
    response = client.put(
        "/users/1/profile?notify=true",
        json={"bio": "Test"}
    )
    data = response.json()
    assert data["notification_sent"] is True


def test_notify_false():
    """Test notify=false"""
    response = client.put(
        "/users/1/profile?notify=false",
        json={"bio": "Test"}
    )
    data = response.json()
    assert data["notification_sent"] is False