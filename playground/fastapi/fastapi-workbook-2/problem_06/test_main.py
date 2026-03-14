"""Tests for Problem 06: Server-Sent Events Streaming"""

from fastapi.testclient import TestClient
from main import app
import time

client = TestClient(app)


def test_count_stream():
    """Test streaming count endpoint."""
    response = client.get("/stream/count?max_count=3", stream=True)
    assert response.status_code == 200
    assert "text/event-stream" in response.headers["content-type"]
    
    # Read streamed data
    content = response.text
    assert "data: 1" in content
    assert "data: 2" in content
    assert "data: 3" in content


def test_count_stream_default():
    """Test count stream with default max_count."""
    response = client.get("/stream/count", stream=True)
    assert response.status_code == 200
    content = response.text
    # Should have 10 numbers by default
    assert "data: 10" in content


def test_count_stream_max_limit():
    """Test that count stream respects max limit."""
    response = client.get("/stream/count?max_count=150")
    # Should either limit to 100 or return validation error
    assert response.status_code in [200, 422]


def test_text_stream():
    """Test streaming text word by word."""
    response = client.get("/stream/text?text=hello world test", stream=True)
    assert response.status_code == 200
    assert "text/event-stream" in response.headers["content-type"]
    
    content = response.text
    assert "data: hello" in content
    assert "data: world" in content
    assert "data: test" in content


def test_text_stream_single_word():
    """Test streaming single word."""
    response = client.get("/stream/text?text=hello", stream=True)
    assert response.status_code == 200
    content = response.text
    assert "data: hello" in content


def test_text_stream_required():
    """Test that text parameter is required."""
    response = client.get("/stream/text")
    assert response.status_code == 422


def test_stream_timing():
    """Test that streaming has delays between events."""
    start = time.time()
    response = client.get("/stream/count?max_count=3", stream=True)
    elapsed = time.time() - start
    
    # Should take at least 0.2 seconds for 3 items with 0.1s delays
    # (actual timing may vary, so use generous threshold)
    assert elapsed >= 0.2
