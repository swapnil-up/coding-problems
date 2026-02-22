"""
PROBLEM 02: Path Parameters
============================

LEARNING OBJECTIVES:
- Use path parameters in URL routes
- Access path parameters in endpoint functions
- Return dynamic responses based on parameters

TASK:
Create an endpoint that greets a user by name using path parameters.

REQUIREMENTS:
- GET endpoint at "/greet/{name}"
- Accepts a name as a path parameter
- Returns: {"greeting": "Hello, {name}!"}
- Example: GET /greet/Alice → {"greeting": "Hello, Alice!"}

HINTS:
- Define path parameters in curly braces in the route
- Add the parameter as a function argument
- Use f-strings or format() to create the greeting
"""

from fastapi import FastAPI

app = FastAPI()

@app.get("/greet/{name}")
def greet_user(name: str):
    return {"greeting": f"Hello, {name}!"}