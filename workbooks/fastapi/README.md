# FastAPI Interactive Workbook

Learn FastAPI by solving progressively harder problems. Each problem has:
- A starter file with instructions and broken/incomplete code
- A test file to verify your solution
- Clear learning objectives

## Setup

```bash
# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install fastapi uvicorn pytest httpx
```

## How to Use

1. Start with `problem_01/` and work through sequentially
2. Read the problem description in each `main.py`
3. Fix/complete the code to make tests pass
4. Run tests: `pytest problem_01/test_main.py -v`
5. Move to the next problem when all tests pass

## Running Individual Problems

```bash
# Run the FastAPI app
cd problem_01
uvicorn main:app --reload

# In another terminal, run tests
pytest test_main.py -v
```

## Problem Structure

- **01-05**: Basics (routing, responses, request handling)
- **06-10**: Data validation (Pydantic models, query params, path params)
- **11-15**: Advanced patterns (dependencies, middleware, async, database)
- **16-20**: Real-world scenarios (auth, error handling, file uploads, testing)

## Progress Tracking

Mark problems as complete by adding ✓ here:
- [ ] Problem 01: Hello FastAPI
- [ ] Problem 02: Path Parameters
- [ ] Problem 03: Query Parameters
- [ ] Problem 04: Request Body
- [ ] Problem 05: Response Models
- [ ] Problem 06: Data Validation
- [ ] Problem 07: Multiple Parameters
- [ ] Problem 08: Nested Models
- [ ] Problem 09: Dependencies
- [ ] Problem 10: Dependency Injection
- [ ] Problem 11: Async Endpoints
- [ ] Problem 12: Background Tasks
- [ ] Problem 13: Error Handling
- [ ] Problem 14: Middleware
- [ ] Problem 15: Database Integration
- [ ] Problem 16: Authentication Basics
- [ ] Problem 17: JWT Auth
- [ ] Problem 18: File Upload
- [ ] Problem 19: CORS & Security
- [ ] Problem 20: Testing FastAPI Apps

Good luck! 🚀