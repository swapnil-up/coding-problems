"""Tests for Problem 12: Password Hashing & Secure Registration"""

from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from main import app, Base, get_db, User, hash_password, verify_password, validate_password_strength
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


def teardown_function():
    Base.metadata.drop_all(bind=engine)
    if os.path.exists("test_db.db"):
        os.remove("test_db.db")


def test_hash_password():
    """Test that password hashing works."""
    password = "TestPassword123"
    hashed = hash_password(password)
    
    assert hashed != password
    assert len(hashed) > 20
    assert hashed.startswith("$2b$")  # bcrypt prefix


def test_verify_password_correct():
    """Test password verification with correct password."""
    password = "TestPassword123"
    hashed = hash_password(password)
    
    assert verify_password(password, hashed) is True


def test_verify_password_incorrect():
    """Test password verification with incorrect password."""
    password = "TestPassword123"
    hashed = hash_password(password)
    
    assert verify_password("WrongPassword", hashed) is False


def test_validate_password_strength_valid():
    """Test password strength validation with valid password."""
    assert validate_password_strength("SecurePass123") is True
    assert validate_password_strength("Abcdefg1") is True


def test_validate_password_strength_too_short():
    """Test that short passwords are rejected."""
    assert validate_password_strength("Short1") is False


def test_validate_password_strength_no_uppercase():
    """Test that passwords without uppercase are rejected."""
    assert validate_password_strength("lowercase123") is False


def test_validate_password_strength_no_lowercase():
    """Test that passwords without lowercase are rejected."""
    assert validate_password_strength("UPPERCASE123") is False


def test_validate_password_strength_no_digit():
    """Test that passwords without digits are rejected."""
    assert validate_password_strength("NoDigitsHere") is False


def test_register_user():
    """Test user registration."""
    response = client.post(
        "/auth/register",
        json={
            "email": "alice@example.com",
            "password": "SecurePass123"
        }
    )
    
    assert response.status_code == 201
    data = response.json()
    assert data["email"] == "alice@example.com"
    assert "id" in data
    assert "password" not in data
    assert "hashed_password" not in data


def test_register_password_is_hashed():
    """Test that password is hashed in database."""
    client.post(
        "/auth/register",
        json={
            "email": "bob@example.com",
            "password": "SecurePass123"
        }
    )
    
    db = TestingSessionLocal()
    user = db.query(User).filter(User.email == "bob@example.com").first()
    db.close()
    
    assert user.hashed_password != "SecurePass123"
    assert user.hashed_password.startswith("$2b$")


def test_register_duplicate_email():
    """Test that duplicate email registration fails."""
    client.post(
        "/auth/register",
        json={
            "email": "charlie@example.com",
            "password": "SecurePass123"
        }
    )
    
    # Try to register again
    response = client.post(
        "/auth/register",
        json={
            "email": "charlie@example.com",
            "password": "DifferentPass456"
        }
    )
    
    assert response.status_code == 400


def test_register_weak_password():
    """Test that weak passwords are rejected."""
    response = client.post(
        "/auth/register",
        json={
            "email": "david@example.com",
            "password": "weak"
        }
    )
    
    assert response.status_code == 422


def test_verify_endpoint():
    """Test password verification endpoint."""
    # Register user
    client.post(
        "/auth/register",
        json={
            "email": "eve@example.com",
            "password": "SecurePass123"
        }
    )
    
    # Verify correct password
    response = client.post(
        "/auth/verify",
        json={
            "email": "eve@example.com",
            "password": "SecurePass123"
        }
    )
    
    assert response.status_code == 200
    assert response.json()["valid"] is True


def test_verify_wrong_password():
    """Test verification with wrong password."""
    client.post(
        "/auth/register",
        json={
            "email": "frank@example.com",
            "password": "SecurePass123"
        }
    )
    
    response = client.post(
        "/auth/verify",
        json={
            "email": "frank@example.com",
            "password": "WrongPassword"
        }
    )
    
    assert response.status_code == 200
    assert response.json()["valid"] is False
