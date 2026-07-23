"""
PROBLEM 14: Background Tasks
=============================

LEARNING OBJECTIVES:
- Use BackgroundTasks to run tasks after response
- Understand when to use background tasks
- Handle async background operations

TASK:
Create an endpoint that sends emails in the background.

REQUIREMENTS:
- Create a function send_email(email: str, message: str):
  - Simulates sending email by appending to global sent_emails list
  - Format: {"email": email, "message": message}
- POST endpoint at "/send-notification"
  - Body: {"email": str, "message": str}
  - Add send_email to background tasks
  - Returns immediately: {"status": "notification queued"}
- GET endpoint at "/sent-emails"
  - Returns list of all sent emails

EXAMPLE:
POST /send-notification {"email": "test@example.com", "message": "Hello"}
→ {"status": "notification queued"} (returns immediately)

GET /sent-emails
→ [{"email": "test@example.com", "message": "Hello"}]

HINTS:
- from fastapi import BackgroundTasks
- Add background_tasks: BackgroundTasks to endpoint parameters
- Use background_tasks.add_task(function, arg1, arg2)
- Global list to store sent emails for testing
"""

from fastapi import FastAPI, BackgroundTasks
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Storage for sent emails (for testing)
sent_emails = []

class Notification(BaseModel):
    email: str
    message: str

def send_email(email: str, message: str):
  global sent_emails
  sent_emails.append({"email": email, "message": message})

@app.post("/send-notification")
def send_noti(notification: Notification, background_tasks: BackgroundTasks):
  background_tasks.add_task(send_email, notification.email, notification.message)
  return {"status": "notification queued"}

@app.get("/sent-emails")
def get_emails():
  return sent_emails

