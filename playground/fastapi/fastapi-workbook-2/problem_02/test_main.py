"""Tests for Problem 02: Conversation CRUD Operations"""

from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from main import app, Base, get_db, User
import os

TEST_DATABASE_URL = "sqlite:///./test_db.db"
engine = create_engine(TEST_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db
client = TestClient(app)


def setup_function():
    Base.metadata.create_all(bind=engine)
    # Create a test user
    db = TestingSessionLocal()
    user = User(email="test@example.com", hashed_password="password")
    db.add(user)
    db.commit()
    db.close()


def teardown_function():
    Base.metadata.drop_all(bind=engine)
    if os.path.exists("test_db.db"):
        os.remove("test_db.db")


def test_create_conversation():
    """Test creating a conversation."""
    response = client.post(
        "/conversations",
        json={"user_id": 1, "title": "My First Chat"}
    )
    assert response.status_code == 201
    data = response.json()
    assert data["user_id"] == 1
    assert data["title"] == "My First Chat"
    assert "id" in data
    assert "created_at" in data


def test_list_conversations_empty():
    """Test listing conversations when none exist."""
    response = client.get("/conversations")
    assert response.status_code == 200
    assert response.json() == []


def test_list_conversations():
    """Test listing all conversations."""
    # Create a few conversations
    client.post("/conversations", json={"user_id": 1, "title": "Chat 1"})
    client.post("/conversations", json={"user_id": 1, "title": "Chat 2"})
    
    response = client.get("/conversations")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2
    assert data[0]["title"] == "Chat 1"
    assert data[1]["title"] == "Chat 2"


def test_list_conversations_filter_by_user():
    """Test filtering conversations by user_id."""
    # Create another user
    db = TestingSessionLocal()
    user2 = User(email="user2@example.com", hashed_password="pass")
    db.add(user2)
    db.commit()
    user2_id = user2.id
    db.close()
    
    # Create conversations for different users
    client.post("/conversations", json={"user_id": 1, "title": "User 1 Chat"})
    client.post("/conversations", json={"user_id": user2_id, "title": "User 2 Chat"})
    
    # Filter by user 1
    response = client.get(f"/conversations?user_id=1")
    data = response.json()
    assert len(data) == 1
    assert data[0]["user_id"] == 1


def test_get_conversation_by_id():
    """Test getting a specific conversation."""
    # Create conversation
    create_response = client.post(
        "/conversations",
        json={"user_id": 1, "title": "Specific Chat"}
    )
    conversation_id = create_response.json()["id"]
    
    # Get it
    response = client.get(f"/conversations/{conversation_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == conversation_id
    assert data["title"] == "Specific Chat"


def test_get_nonexistent_conversation():
    """Test getting a conversation that doesn't exist."""
    response = client.get("/conversations/99999")
    assert response.status_code == 404


def test_update_conversation():
    """Test updating a conversation title."""
    # Create conversation
    create_response = client.post(
        "/conversations",
        json={"user_id": 1, "title": "Old Title"}
    )
    conversation_id = create_response.json()["id"]
    
    # Update it
    response = client.put(
        f"/conversations/{conversation_id}",
        json={"title": "New Title"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "New Title"
    assert data["id"] == conversation_id
    
    # Verify update persisted
    get_response = client.get(f"/conversations/{conversation_id}")
    assert get_response.json()["title"] == "New Title"


def test_update_nonexistent_conversation():
    """Test updating a conversation that doesn't exist."""
    response = client.put(
        "/conversations/99999",
        json={"title": "New Title"}
    )
    assert response.status_code == 404


def test_delete_conversation():
    """Test deleting a conversation."""
    # Create conversation
    create_response = client.post(
        "/conversations",
        json={"user_id": 1, "title": "To Delete"}
    )
    conversation_id = create_response.json()["id"]
    
    # Delete it
    response = client.delete(f"/conversations/{conversation_id}")
    assert response.status_code == 204
    
    # Verify it's gone
    get_response = client.get(f"/conversations/{conversation_id}")
    assert get_response.status_code == 404


def test_delete_nonexistent_conversation():
    """Test deleting a conversation that doesn't exist."""
    response = client.delete("/conversations/99999")
    assert response.status_code == 404


def test_multiple_conversations_for_same_user():
    """Test that one user can have multiple conversations."""
    client.post("/conversations", json={"user_id": 1, "title": "Chat 1"})
    client.post("/conversations", json={"user_id": 1, "title": "Chat 2"})
    client.post("/conversations", json={"user_id": 1, "title": "Chat 3"})
    
    response = client.get("/conversations?user_id=1")
    assert len(response.json()) == 3
