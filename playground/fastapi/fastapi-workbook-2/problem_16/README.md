"""
PROBLEM 16: Multi-File Application Structure
=============================================

LEARNING OBJECTIVES:
- Organize FastAPI projects with multiple files
- Separate concerns (routers, models, schemas, dependencies)
- Use APIRouter for modular endpoints
- Import and compose routers in main app

TASK:
Refactor a monolithic app into a proper multi-file structure.

REQUIRED STRUCTURE:
```
problem_16/
├── app/
│   ├── __init__.py
│   ├── main.py           # FastAPI app instance, router registration
│   ├── database.py       # Database setup, engine, session
│   ├── models.py         # SQLAlchemy models
│   ├── schemas.py        # Pydantic schemas
│   ├── dependencies.py   # Shared dependencies (get_db, etc.)
│   └── routers/
│       ├── __init__.py
│       ├── users.py      # User-related endpoints
│       └── conversations.py  # Conversation endpoints
└── tests/
    └── test_structure.py
```

REQUIREMENTS:
Each file should have specific content:

**app/database.py:**
- Database engine setup
- SessionLocal creation
- Base declarative class

**app/models.py:**
- User model
- Conversation model
- Message model (bonus)

**app/schemas.py:**
- UserCreate, UserResponse schemas
- ConversationCreate, ConversationResponse schemas

**app/dependencies.py:**
- get_db() dependency function

**app/routers/users.py:**
- APIRouter instance with prefix="/users" and tag="users"
- POST /users (create user)
- GET /users/{user_id} (get user)

**app/routers/conversations.py:**
- APIRouter instance with prefix="/conversations" and tag="conversations"
- POST /conversations
- GET /conversations
- GET /conversations/{conversation_id}

**app/main.py:**
- FastAPI app instance
- Include both routers
- Startup event to create tables

PRODUCTION NOTES:
- **Separation of concerns**: Models, schemas, and routes separated
- **Testability**: Each component can be tested independently
- **Scalability**: Easy to add new routers/features
- **Team collaboration**: Multiple devs can work on different routers
- **API versioning**: Can add v1/, v2/ routers easily
- **Dependency management**: Shared dependencies in one place
- **Configuration**: Add config.py for settings (Problem 17)

WHY THIS STRUCTURE:
- Small projects: Single file is fine
- Medium projects (>5 endpoints): Use this structure
- Large projects: Add services/, repositories/, more layers

EXAMPLE USAGE:
```python
# Instead of:
@app.get("/users/{user_id}")
def get_user(...):
    pass

# We have:
# In app/routers/users.py:
router = APIRouter(prefix="/users", tags=["users"])

@router.get("/{user_id}")
def get_user(...):
    pass

# In app/main.py:
from app.routers import users, conversations
app.include_router(users.router)
app.include_router(conversations.router)
```

HINTS:
- Use relative imports: from ..database import SessionLocal
- APIRouter works like FastAPI but for subsets of routes
- Tags help organize API docs
- Prefix avoids repeating path parts
"""

# This problem has multiple files - see the file structure above
# You'll need to create each file according to the specifications

# File: app/__init__.py
# (Empty file to make app a package)

# File: app/database.py
# TODO: Create database setup here

# File: app/models.py
# TODO: Move models here

# File: app/schemas.py
# TODO: Move Pydantic schemas here

# File: app/dependencies.py
# TODO: Create get_db dependency here

# File: app/routers/__init__.py
# (Empty file)

# File: app/routers/users.py
# TODO: Create user routes here with APIRouter

# File: app/routers/conversations.py
# TODO: Create conversation routes here with APIRouter

# File: app/main.py
# TODO: Create main app, include routers

# See the test file for expected structure and behavior
