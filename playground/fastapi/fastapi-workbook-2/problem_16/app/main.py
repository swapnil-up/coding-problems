"""
Main FastAPI application.
Combines all routers and configures the app.
"""

from fastapi import FastAPI
from .database import engine, Base
from .routers import users, conversations

# TODO: Create FastAPI app instance
app = FastAPI(title="Chatbot API", version="1.0.0")

# TODO: Include routers
# app.include_router(users.router)
# app.include_router(conversations.router)

# TODO: Add startup event to create tables
@app.on_event("startup")
def startup():
    # Create all tables
    # Base.metadata.create_all(bind=engine)
    pass

@app.get("/")
def root():
    """Health check endpoint."""
    return {"status": "ok", "message": "Chatbot API is running"}
