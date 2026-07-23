"""Tests for Problem 14: Background Tasks"""

from fastapi.testclient import TestClient
from main import app, sent_emails
import time

client = TestClient(app)


def setup_function():
    """Clear sent emails before each test"""
    sent_emails.clear()


def test_send_notification_queues_task():
    """Test that sending notification queues the task"""
    response = client.post(
        "/send-notification",
        json={"email": "test@example.com", "message": "Hello"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "notification queued"


def test_background_task_executes():
    """Test that background task actually executes"""
    client.post(
        "/send-notification",
        json={"email": "alice@example.com", "message": "Test message"}
    )
    
    # Small delay to let background task complete
    time.sleep(0.1)
    
    # Check sent emails
    response = client.get("/sent-emails")
    emails = response.json()
    assert len(emails) == 1
    assert emails[0]["email"] == "alice@example.com"
    assert emails[0]["message"] == "Test message"


def test_multiple_notifications():
    """Test sending multiple notifications"""
    notifications = [
        {"email": "user1@example.com", "message": "Message 1"},
        {"email": "user2@example.com", "message": "Message 2"},
        {"email": "user3@example.com", "message": "Message 3"}
    ]
    
    for notif in notifications:
        client.post("/send-notification", json=notif)
    
    time.sleep(0.2)
    
    response = client.get("/sent-emails")
    emails = response.json()
    assert len(emails) == 3


def test_endpoint_returns_immediately():
    """Test that endpoint returns before email is 'sent'"""
    start = time.time()
    response = client.post(
        "/send-notification",
        json={"email": "quick@example.com", "message": "Fast"}
    )
    elapsed = time.time() - start
    
    # Should return very quickly (< 0.05 seconds)
    # Background task doesn't block the response
    assert elapsed < 0.05
    assert response.status_code == 200


def test_get_sent_emails_initially_empty():
    """Test that sent emails starts empty"""
    response = client.get("/sent-emails")
    assert response.status_code == 200
    emails = response.json()
    assert isinstance(emails, list)
    assert len(emails) == 0
