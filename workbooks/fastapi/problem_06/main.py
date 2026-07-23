"""
PROBLEM 06: Data Validation
============================

LEARNING OBJECTIVES:
- Use Pydantic Field for advanced validation
- Set min/max constraints on values
- Use regex patterns for string validation
- Provide custom error messages

TASK:
Create a product creation endpoint with strict validation rules.

REQUIREMENTS:
- Define Product model with validation:
  - name: string, min length 3, max length 50
  - price: float, must be positive (> 0)
  - stock: integer, must be >= 0
  - sku: string, must match pattern "^[A-Z]{3}-[0-9]{4}$" (e.g., "ABC-1234")
- POST endpoint at "/products"
- Returns the created product

EXAMPLE:
POST /products
Body: {"name": "Laptop", "price": 999.99, "stock": 10, "sku": "LAP-1001"}
→ {"name": "Laptop", "price": 999.99, "stock": 10, "sku": "LAP-1001"}

HINTS:
- from pydantic import BaseModel, Field
- Use Field(gt=0) for "greater than"
- Use Field(ge=0) for "greater than or equal"
- Use Field(min_length=..., max_length=...)
- Use Field(pattern="regex") for string patterns
"""

from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

class Product(BaseModel):
    name: str = Field(min_length=3, max_length=50)
    price: float = Field(gt=0)
    stock: int = Field(ge=0)
    sku: str= Field(pattern="^[A-Z]{3}-[0-9]{4}$")

@app.post("/products/")
def create_product(product: Product):
    return product