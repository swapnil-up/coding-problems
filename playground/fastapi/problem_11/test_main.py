"""Tests for Problem 11: Async Endpoints"""

from fastapi.testclient import TestClient
from main import app
import time

client = TestClient(app)


def test_slow_task_response():
    """Test slow task returns correct response"""
    response = client.get("/slow-task")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "completed"
    assert data["duration"] == 0.1


def test_slow_task_actually_waits():
    """Test that slow task actually waits"""
    start = time.time()
    response = client.get("/slow-task")
    elapsed = time.time() - start
    assert elapsed >= 0.1  # Should take at least 0.1 seconds
    assert response.status_code == 200


def test_parallel_tasks_default():
    """Test parallel tasks with default count"""
    response = client.get("/parallel-tasks")
    assert response.status_code == 200
    data = response.json()
    assert data["tasks_completed"] == 3
    assert "time_saved" in data


def test_parallel_tasks_custom_count():
    """Test parallel tasks with custom count"""
    response = client.get("/parallel-tasks?count=5")
    data = response.json()
    assert data["tasks_completed"] == 5


def test_parallel_tasks_runs_in_parallel():
    """Test that parallel tasks actually run in parallel"""
    # If 5 tasks run sequentially, they'd take 0.5 seconds
    # If parallel, should take ~0.1 seconds
    start = time.time()
    response = client.get("/parallel-tasks?count=5")
    elapsed = time.time() - start
    # Should NOT take 0.5 seconds (5 * 0.1)
    # Should take roughly 0.1 seconds (with some overhead)
    assert elapsed < 0.3  # Much less than sequential would take
    assert response.status_code == 200


def test_parallel_tasks_max_count():
    """Test parallel tasks respects max count"""
    response = client.get("/parallel-tasks?count=15")
    assert response.status_code == 422  # Exceeds max


def test_parallel_tasks_single():
    """Test parallel tasks with count=1"""
    response = client.get("/parallel-tasks?count=1")
    data = response.json()
    assert data["tasks_completed"] == 1