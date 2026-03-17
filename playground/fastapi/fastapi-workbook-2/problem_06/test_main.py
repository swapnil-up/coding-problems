"""Tests for Problem 06: Server-Sent Events Streaming"""

from fastapi.testclient import TestClient
from main import app
import time

client = TestClient(app)


def test_count_stream():
    """Test streaming count endpoint."""
    with client.stream("GET", "/stream/count?max_count=3") as response:
        assert response.status_code == 200
        assert "text/event-stream" in response.headers["content-type"]
        
        # In streaming mode, you iterate over the response text
        content = "".join([chunk for chunk in response.iter_text()])
        assert "data: 1" in content


def test_count_stream_default():
    """Test count stream with default max_count."""
    with client.stream("GET", "/stream/count") as response:
        assert response.status_code == 200
        content = "".join(chunk for chunk in response.iter_text())
        # Should have 10 numbers by default
        assert "data: 10" in content


def test_count_stream_max_limit():
    """Test that count stream respects max limit."""
    response = client.get("/stream/count?max_count=150")
    # Should either limit to 100 or return validation error
    assert response.status_code in [200, 422]


def test_text_stream():
    """Test streaming text word by word."""
    with client.stream("GET", "/stream/text?text=hello world test") as response:
        assert response.status_code == 200
        assert "text/event-stream" in response.headers["content-type"]
        
        content = "".join(chunk for chunk in response.iter_text())
        assert "data: hello" in content
        assert "data: world" in content
        assert "data: test" in content


def test_text_stream_single_word():
    """Test streaming single word."""
    with client.stream("GET", "/stream/text?text=hello") as response:
        assert response.status_code == 200
        content = "".join(chunk for chunk in response.iter_text())
        assert "data: hello" in content


def test_text_stream_required():
    """Test that text parameter is required."""
    response = client.get("/stream/text")
    assert response.status_code == 422


def test_stream_timing():
    """Test that streaming has delays between events."""
    start = time.time()
    with client.stream("GET", "/stream/count?max_count=3") as response:
        list(response.iter_text())

    elapsed = time.time() - start
    
    # Should take at least 0.2 seconds for 3 items with 0.1s delays
    # (actual timing may vary, so use generous threshold)
    assert elapsed >= 0.2
