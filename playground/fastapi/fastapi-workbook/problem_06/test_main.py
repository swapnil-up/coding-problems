"""Tests for Problem 06: Data Validation"""

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_valid_product():
    """Test creating a valid product"""
    response = client.post(
        "/products",
        json={
            "name": "Laptop",
            "price": 999.99,
            "stock": 10,
            "sku": "LAP-1001"
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Laptop"
    assert data["price"] == 999.99


def test_name_too_short():
    """Test that short names are rejected"""
    response = client.post(
        "/products",
        json={
            "name": "AB",  # Too short
            "price": 10.0,
            "stock": 5,
            "sku": "TST-0001"
        }
    )
    assert response.status_code == 422


def test_name_too_long():
    """Test that long names are rejected"""
    response = client.post(
        "/products",
        json={
            "name": "A" * 51,  # Too long
            "price": 10.0,
            "stock": 5,
            "sku": "TST-0001"
        }
    )
    assert response.status_code == 422


def test_negative_price():
    """Test that negative prices are rejected"""
    response = client.post(
        "/products",
        json={
            "name": "Test Product",
            "price": -10.0,
            "stock": 5,
            "sku": "TST-0001"
        }
    )
    assert response.status_code == 422


def test_zero_price():
    """Test that zero price is rejected"""
    response = client.post(
        "/products",
        json={
            "name": "Test Product",
            "price": 0.0,
            "stock": 5,
            "sku": "TST-0001"
        }
    )
    assert response.status_code == 422


def test_negative_stock():
    """Test that negative stock is rejected"""
    response = client.post(
        "/products",
        json={
            "name": "Test Product",
            "price": 10.0,
            "stock": -1,
            "sku": "TST-0001"
        }
    )
    assert response.status_code == 422


def test_zero_stock_allowed():
    """Test that zero stock is allowed"""
    response = client.post(
        "/products",
        json={
            "name": "Test Product",
            "price": 10.0,
            "stock": 0,
            "sku": "TST-0001"
        }
    )
    assert response.status_code == 200


def test_invalid_sku_format():
    """Test that invalid SKU formats are rejected"""
    invalid_skus = [
        "ABC-123",      # Not enough digits
        "AB-1234",      # Not enough letters
        "abc-1234",     # Lowercase letters
        "ABC1234",      # Missing dash
        "ABC-ABCD"      # Letters instead of numbers
    ]
    for sku in invalid_skus:
        response = client.post(
            "/products",
            json={
                "name": "Test Product",
                "price": 10.0,
                "stock": 5,
                "sku": sku
            }
        )
        assert response.status_code == 422, f"SKU {sku} should be invalid"


def test_valid_sku_format():
    """Test that valid SKU formats are accepted"""
    valid_skus = ["ABC-1234", "XYZ-9999", "TST-0001"]
    for sku in valid_skus:
        response = client.post(
            "/products",
            json={
                "name": "Test Product",
                "price": 10.0,
                "stock": 5,
                "sku": sku
            }
        )
        assert response.status_code == 200, f"SKU {sku} should be valid"