"""
PROBLEM 08: Nested Models
==========================

LEARNING OBJECTIVES:
- Create nested Pydantic models
- Handle complex data structures
- Validate nested data

TASK:
Create an order system with nested models for items and addresses.

REQUIREMENTS:
- Define Address model: street (str), city (str), zip_code (str)
- Define OrderItem model: product_name (str), quantity (int, min=1), price (float, min=0)
- Define Order model:
  - order_id (str)
  - items (list of OrderItem)
  - shipping_address (Address)
  - total (float) - calculated from items
- POST endpoint at "/orders"
- Calculate total as sum of (quantity * price) for all items
- Return the complete order

EXAMPLE:
POST /orders
Body: {
  "order_id": "ORD-001",
  "items": [
    {"product_name": "Laptop", "quantity": 1, "price": 999.99},
    {"product_name": "Mouse", "quantity": 2, "price": 25.00}
  ],
  "shipping_address": {
    "street": "123 Main St",
    "city": "San Francisco",
    "zip_code": "94102"
  }
}
→ Returns order with total: 1049.99

HINTS:
- Define models in order: Address, OrderItem, then Order
- Use List[OrderItem] from typing for the items field
- Calculate total in the endpoint function
- You can modify the order object before returning it
"""

from fastapi import FastAPI
from pydantic import BaseModel, Field, computed_field
from typing import List

app = FastAPI()

class Address(BaseModel):
    street: str
    city: str
    zip_code: str

class OrderItem(BaseModel):
    product_name: str
    quantity: int = Field(ge=1)
    price: float = Field(ge=0)

class Order(BaseModel):
    order_id: str
    items: List[OrderItem]
    shipping_address: Address
    @computed_field
    @property
    def total(self) -> float:
        return sum(item.price*item.quantity for item in self.items)

@app.post("/orders/")
def create_order(order: Order):
    return order