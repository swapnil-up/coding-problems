"""Tests for Problem 01: SQLAlchemy Models & Database Setup"""

from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from main import app, Base, get_db, User, Conversation
import os

# Use a separate test database
TEST_DATABASE_URL = "sqlite:///./test_db.db"
engine = create_engine(TEST_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def override_get_db():
    """Override database dependency for testing."""
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)


def setup_function():
    """Create tables before each test."""
    Base.metadata.create_all(bind=engine)


def teardown_function():
    """Drop tables after each test."""
    Base.metadata.drop_all(bind=engine)
    engine.dispose()
    if os.path.exists("test_db.db"):
        os.remove("test_db.db")


def test_create_user():
    """Test creating a user."""
    response = client.post(
        "/users",
        json={"email": "alice@example.com", "password": "password123"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["email"] == "alice@example.com"
    assert "id" in data
    assert "created_at" in data


def test_user_id_autoincrement():
    """Test that user IDs auto-increment."""
    response1 = client.post("/users", json={"email": "user1@example.com", "password": "pass"})
    response2 = client.post("/users", json={"email": "user2@example.com", "password": "pass"})
    
    id1 = response1.json()["id"]
    id2 = response2.json()["id"]
    assert id2 > id1


def test_user_email_stored():
    """Test that email is correctly stored."""
    email = "test@example.com"
    client.post("/users", json={"email": email, "password": "pass"})
    
    # Check directly in database
    db = TestingSessionLocal()
    user = db.query(User).filter(User.email == email).first()
    assert user is not None
    assert user.email == email
    db.close()


def test_user_has_created_at():
    """Test that created_at timestamp is set."""
    response = client.post("/users", json={"email": "time@example.com", "password": "pass"})
    data = response.json()
    assert "created_at" in data
    # Should be able to parse as ISO datetime
    from datetime import datetime
    datetime.fromisoformat(data["created_at"].replace("Z", "+00:00"))


def test_user_model_exists():
    """Test that User model is defined correctly."""
    assert hasattr(User, '__tablename__')
    assert hasattr(User, 'id')
    assert hasattr(User, 'email')
    assert hasattr(User, 'hashed_password')
    assert hasattr(User, 'created_at')


def test_conversation_model_exists():
    """Test that Conversation model is defined correctly."""
    assert hasattr(Conversation, '__tablename__')
    assert hasattr(Conversation, 'id')
    assert hasattr(Conversation, 'user_id')
    assert hasattr(Conversation, 'title')
    assert hasattr(Conversation, 'created_at')


def test_conversation_user_relationship():
    """Test that Conversation has a relationship to User."""
    assert hasattr(Conversation, 'user')


def test_database_tables_created():
    """Test that tables are created in database."""
    from sqlalchemy import inspect
    inspector = inspect(engine)
    tables = inspector.get_table_names()
    
    assert 'users' in tables or 'user' in tables
    assert 'conversations' in tables or 'conversation' in tables


def test_user_email_index():
    """Test that email column has an index."""
    from sqlalchemy import inspect
    inspector = inspect(engine)
    # Get indexes for users table
    indexes = inspector.get_indexes('users') if 'users' in inspector.get_table_names() else inspector.get_indexes('user')
    
    # Check if any index includes email column
    email_indexed = any('email' in idx.get('column_names', []) for idx in indexes)
    assert email_indexed, "Email column should be indexed for performance"


def test_foreign_key_relationship():
    """Test that Conversation.user_id is a foreign key to User.id."""
    # Create a user first
    response = client.post("/users", json={"email": "fk@example.com", "password": "pass"})
    user_id = response.json()["id"]
    
    # Create conversation in database
    db = TestingSessionLocal()
    conversation = Conversation(user_id=user_id, title="Test Conversation")
    db.add(conversation)
    db.commit()
    db.refresh(conversation)
    
    # Test relationship works
    assert conversation.user is not None
    assert conversation.user.id == user_id
    db.close()
