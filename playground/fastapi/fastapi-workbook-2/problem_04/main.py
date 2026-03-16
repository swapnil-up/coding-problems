"""
PROBLEM 04: Database Migrations with Alembic
=============================================

LEARNING OBJECTIVES:
- Initialize and use Alembic for database migrations
- Create and apply migrations
- Handle schema changes safely
- Understand migration best practices

TASK:
Set up Alembic and create your first migration.

REQUIREMENTS:
1. Initialize Alembic in your project
2. Configure alembic.ini and env.py to use your database
3. Create an initial migration for User and Conversation models
4. Add a new column to User model: "bio" (Boolean, default=True)
5. Create a migration for this change
6. Implement endpoints to test the migration worked

SETUP COMMANDS:
```bash
# Initialize Alembic
alembic init alembic

# Create migration
alembic revision --autogenerate -m "Initial migration"

# Apply migration
alembic upgrade head

# Create new migration after model change
alembic revision --autogenerate -m "Add bio to users"

# Apply new migration
alembic upgrade head
```

ENDPOINTS TO IMPLEMENT:
- GET /migration-status
  - Returns: {"current_revision": str, "bio_column_exists": bool}
  
- POST /users (updated from Problem 01)
  - Now includes bio field
  - Body: {"email": str, "password": str, "bio": bool} (bio optional, default=True)

PRODUCTION NOTES:
- **Zero-downtime migrations**: Test migrations thoroughly before production
- **Rollback plan**: Always have a rollback strategy (alembic downgrade)
- **Data migrations**: Handle data transformation separately from schema changes
- **Version control**: Commit migration files to git
- **Production deployment**: Run migrations before deploying new code
- **Large tables**: Adding columns to large tables can lock them; use strategies like:
  - Add column as nullable first
  - Backfill data
  - Make non-nullable later
- **Multiple databases**: Coordinate migrations across databases
- **Team coordination**: Avoid conflicts by communicating schema changes

MIGRATION BEST PRACTICES:
1. Always review auto-generated migrations
2. Test migrations on a copy of production data
3. Make migrations reversible (implement downgrade())
4. Keep migrations small and focused
5. Don't edit applied migrations
6. Use transactions where possible
7. Document complex migrations

ALEMBIC CONFIG (env.py):
You'll need to import your Base and configure the target_metadata:

```python
from app.models import Base
target_metadata = Base.metadata
```

EXAMPLE MIGRATION FILE:
```python
def upgrade():
    op.add_column('users', sa.Column('bio', sa.Boolean(), nullable=True))
    op.execute("UPDATE users SET bio = true WHERE bio IS NULL")
    op.alter_column('users', 'bio', nullable=False)

def downgrade():
    op.drop_column('users', 'bio')
```

HINTS:
- alembic.ini contains database URL
- env.py needs your Base.metadata
- Use autogenerate but always review
- Test both upgrade and downgrade
"""

from typing import Optional

from fastapi import FastAPI, Depends
from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey, Boolean, inspect
from sqlalchemy.orm import Session, sessionmaker, relationship, declarative_base
from datetime import datetime
from pydantic import BaseModel
from alembic.migration import MigrationContext

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Models - UPDATED with bio field
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True)
    hashed_password = Column(String)
    bio = Column(String(500), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

class Conversation(Base):
    __tablename__ = "conversations"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), index=True)
    title = Column(String(255))
    created_at = Column(DateTime, default=datetime.utcnow)
    user = relationship("User")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Pydantic schemas
class UserCreate(BaseModel):
    email: str
    password: str
    bio: Optional[str] = None

class UserResponse(BaseModel):
    id: int
    email: str
    bio: Optional[str] = None
    created_at: datetime
    
    class Config:
        from_attributes = True

class MigrationStatus(BaseModel):
    message: str
    bio_column_exists: bool

app = FastAPI()

@app.get("/migration-status", response_model=MigrationStatus)
def check_migration():
    check = column_exists(engine, "User", "bio")
    version = check_version()
    return {"current_revision": version, "bio_column_exists": check}

def column_exists(engine, table_name, column_name, schema=None):
    insp = inspect(engine)
    columns=insp.get_columns(table_name, schema=schema)
    for col in columns:
        if col['name']==column_name:
            return True
    return False
    
def check_version():
    conn = engine.connect()
    context = MigrationContext.configure(conn)
    version = context.get_current_revision()
    conn.close()
    return version


@app.post("/users", response_model=UserResponse, status_code=201)
def create_user(user_data: UserCreate, db: Session = Depends(get_db)):
    new_user = User(
        email = user_data.email, 
        hashed_password = user_data.password,
        bio=user_data.bio
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@app.get("/users/{user_id}", response_model=UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        from fastapi import HTTPException
        raise HTTPException(status_code=404, detail="User not found")
    return user

"""
INSTRUCTIONS:
1. Run: alembic init alembic
2. Edit alembic.ini: set sqlalchemy.url to your database
3. Edit alembic/env.py: import Base and set target_metadata = Base.metadata
4. Create initial migration: alembic revision --autogenerate -m "Initial migration"
5. Apply migration: alembic upgrade head
6. Add bio column to User model (uncomment TODO above)
7. Create migration: alembic revision --autogenerate -m "Add bio to users"
8. Apply migration: alembic upgrade head
9. Test with pytest
"""
