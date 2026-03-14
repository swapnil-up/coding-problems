"""
PROBLEM 11: File Processing (Extract Text, Resize Images)
==========================================================

LEARNING OBJECTIVES:
- Extract text from PDF files
- Resize and optimize images
- Use background processing for heavy tasks
- Handle processing errors gracefully

TASK:
Create endpoints that process uploaded files.

REQUIREMENTS:
- POST /process/pdf
  - Accepts PDF file
  - Extracts all text from PDF
  - Returns: {"text": str, "page_count": int, "char_count": int}

- POST /process/image/resize
  - Accepts image file
  - Query params: width (int), height (int)
  - Resizes image to specified dimensions
  - Returns resized image file
  - Preserves aspect ratio if only width OR height provided

- POST /process/image/thumbnail
  - Accepts image file
  - Creates 200x200 thumbnail
  - Returns thumbnail image

PRODUCTION NOTES:
- **Background processing**: Use Celery/RQ for large files
- **Timeouts**: Set processing time limits
- **Memory limits**: Large PDFs can cause OOM
- **Error handling**: Corrupted files should return clear errors
- **Rate limiting**: Prevent abuse of CPU-intensive operations
- **Caching**: Cache processed results
- **Async**: Use async processing for non-blocking operations
- **Storage**: Store processed files, don't reprocess
- **Monitoring**: Track processing time and failures

SECURITY:
- **PDF bombs**: PDFs with millions of pages
- **Image bombs**: Compressed images that expand hugely
- **Malicious content**: PDFs with embedded malware
- **Resource limits**: Set max pages, max pixels

LIBRARIES:
- PyPDF2 or pdfplumber for PDF text extraction
- Pillow (PIL) for image processing

EXAMPLE:
POST /process/pdf
file: document.pdf

→ {
    "text": "This is the extracted text...",
    "page_count": 5,
    "char_count": 1523
  }

POST /process/image/resize?width=800
file: photo.jpg

→ [Returns resized image file]

HINTS:
- from PIL import Image
- import pdfplumber or PyPDF2
- Image.open(file.file) to open uploaded image
- Use BytesIO to return image bytes
- Set Content-Type header for image responses
"""

from fastapi import FastAPI, UploadFile, File, HTTPException, Query
from fastapi.responses import Response, StreamingResponse
from pydantic import BaseModel
from PIL import Image
import pdfplumber
from io import BytesIO
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

MAX_PDF_PAGES = 100
MAX_IMAGE_PIXELS = 50_000_000  # 50 megapixels

class PDFProcessResult(BaseModel):
    text: str
    page_count: int
    char_count: int

def extract_text_from_pdf(file_bytes: bytes) -> PDFProcessResult:
    """
    Extract text from PDF file.
    
    Args:
        file_bytes: PDF file content
        
    Returns:
        PDFProcessResult with extracted text and stats
        
    Raises:
        HTTPException if PDF is too large or corrupted
    """
    # TODO: Implement PDF text extraction
    # 1. Open PDF with pdfplumber
    # 2. Extract text from each page
    # 3. Combine all text
    # 4. Check page count limit
    # 5. Return result
    # Your code here
    pass

def resize_image(
    file_bytes: bytes,
    width: int = None,
    height: int = None
) -> bytes:
    """
    Resize image while preserving aspect ratio.
    
    Args:
        file_bytes: Image file content
        width: Target width (optional)
        height: Target height (optional)
        
    Returns:
        Resized image bytes
    """
    # TODO: Implement image resizing
    # 1. Open image with PIL
    # 2. Check size limits
    # 3. Calculate new dimensions (preserve aspect ratio if only one dimension given)
    # 4. Resize image
    # 5. Save to BytesIO
    # 6. Return bytes
    # Your code here
    pass

# TODO: Implement POST /process/pdf
# Extract text from uploaded PDF
# Return PDFProcessResult
# Your code here

# TODO: Implement POST /process/image/resize
# Resize image to specified dimensions
# Return image file with appropriate Content-Type
# Your code here

# TODO: Implement POST /process/image/thumbnail
# Create 200x200 thumbnail
# Return thumbnail image
# Your code here
