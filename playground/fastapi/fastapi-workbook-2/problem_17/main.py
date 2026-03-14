"""
PROBLEM 17: Configuration Management with Pydantic Settings
============================================================

LEARNING OBJECTIVES:
- Use pydantic-settings for configuration
- Load settings from environment variables
- Different configs for dev/test/prod
- Validate configuration at startup

TASK:
Create a proper configuration system using environment variables.

REQUIREMENTS:
Create config.py with Settings class:

```python
class Settings(BaseSettings):
    # Application
    app_name: str = "Chatbot API"
    debug: bool = False
    environment: str = "production"
    
    # Database
    database_url: str
    
    # JWT
    secret_key: str
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30
    refresh_token_expire_days: int = 7
    
    # File Upload
    max_file_size_mb: int = 10
    upload_dir: str = "./uploads"
    
    # CORS
    allowed_origins: list[str] = ["http://localhost:3000"]
    
    class Config:
        env_file = ".env"
```

Use configuration in main.py:
- Import and instantiate Settings
- Use settings for database URL, CORS, etc.
- Different .env files for dev/test/prod

PRODUCTION NOTES:
- **Never commit secrets**: Add .env to .gitignore
- **Environment-specific configs**: Use .env.production, .env.development
- **Validation**: Pydantic validates types at startup
- **Fail fast**: App won't start with invalid config
- **Defaults**: Provide sensible defaults for non-secrets
- **Documentation**: Document all required env vars
- **Secret management**: Use AWS Secrets Manager, Vault, etc. in production

12-FACTOR APP PRINCIPLES:
1. Config in environment (not code)
2. Strict separation of config from code
3. Never group configs as "environments"
4. Config should be language/OS agnostic

ENV FILE EXAMPLE (.env):
```
DATABASE_URL=postgresql://user:pass@localhost/db
SECRET_KEY=super-secret-key
DEBUG=true
ALLOWED_ORIGINS=http://localhost:3000,http://localhost:5173
```

EXAMPLE USAGE:
```python
from config import Settings

settings = Settings()

# Use in FastAPI
app = FastAPI(
    title=settings.app_name,
    debug=settings.debug
)

engine = create_engine(settings.database_url)
```

HINTS:
- from pydantic_settings import BaseSettings
- pip install pydantic-settings
- Use Field() for validation and descriptions
"""

# File: config.py
from pydantic_settings import BaseSettings
from pydantic import Field
from typing import List

# TODO: Create Settings class
# Inherit from BaseSettings
# Add all configuration fields
# Your code here

class Settings(BaseSettings):
    pass  # Implement this

# File: main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# TODO: Import Settings and create instance
# Your code here

# TODO: Use settings throughout the app
# - Database URL
# - CORS origins
# - JWT settings
# - File upload limits
# Your code here
