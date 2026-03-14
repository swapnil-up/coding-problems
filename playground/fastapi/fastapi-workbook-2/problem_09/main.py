"""
PROBLEM 09: File Upload with Security Validation
=================================================

LEARNING OBJECTIVES:
- Handle file uploads in FastAPI
- Validate file size and type
- Implement security checks
- Prevent common file upload attacks

TASK:
Create secure file upload endpoints with validation.

REQUIREMENTS:
- POST /upload
  - Accepts file upload (multipart/form-data)
  - Validates file size (max 10MB)
  - Validates file type (only: image/jpeg, image/png, application/pdf, text/plain)
  - Returns: {"filename": str, "size": int, "content_type": str}
  - Returns 413 if file too large
  - Returns 400 if invalid type

PRODUCTION NOTES:
- **File size limits**: Prevent DoS via huge uploads
- **File type validation**: Check MIME type AND magic bytes (not just extension)
- **Filename sanitization**: Remove path traversal (../, etc.)
- **Virus scanning**: Integrate with ClamAV or similar
- **Storage limits**: Set per-user upload quotas
- **Async uploads**: For large files, use async/await
- **Temporary files**: Clean up temp files after processing
- **Content inspection**: For PDFs, check for embedded malware

SECURITY CHECKLIST:
✓ Validate file size before reading entire file
✓ Check MIME type
✓ Verify magic bytes (file signature)
✓ Sanitize filename
✓ Store outside web root
✓ Generate unique filenames (don't use user-provided names as-is)
✓ Set upload rate limits
✓ Scan for viruses (production)

ATTACK VECTORS TO PREVENT:
- Zip bombs (tiny file expands to huge size)
- Path traversal (../../etc/passwd)
- Executable uploads disguised as images
- DoS via many small files
- XXE attacks in XML/SVG files

EXAMPLE:
POST /upload
Content-Type: multipart/form-data
file: [image.jpg, 5MB]

→ 200 {"filename": "image.jpg", "size": 5242880, "content_type": "image/jpeg"}

HINTS:
- from fastapi import UploadFile, File
- Use UploadFile for file uploads
- Check file.size and file.content_type
- Use python-magic to verify actual file type
- UploadFile.file is a SpooledTemporaryFile
"""

from fastapi import FastAPI, UploadFile, File, HTTPException, status
from pydantic import BaseModel
import magic
import os

app = FastAPI()

# Configuration
MAX_FILE_SIZE = 10 * 1024 * 1024  # 10MB
ALLOWED_TYPES = {
    "image/jpeg",
    "image/png",
    "application/pdf",
    "text/plain"
}

class UploadResponse(BaseModel):
    filename: str
    size: int
    content_type: str

def sanitize_filename(filename: str) -> str:
    """
    Remove dangerous characters from filename.
    
    Prevents path traversal attacks.
    """
    # TODO: Implement filename sanitization
    # Remove: .., /, \, null bytes, etc.
    # Your code here
    pass

def verify_file_type(file_content: bytes, declared_type: str) -> bool:
    """
    Verify file type using magic bytes.
    
    Prevents files disguised with wrong extension.
    """
    # TODO: Use python-magic to check actual file type
    # Compare with declared_type
    # Your code here
    pass

# TODO: Implement POST /upload
# 1. Check file size
# 2. Check declared content type
# 3. Read file content
# 4. Verify actual file type with magic bytes
# 5. Sanitize filename
# 6. Return upload response
# Your code here
