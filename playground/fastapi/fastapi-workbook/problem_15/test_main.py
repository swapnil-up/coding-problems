"""Tests for Problem 15: Middleware"""

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_endpoint_exists():
    """Test that test endpoint exists"""
    response = client.get("/test")
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "Middleware test"


def test_custom_header_present():
    """Test that custom header is added"""
    response = client.get("/test")
    assert "x-custom-header" in response.headers
    assert response.headers["x-custom-header"] == "FastAPI-Workbook"


def test_process_time_header_present():
    """Test that process time header is added"""
    response = client.get("/test")
    assert "x-process-time" in response.headers


def test_process_time_is_numeric():
    """Test that process time is a valid number"""
    response = client.get("/test")
    process_time = response.headers["x-process-time"]
    # Should be able to convert to float
    time_value = float(process_time)
    # Should be a reasonable value (less than 1 second for this simple endpoint)
    assert 0 <= time_value < 1


def test_headers_on_404():
    """Test that middleware works even on 404 responses"""
    response = client.get("/nonexistent")
    assert response.status_code == 404
    # Middleware should still add headers
    assert "x-custom-header" in response.headers
    assert "x-process-time" in response.headers


def test_multiple_requests():
    """Test that middleware works for multiple requests"""
    for _ in range(3):
        response = client.get("/test")
        assert "x-custom-header" in response.headers
        assert "x-process-time" in response.headers
