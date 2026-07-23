"""
PROBLEM 18: Custom Response Classes
====================================

LEARNING OBJECTIVES:
- Use different response classes (JSONResponse, PlainTextResponse, etc.)
- Return custom content types
- Control response formatting

TASK:
Create endpoints that return different response types.

REQUIREMENTS:
- GET endpoint at "/json"
  - Uses JSONResponse
  - Returns: {"format": "json", "data": "example"}
  - Content-Type: application/json
- GET endpoint at "/text"
  - Uses PlainTextResponse
  - Returns: "This is plain text"
  - Content-Type: text/plain
- GET endpoint at "/html"
  - Uses HTMLResponse
  - Returns: "<h1>Hello from FastAPI</h1>"
  - Content-Type: text/html

EXAMPLE:
GET /json → JSON response
GET /text → Plain text response
GET /html → HTML response

HINTS:
- from fastapi.responses import JSONResponse, PlainTextResponse, HTMLResponse
- Return: return JSONResponse(content={...})
- Or use response_class in decorator: @app.get("/text", response_class=PlainTextResponse)
"""

from fastapi import FastAPI
from fastapi.responses import JSONResponse, PlainTextResponse, HTMLResponse

app = FastAPI()

@app.get("/json", response_class=JSONResponse)
def send_json():
  return {
    "format": "json",
    "data": "example"
  }

@app.get("/text", response_class=PlainTextResponse)
def send_text():
  return "This is plain text"

@app.get("/html", response_class=HTMLResponse)
def send_html():
  return "<h1>Hello from FastAPI</h1>"
