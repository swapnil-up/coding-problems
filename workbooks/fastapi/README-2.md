# FastAPI Workbook 2: Chatbot Platform Essentials

Build production-ready FastAPI skills for real applications. This workbook focuses on the patterns and practices you'll use building a chatbot messaging platform.

## Prerequisites

- Complete Workbook 1 (FastAPI Fundamentals)
- Python 3.9+
- Basic understanding of SQL

## What You'll Learn

This workbook teaches you to build a **real chatbot API** with:
- Database persistence (SQLAlchemy + PostgreSQL/SQLite)
- Streaming responses (like ChatGPT)
- File uploads and processing
- JWT authentication
- Production-ready code structure
- Security best practices

## Setup

```bash
# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Create .env file for configuration
cp .env.example .env
```

## Workbook Structure

### Module 1: Database with SQLAlchemy (Problems 1-5)
Learn to persist data properly with relationships, migrations, and transactions.

- **Problem 01**: SQLAlchemy setup, User and Conversation models
- **Problem 02**: CRUD operations for conversations
- **Problem 03**: Message model with pagination
- **Problem 04**: Database migrations with Alembic
- **Problem 05**: Transactions and rollback handling

**Production notes**: Connection pooling, N+1 queries, indexing strategy

### Module 2: Streaming Responses (Problems 6-8)
Implement ChatGPT-style streaming where tokens appear one by one.

- **Problem 06**: Server-Sent Events (SSE) basics
- **Problem 07**: Stream LLM-style responses
- **Problem 08**: Handle client disconnection gracefully

**Production notes**: Timeout handling, memory management, error recovery

### Module 3: File Handling (Problems 9-11)
Handle user file uploads securely and efficiently.

- **Problem 09**: Upload validation (size, type, security)
- **Problem 10**: Store files with organized paths
- **Problem 11**: Process files (extract text, resize images)

**Production notes**: Virus scanning, storage limits, CDN integration

### Module 4: Authentication & Authorization (Problems 12-15)
Implement secure user authentication with JWT.

- **Problem 12**: User registration with password hashing
- **Problem 13**: Login with JWT token generation
- **Problem 14**: Protected endpoints with JWT validation
- **Problem 15**: Refresh tokens and token rotation

**Production notes**: Password policies, rate limiting, token revocation

### Module 5: Production Code Structure (Problems 16-20)
Build a properly structured application that scales.

- **Problem 16**: Multi-file structure (routers, models, schemas)
- **Problem 17**: Configuration management and secrets
- **Problem 18**: Centralized error handling
- **Problem 19**: Logging and monitoring
- **Problem 20**: Full chat API integration

**Production notes**: Deployment, Docker, health checks, observability

## Running Problems

Each problem can be run independently:

```bash
# For single-file problems (1-15)
cd problem_01
uvicorn main:app --reload

# Run tests
pytest test_main.py -v

# For multi-file problems (16-20)
cd problem_16
uvicorn app.main:app --reload

pytest tests/ -v
```

## Database Setup

Starting from Problem 1, you'll need a database. We use SQLite for development:

```bash
# SQLite (automatic, no setup needed)
# Database file will be created as chatbot.db

# For PostgreSQL (production-like):
# Install PostgreSQL, then update .env with:
# DATABASE_URL=postgresql://user:password@localhost/chatbot_db
```

## Progress Tracking

- [ ] **Module 1: Database** (Problems 1-5)
  - [ ] Problem 01: SQLAlchemy Models
  - [ ] Problem 02: Conversation CRUD
  - [ ] Problem 03: Messages & Pagination
  - [ ] Problem 04: Alembic Migrations
  - [ ] Problem 05: Transactions

- [ ] **Module 2: Streaming** (Problems 6-8)
  - [ ] Problem 06: SSE Basics
  - [ ] Problem 07: Token Streaming
  - [ ] Problem 08: Disconnection Handling

- [ ] **Module 3: Files** (Problems 9-11)
  - [ ] Problem 09: Upload Validation
  - [ ] Problem 10: File Storage
  - [ ] Problem 11: File Processing

- [ ] **Module 4: Auth** (Problems 12-15)
  - [ ] Problem 12: Registration & Hashing
  - [ ] Problem 13: JWT Login
  - [ ] Problem 14: Protected Endpoints
  - [ ] Problem 15: Refresh Tokens

- [ ] **Module 5: Structure** (Problems 16-20)
  - [ ] Problem 16: Multi-file App
  - [ ] Problem 17: Configuration
  - [ ] Problem 18: Error Handling
  - [ ] Problem 19: Logging
  - [ ] Problem 20: Full Integration

## Production Best Practices Covered

Throughout this workbook, you'll learn:

- **Security**: Password hashing, JWT secrets, file validation, SQL injection prevention
- **Performance**: Database indexing, connection pooling, pagination, async I/O
- **Reliability**: Error handling, transactions, graceful degradation
- **Observability**: Logging, request tracing, health checks
- **Scalability**: Proper separation of concerns, stateless design
- **Maintainability**: Clean code structure, type hints, comprehensive tests

## After This Workbook

You'll be ready to:
- Build and deploy a production chatbot API
- Integrate with LLM providers (OpenAI, Anthropic, etc.)
- Handle thousands of concurrent users
- Debug production issues
- Scale your application

## Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [SQLAlchemy 2.0 Documentation](https://docs.sqlalchemy.org/)
- [Alembic Tutorial](https://alembic.sqlalchemy.org/en/latest/tutorial.html)
- [JWT Best Practices](https://tools.ietf.org/html/rfc8725)

Good luck! 🚀
