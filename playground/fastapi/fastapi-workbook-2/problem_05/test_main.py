"""Tests for Problem 05: Transactions and Error Handling"""

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
    # Create test user
    db = TestingSessionLocal()
    user = User(email="test@example.com", hashed_password="password")
    db.add(user)
    db.commit()
    db.close()


def teardown_function():
    Base.metadata.drop_all(bind=engine)
    if os.path.exists("test_db.db"):
        os.remove("test_db.db")


def test_batch_create_conversations_success():
    """Test creating multiple conversations successfully."""
    response = client.post(
        "/conversations/batch",
        json={
            "user_id": 1,
            "titles": ["Chat 1", "Chat 2", "Chat 3"]
        }
    )
    assert response.status_code == 201
    data = response.json()
    assert len(data) == 3
    assert data[0]["title"] == "Chat 1"
    assert data[1]["title"] == "Chat 2"
    assert data[2]["title"] == "Chat 3"


def test_batch_create_all_or_nothing():
    """Test that if any conversation fails, none are created."""
    # First create some conversations successfully
    client.post(
        "/conversations/batch",
        json={"user_id": 1, "titles": ["Existing 1", "Existing 2"]}
    )
    
    # Count conversations before
    db = TestingSessionLocal()
    from main import Conversation
    count_before = db.query(Conversation).count()
    db.close()
    
    # Try to create batch with invalid user_id (should fail)
    response = client.post(
        "/conversations/batch",
        json={"user_id": 999, "titles": ["Should", "Not", "Exist"]}
    )
    
    # Should get error
    assert response.status_code in [400, 404, 500]
    
    # Count should be same (atomic rollback)
    db = TestingSessionLocal()
    count_after = db.query(Conversation).count()
    db.close()
    
    assert count_after == count_before, "Conversations were created despite error (not atomic)"


def test_batch_messages_success():
    """Test creating multiple messages successfully."""
    # Create conversation first
    conv_response = client.post(
        "/conversations/batch",
        json={"user_id": 1, "titles": ["Test"]}
    )
    conv_id = conv_response.json()[0]["id"]
    
    # Create batch messages
    response = client.post(
        "/messages/conversation",
        json={
            "conversation_id": conv_id,
            "messages": [
                {"content": "Hello", "role": "user"},
                {"content": "Hi there!", "role": "assistant"},
                {"content": "How are you?", "role": "user"}
            ]
        }
    )
    assert response.status_code == 201
    data = response.json()
    assert len(data) == 3


def test_batch_messages_invalid_role_rollback():
    """Test that invalid role causes full rollback."""
    # Create conversation
    conv_response = client.post(
        "/conversations/batch",
        json={"user_id": 1, "titles": ["Test"]}
    )
    conv_id = conv_response.json()[0]["id"]
    
    # Try to create messages with one invalid role
    response = client.post(
        "/messages/conversation",
        json={
            "conversation_id": conv_id,
            "messages": [
                {"content": "First", "role": "user"},
                {"content": "Invalid", "role": "system"},  # Invalid!
                {"content": "Third", "role": "user"}
            ]
        }
    )
    
    # Should fail validation
    assert response.status_code == 422
    
    # No messages should have been created
    db = TestingSessionLocal()
    from main import Message
    message_count = db.query(Message).filter(
        Message.conversation_id == conv_id
    ).count()
    db.close()
    
    assert message_count == 0, "Messages were created despite validation error"


def test_transaction_isolation():
    """Test that transactions are properly isolated."""
    response1 = client.post(
        "/conversations/batch",
        json={"user_id": 1, "titles": ["A", "B"]}
    )
    
    response2 = client.post(
        "/conversations/batch",
        json={"user_id": 1, "titles": ["C", "D"]}
    )
    
    # Both should succeed independently
    assert response1.status_code == 201
    assert response2.status_code == 201


def test_empty_batch():
    """Test handling of empty batch."""
    response = client.post(
        "/conversations/batch",
        json={"user_id": 1, "titles": []}
    )
    # Should either succeed with empty list or return validation error
    assert response.status_code in [200, 201, 422]
