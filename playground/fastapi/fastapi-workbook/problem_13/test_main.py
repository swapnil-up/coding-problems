"""Tests for Problem 13: Status Codes and Response Types"""

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_create_item_status_code():
    """Test that creating item returns 201"""
    response = client.post("/items", json={"name": "Test Item"})
    assert response.status_code == 201


def test_create_item_returns_data():
    """Test that creating item returns correct data"""
    response = client.post("/items", json={"name": "My Item"})
    data = response.json()
    assert "id" in data
    assert data["name"] == "My Item"


def test_create_multiple_items():
    """Test creating multiple items increments ID"""
    # Reset by creating new test client
    response1 = client.post("/items", json={"name": "Item 1"})
    response2 = client.post("/items", json={"name": "Item 2"})
    
    data1 = response1.json()
    data2 = response2.json()
    
    assert data2["id"] > data1["id"]


def test_delete_existing_item():
    """Test deleting an existing item returns 204"""
    # Create an item first
    create_response = client.post("/items", json={"name": "To Delete"})
    item_id = create_response.json()["id"]
    
    # Delete it
    delete_response = client.delete(f"/items/{item_id}")
    assert delete_response.status_code == 204


def test_delete_returns_no_content():
    """Test that delete returns no content"""
    # Create an item
    create_response = client.post("/items", json={"name": "Another Item"})
    item_id = create_response.json()["id"]
    
    # Delete it
    delete_response = client.delete(f"/items/{item_id}")
    assert delete_response.content == b""


def test_delete_non_existent_item():
    """Test deleting non-existent item returns 404"""
    response = client.delete("/items/999999")
    assert response.status_code == 404


def test_cannot_delete_same_item_twice():
    """Test that deleting the same item twice fails"""
    # Create an item
    create_response = client.post("/items", json={"name": "Once Only"})
    item_id = create_response.json()["id"]
    
    # Delete it first time
    first_delete = client.delete(f"/items/{item_id}")
    assert first_delete.status_code == 204
    
    # Try to delete again
    second_delete = client.delete(f"/items/{item_id}")
    assert second_delete.status_code == 404
