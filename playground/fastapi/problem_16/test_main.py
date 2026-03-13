"""Tests for Problem 16: CORS"""

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_public_endpoint():
    """Test public endpoint returns correct data"""
    response = client.get("/public")
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "Public endpoint"


def test_data_endpoint():
    """Test data endpoint receives and returns value"""
    response = client.post("/data", json={"value": "test"})
    assert response.status_code == 200
    data = response.json()
    assert data["received"] == "test"


def test_cors_headers_on_get():
    """Test that CORS headers are present on GET request"""
    response = client.get(
        "/public",
        headers={"Origin": "http://localhost:3000"}
    )
    # Access-Control-Allow-Origin should be present
    assert "access-control-allow-origin" in response.headers


def test_cors_headers_on_post():
    """Test that CORS headers are present on POST request"""
    response = client.post(
        "/data",
        json={"value": "test"},
        headers={"Origin": "http://localhost:8080"}
    )
    assert "access-control-allow-origin" in response.headers


def test_cors_allows_credentials():
    """Test that CORS allows credentials"""
    response = client.get(
        "/public",
        headers={"Origin": "http://localhost:3000"}
    )
    # Should have allow-credentials header
    assert response.headers.get("access-control-allow-credentials") == "true"


def test_preflight_request():
    """Test CORS preflight (OPTIONS) request"""
    response = client.options(
        "/public",
        headers={
            "Origin": "http://localhost:3000",
            "Access-Control-Request-Method": "GET"
        }
    )
    # Preflight should return 200
    assert response.status_code == 200


def test_multiple_values():
    """Test POST endpoint with different values"""
    test_values = ["hello", "world", "fastapi"]
    for value in test_values:
        response = client.post("/data", json={"value": value})
        data = response.json()
        assert data["received"] == value
