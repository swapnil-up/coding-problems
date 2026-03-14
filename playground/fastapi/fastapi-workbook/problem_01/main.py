"""
PROBLEM 01: Hello FastAPI
==========================

LEARNING OBJECTIVES:
- Create a FastAPI application instance
- Define a basic GET endpoint
- Return JSON responses

TASK:
Fix the code below to create a working FastAPI app that returns
a JSON response with a greeting message.

REQUIREMENTS:
- GET endpoint at root path "/"
- Returns: {"message": "Hello, FastAPI!"}

HINTS:
- Import FastAPI from fastapi
- Create an app instance
- Use the @app.get() decorator
- Return a dictionary (FastAPI converts it to JSON automatically)
"""

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return {"message": "Hello, FastAPI!"}