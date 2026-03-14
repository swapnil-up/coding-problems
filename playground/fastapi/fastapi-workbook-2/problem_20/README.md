"""
PROBLEM 20: Full Chat API Integration
======================================

LEARNING OBJECTIVES:
- Integrate all previous concepts into one application
- Build a complete, production-ready chat API
- Apply architectural best practices
- Understand how all pieces fit together

TASK:
Build a complete chatbot API that combines everything you've learned.

REQUIREMENTS:
This is a multi-file application with the following structure:

```
problem_20/
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI app, router registration
│   ├── config.py            # Settings (Problem 17)
│   ├── database.py          # Database setup
│   ├── models.py            # All SQLAlchemy models
│   ├── schemas.py           # All Pydantic schemas
│   ├── dependencies.py      # get_db, get_current_user
│   ├── auth.py              # Password hashing, JWT utilities
│   ├── middleware.py        # Logging, error handling
│   └── routers/
│       ├── __init__.py
│       ├── auth.py          # Register, login, refresh, logout
│       ├── conversations.py # CRUD conversations
│       ├── messages.py      # CRUD messages
│       ├── chat.py          # Streaming chat endpoint
│       └── files.py         # File upload/download
├── tests/
│   ├── test_auth.py
│   ├── test_conversations.py
│   ├── test_messages.py
│   ├── test_chat.py
│   └── test_files.py
├── alembic/                 # Database migrations
├── uploads/                 # File storage
├── .env.example
├── requirements.txt
└── README.md
```

FEATURES TO IMPLEMENT:
1. **Authentication** (Problems 12-15)
   - User registration with password hashing
   - JWT login with access + refresh tokens
   - Protected endpoints
   - Logout (token revocation)

2. **Conversations** (Problems 1-3)
   - Create conversation
   - List user's conversations
   - Get conversation details
   - Delete conversation

3. **Messages** (Problem 3)
   - Add message to conversation
   - List messages with pagination
   - Message history

4. **Streaming Chat** (Problems 6-7)
   - POST /chat/stream
   - Stream LLM-style responses
   - Save messages to database
   - Handle disconnection gracefully

5. **File Uploads** (Problems 9-11)
   - Upload files to conversations
   - File validation and security
   - Download files
   - Associate files with messages

6. **Production Features** (Problems 17-19)
   - Environment-based configuration
   - Centralized error handling
   - Request logging
   - Health checks
   - Metrics endpoint

API ENDPOINTS:
```
POST   /auth/register          # Register new user
POST   /auth/login             # Login (get tokens)
POST   /auth/refresh           # Refresh access token
POST   /auth/logout            # Logout (revoke tokens)

GET    /conversations          # List user's conversations
POST   /conversations          # Create conversation
GET    /conversations/{id}     # Get conversation
DELETE /conversations/{id}     # Delete conversation

GET    /conversations/{id}/messages  # List messages (paginated)
POST   /messages               # Add message

POST   /chat/stream            # Stream chat response
                               # Body: {conversation_id, message}
                               # Returns: SSE stream

POST   /files/upload           # Upload file
GET    /files/{id}             # Get file metadata
GET    /files/{id}/download    # Download file

GET    /health                 # Health check
GET    /metrics                # API metrics
```

PRODUCTION NOTES:
This brings together all production practices:
- **Security**: JWT auth, password hashing, file validation
- **Performance**: Pagination, streaming, async operations
- **Reliability**: Error handling, health checks, graceful degradation
- **Observability**: Logging, metrics, request tracing
- **Scalability**: Stateless design, database optimization
- **Maintainability**: Clean architecture, separation of concerns

TESTING:
Each feature should have comprehensive tests:
- Unit tests for utilities (auth, validation)
- Integration tests for endpoints
- Test database fixtures
- Mock external dependencies

DEPLOYMENT CONSIDERATIONS:
- Dockerize the application
- Use PostgreSQL in production (not SQLite)
- Add CORS for frontend
- Set up CI/CD pipeline
- Configure environment variables
- Add rate limiting
- Implement caching

SIMULATED LLM RESPONSES:
For this exercise, use simple rule-based responses:
- If message contains "hello" → "Hello! How can I help?"
- If message contains "weather" → "I don't have weather data."
- Default → "I'm a simulated assistant. How can I help?"

In production, replace with actual LLM API calls (OpenAI, Anthropic, etc.)

BONUS FEATURES (Optional):
- Conversation titles auto-generation
- Message search
- User preferences
- Conversation sharing
- Export conversation history
- Message reactions
- Typing indicators

SUCCESS CRITERIA:
✓ All endpoints working
✓ Authentication flow complete
✓ Streaming chat functional
✓ File uploads working
✓ Tests passing
✓ Error handling consistent
✓ Logging in place
✓ Configuration externalized
✓ Database migrations set up
✓ Code well-organized

This is your capstone project - a real, deployable chat API!
"""

# This problem requires you to build the entire application
# from scratch using the patterns learned in Problems 1-19.

# Start with the directory structure above, then:
# 1. Set up configuration (config.py)
# 2. Set up database (database.py, models.py)
# 3. Implement authentication (auth.py router)
# 4. Implement conversations (conversations.py router)
# 5. Implement messages (messages.py router)
# 6. Implement streaming chat (chat.py router)
# 7. Implement file uploads (files.py router)
# 8. Add middleware (logging, errors)
# 9. Add health/metrics endpoints
# 10. Write tests

# See the README.md in this directory for detailed instructions.
