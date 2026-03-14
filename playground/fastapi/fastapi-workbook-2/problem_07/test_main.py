"""Tests for Problem 07: LLM-Style Token Streaming"""

from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from main import app, Base, get_db, User, Conversation
import json
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


def test_chat_stream_response():
    """Test that chat stream returns SSE events."""
    response = client.post(
        "/chat/stream",
        json={"conversation_id": 1, "message": "hello"},
        stream=True
    )
    assert response.status_code == 200
    assert "text/event-stream" in response.headers["content-type"]


def test_chat_stream_content():
    """Test that stream contains tokens and done event."""
    response = client.post(
        "/chat/stream",
        json={"conversation_id": 1, "message": "hello"},
        stream=True
    )
    
    content = response.text
    # Should contain token events
    assert "data:" in content
    assert '"done": false' in content
    # Should contain final done event
    assert '"done": true' in content
    assert "message_id" in content


def test_chat_stream_saves_messages():
    """Test that both user and assistant messages are saved."""
    from main import Message
    
    response = client.post(
        "/chat/stream",
        json={"conversation_id": 1, "message": "hello"},
        stream=True
    )
    
    # Consume the stream
    _ = response.text
    
    # Check messages in database
    db = TestingSessionLocal()
    messages = db.query(Message).filter(Message.conversation_id == 1).all()
    db.close()
    
    assert len(messages) == 2  # User message + assistant message
    assert messages[0].role == "user"
    assert messages[0].content == "hello"
    assert messages[1].role == "assistant"


def test_chat_stream_different_responses():
    """Test that different inputs get different simulated responses."""
    # Test hello response
    response1 = client.post(
        "/chat/stream",
        json={"conversation_id": 1, "message": "hello"},
        stream=True
    )
    content1 = response1.text
    
    # Test weather response
    response2 = client.post(
        "/chat/stream",
        json={"conversation_id": 1, "message": "what's the weather"},
        stream=True
    )
    content2 = response2.text
    
    # Responses should be different
    assert content1 != content2


def test_chat_stream_returns_message_id():
    """Test that final event includes message_id."""
    response = client.post(
        "/chat/stream",
        json={"conversation_id": 1, "message": "test"},
        stream=True
    )
    
    content = response.text
    # Parse last event to get message_id
    assert "message_id" in content
