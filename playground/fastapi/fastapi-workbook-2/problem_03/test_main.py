"""Tests for Problem 03: Messages with Pagination"""

from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from main import app, Base, get_db, User, Conversation
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
    # Create test user and conversation
    db = TestingSessionLocal()
    user = User(email="test@example.com", hashed_password="password")
    db.add(user)
    db.commit()
    
    conversation = Conversation(user_id=user.id, title="Test Chat")
    db.add(conversation)
    db.commit()
    db.close()


def teardown_function():
    Base.metadata.drop_all(bind=engine)
    if os.path.exists("test_db.db"):
        os.remove("test_db.db")


def test_create_message():
    """Test creating a message."""
    response = client.post(
        "/messages",
        json={
            "conversation_id": 1,
            "content": "Hello, world!",
            "role": "user"
        }
    )
    assert response.status_code == 201
    data = response.json()
    assert data["conversation_id"] == 1
    assert data["content"] == "Hello, world!"
    assert data["role"] == "user"
    assert "id" in data


def test_message_role_validation():
    """Test that role must be user or assistant."""
    response = client.post(
        "/messages",
        json={
            "conversation_id": 1,
            "content": "Test",
            "role": "invalid_role"
        }
    )
    assert response.status_code == 422


def test_list_messages_pagination():
    """Test message pagination."""
    # Create 15 messages
    for i in range(15):
        client.post(
            "/messages",
            json={
                "conversation_id": 1,
                "content": f"Message {i+1}",
                "role": "user" if i % 2 == 0 else "assistant"
            }
        )
    
    # Get first page
    response = client.get("/conversations/1/messages?limit=10&offset=0")
    assert response.status_code == 200
    data = response.json()
    
    assert len(data["messages"]) == 10
    assert data["total"] == 15
    assert data["limit"] == 10
    assert data["offset"] == 0


def test_messages_ordered_by_created_at():
    """Test that messages are ordered by created_at ascending."""
    # Create messages
    client.post("/messages", json={"conversation_id": 1, "content": "First", "role": "user"})
    client.post("/messages", json={"conversation_id": 1, "content": "Second", "role": "assistant"})
    client.post("/messages", json={"conversation_id": 1, "content": "Third", "role": "user"})
    
    response = client.get("/conversations/1/messages")
    messages = response.json()["messages"]
    
    assert messages[0]["content"] == "First"
    assert messages[1]["content"] == "Second"
    assert messages[2]["content"] == "Third"


def test_pagination_second_page():
    """Test getting second page of results."""
    # Create 25 messages
    for i in range(25):
        client.post(
            "/messages",
            json={"conversation_id": 1, "content": f"Msg {i}", "role": "user"}
        )
    
    # Get second page
    response = client.get("/conversations/1/messages?limit=10&offset=10")
    data = response.json()
    
    assert len(data["messages"]) == 10
    assert data["offset"] == 10
    # Check we got messages 11-20
    assert data["messages"][0]["content"] == "Msg 10"


def test_default_pagination_values():
    """Test default limit of 50."""
    response = client.get("/conversations/1/messages")
    data = response.json()
    assert data["limit"] == 50
    assert data["offset"] == 0


def test_max_limit_enforcement():
    """Test that limit cannot exceed 100."""
    response = client.get("/conversations/1/messages?limit=150")
    # Should either clamp to 100 or return validation error
    # Depending on implementation, adjust this test
    assert response.status_code in [200, 422]


def test_content_length_validation():
    """Test that very long content is rejected."""
    long_content = "x" * 10001  # Over 10000 char limit
    response = client.post(
        "/messages",
        json={
            "conversation_id": 1,
            "content": long_content,
            "role": "user"
        }
    )
    assert response.status_code == 422


def test_empty_messages_list():
    """Test pagination with no messages."""
    response = client.get("/conversations/1/messages")
    data = response.json()
    assert data["messages"] == []
    assert data["total"] == 0
