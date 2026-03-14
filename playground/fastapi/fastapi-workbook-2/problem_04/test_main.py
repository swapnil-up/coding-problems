"""Tests for Problem 04: Alembic Migrations"""

from fastapi.testclient import TestClient
from main import app
import os
import subprocess

client = TestClient(app)


def test_alembic_initialized():
    """Test that Alembic has been initialized."""
    assert os.path.exists("alembic"), "Alembic not initialized. Run: alembic init alembic"
    assert os.path.exists("alembic.ini"), "alembic.ini not found"
    assert os.path.exists("alembic/env.py"), "alembic/env.py not found"


def test_alembic_versions_directory():
    """Test that versions directory exists."""
    assert os.path.exists("alembic/versions"), "alembic/versions directory not found"


def test_migration_files_exist():
    """Test that at least one migration file exists."""
    versions_dir = "alembic/versions"
    if os.path.exists(versions_dir):
        files = [f for f in os.listdir(versions_dir) if f.endswith('.py')]
        assert len(files) > 0, "No migration files found. Run: alembic revision --autogenerate -m 'add bio'"


def test_user_bio_field_in_model():
    """Test that User model has bio field."""
    from main import User
    assert hasattr(User, 'bio'), "User model missing 'bio' field. Add it to the model."


def test_create_user_with_bio():
    """Test creating user with bio field."""
    response = client.post(
        "/users",
        json={
            "email": "test@example.com",
            "password": "password123",
            "bio": "I love Python!"
        }
    )
    assert response.status_code == 201
    data = response.json()
    assert data["bio"] == "I love Python!"


def test_create_user_without_bio():
    """Test that bio is optional."""
    response = client.post(
        "/users",
        json={
            "email": "test2@example.com",
            "password": "password123"
        }
    )
    assert response.status_code == 201
    data = response.json()
    assert data["bio"] is None


def test_get_user_returns_bio():
    """Test that getting user returns bio field."""
    # Create user with bio
    create_response = client.post(
        "/users",
        json={
            "email": "test3@example.com",
            "password": "password123",
            "bio": "Test bio"
        }
    )
    user_id = create_response.json()["id"]
    
    # Get user
    get_response = client.get(f"/users/{user_id}")
    assert get_response.status_code == 200
    data = get_response.json()
    assert "bio" in data
    assert data["bio"] == "Test bio"


def test_alembic_current():
    """Test that Alembic is at head revision."""
    try:
        result = subprocess.run(
            ["alembic", "current"],
            capture_output=True,
            text=True
        )
        # Should not error out
        assert result.returncode == 0, "Alembic current command failed"
    except FileNotFoundError:
        # Alembic not in PATH, skip this test
        pass


# Instructions for completing this problem:
"""
1. Run: alembic init alembic
2. Edit alembic/env.py:
   - Add: from main import Base
   - Set: target_metadata = Base.metadata
3. Edit alembic.ini:
   - Set: sqlalchemy.url = sqlite:///./test.db
4. Uncomment the bio field in User model (main.py)
5. Run: alembic revision --autogenerate -m "add user bio field"
6. Review the generated migration in alembic/versions/
7. Run: alembic upgrade head
8. Run tests: pytest test_main.py -v
"""
