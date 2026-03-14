"""Tests for Problem 08: Nested Models"""

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_create_order_single_item():
    """Test creating an order with a single item"""
    response = client.post(
        "/orders",
        json={
            "order_id": "ORD-001",
            "items": [
                {"product_name": "Laptop", "quantity": 1, "price": 999.99}
            ],
            "shipping_address": {
                "street": "123 Main St",
                "city": "San Francisco",
                "zip_code": "94102"
            }
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert data["order_id"] == "ORD-001"
    assert data["total"] == 999.99


def test_create_order_multiple_items():
    """Test creating an order with multiple items"""
    response = client.post(
        "/orders",
        json={
            "order_id": "ORD-002",
            "items": [
                {"product_name": "Laptop", "quantity": 1, "price": 999.99},
                {"product_name": "Mouse", "quantity": 2, "price": 25.00}
            ],
            "shipping_address": {
                "street": "456 Oak Ave",
                "city": "New York",
                "zip_code": "10001"
            }
        }
    )
    data = response.json()
    assert data["total"] == 1049.99  # 999.99 + (2 * 25.00)


def test_total_calculation():
    """Test that total is correctly calculated"""
    response = client.post(
        "/orders",
        json={
            "order_id": "ORD-003",
            "items": [
                {"product_name": "Book", "quantity": 3, "price": 15.99},
                {"product_name": "Pen", "quantity": 5, "price": 2.50},
                {"product_name": "Notebook", "quantity": 2, "price": 8.00}
            ],
            "shipping_address": {
                "street": "789 Pine Rd",
                "city": "Austin",
                "zip_code": "78701"
            }
        }
    )
    data = response.json()
    expected_total = (3 * 15.99) + (5 * 2.50) + (2 * 8.00)
    assert abs(data["total"] - expected_total) < 0.01


def test_shipping_address_preserved():
    """Test that shipping address is preserved in response"""
    response = client.post(
        "/orders",
        json={
            "order_id": "ORD-004",
            "items": [
                {"product_name": "Test", "quantity": 1, "price": 10.00}
            ],
            "shipping_address": {
                "street": "999 Test Blvd",
                "city": "Seattle",
                "zip_code": "98101"
            }
        }
    )
    data = response.json()
    assert data["shipping_address"]["street"] == "999 Test Blvd"
    assert data["shipping_address"]["city"] == "Seattle"
    assert data["shipping_address"]["zip_code"] == "98101"


def test_items_preserved():
    """Test that items are preserved in response"""
    response = client.post(
        "/orders",
        json={
            "order_id": "ORD-005",
            "items": [
                {"product_name": "Widget", "quantity": 3, "price": 7.50}
            ],
            "shipping_address": {
                "street": "1 Test St",
                "city": "Boston",
                "zip_code": "02101"
            }
        }
    )
    data = response.json()
    assert len(data["items"]) == 1
    assert data["items"][0]["product_name"] == "Widget"
    assert data["items"][0]["quantity"] == 3
    assert data["items"][0]["price"] == 7.50


def test_invalid_quantity():
    """Test that quantity less than 1 is rejected"""
    response = client.post(
        "/orders",
        json={
            "order_id": "ORD-006",
            "items": [
                {"product_name": "Test", "quantity": 0, "price": 10.00}
            ],
            "shipping_address": {
                "street": "1 St",
                "city": "City",
                "zip_code": "00000"
            }
        }
    )
    assert response.status_code == 422


def test_negative_price():
    """Test that negative price is rejected"""
    response = client.post(
        "/orders",
        json={
            "order_id": "ORD-007",
            "items": [
                {"product_name": "Test", "quantity": 1, "price": -10.00}
            ],
            "shipping_address": {
                "street": "1 St",
                "city": "City",
                "zip_code": "00000"
            }
        }
    )
    assert response.status_code == 422