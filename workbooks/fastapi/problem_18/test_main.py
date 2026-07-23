"""Tests for Problem 18: Custom Response Classes"""

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_json_endpoint_exists():
    """Test JSON endpoint exists and returns 200"""
    response = client.get("/json")
    assert response.status_code == 200


def test_json_content_type():
    """Test JSON endpoint returns correct content type"""
    response = client.get("/json")
    assert "application/json" in response.headers["content-type"]


def test_json_content():
    """Test JSON endpoint returns correct content"""
    response = client.get("/json")
    data = response.json()
    assert data["format"] == "json"
    assert data["data"] == "example"


def test_text_endpoint_exists():
    """Test text endpoint exists and returns 200"""
    response = client.get("/text")
    assert response.status_code == 200


def test_text_content_type():
    """Test text endpoint returns correct content type"""
    response = client.get("/text")
    assert "text/plain" in response.headers["content-type"]


def test_text_content():
    """Test text endpoint returns correct content"""
    response = client.get("/text")
    assert response.text == "This is plain text"


def test_html_endpoint_exists():
    """Test HTML endpoint exists and returns 200"""
    response = client.get("/html")
    assert response.status_code == 200


def test_html_content_type():
    """Test HTML endpoint returns correct content type"""
    response = client.get("/html")
    assert "text/html" in response.headers["content-type"]


def test_html_content():
    """Test HTML endpoint returns correct content"""
    response = client.get("/html")
    assert response.text == "<h1>Hello from FastAPI</h1>"


def test_all_endpoints_return_different_types():
    """Test that all three endpoints return different content types"""
    json_response = client.get("/json")
    text_response = client.get("/text")
    html_response = client.get("/html")
    
    json_type = json_response.headers["content-type"]
    text_type = text_response.headers["content-type"]
    html_type = html_response.headers["content-type"]
    
    # All should be different
    assert json_type != text_type
    assert text_type != html_type
    assert json_type != html_type
