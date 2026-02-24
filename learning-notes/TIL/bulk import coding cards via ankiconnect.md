# bulk import coding cards via ankiconnect

Date: 2026-02-24 12:39

---
With multiline csv files, one of the best things you can do is use ankiconnect and use python's superior parsing skills to import cards directly into anki. 

Sample of the cards that led to this:
```

from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def root():
    return "hello"
# What type is the response? | str gets auto-converted to JSON string response with quotes: "hello" | FastAPI auto-converts return values. Use PlainTextResponse for actual plain text.

from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def root():
    return {"msg": "hello"}
# What's in response body? | {"msg":"hello"} as JSON | Dicts are automatically serialized to JSON with correct content-type header.

from fastapi import FastAPI
app = FastAPI()
@app.get("/users/{user_id}")
def get_user(id: int):
    return {"user_id": id}
# Does this work? GET /users/5 | No - NameError: name 'id' is not defined | Path parameter name in decorator must match function parameter name exactly.

from fastapi import FastAPI
app = FastAPI()
@app.get("/users/{user_id}")
def get_user(user_id):
    return {"user_id": user_id}
# GET /users/abc - what happens? | 422 Validation Error | No type hint means str, but we should add type hints. With user_id: int it would also 422.
```


Script used:

```
import requests
import re
import json

FILE_PATH = "to-import.csv"

def add_note(front, back, extra):
    payload = {
        "action": "addNote",
        "version": 6,
        "params": {
            "note": {
                "deckName": "fastapi",  # Change to your deck name
                "modelName": "Basic",         # Change to your note type (e.g., "Basic")
                "fields": {
                    "Front": f"<pre><code>{front}</code></pre>",
                    "Back": back,
                    "Context": extra
                },
                "options": {
                    "allowDuplicate": False
                },
                "tags": ["fastapi_auto_import"]
            }
        }
    }
    try:
        response = requests.post('http://localhost:8765', json=payload)
        return response.json()
    except Exception as e:
        return {"error": str(e)}

print(f"--- STARTING DEBUG FOR: {FILE_PATH} ---")

try:
    with open(FILE_PATH, 'r', encoding='utf-8') as f:
        content = f.read().strip()
    
    # Using regex to split by 2 or more newlines
    chunks = re.split(r'\n\s*\n', content)
    print(f"DEBUG: Found {len(chunks)} potential chunks.\n")

    for i, chunk in enumerate(chunks, 1):
        # Move the replace outside the f-string for compatibility
        readable_chunk = chunk.replace('\n', ' [NL] ')
        
        print(f"--- ANALYZING CHUNK #{i} ---")
        print(f"RAW CONTENT: {readable_chunk[:150]}...") # Truncated for readability
        
        # Use maxsplit=2 to keep the 3rd part whole
        parts = [p.strip() for p in chunk.split('|', 2)]
        print(f"SPLIT COUNT: {len(parts)} parts found.")
        
        if len(parts) >= 2:
            front = parts[0]
            back = parts[1]
            extra = parts[2] if len(parts) == 3 else "[EMPTY]"
            
            print(f"  > FRONT: {repr(front[:50])}...")
            print(f"  > BACK:  {repr(back)}")
            print(f"  > EXTRA: {repr(extra)}")
            
            # UNCOMMENT THESE TWO LINES TO ACTUALLY IMPORT
            result = add_note(front, back, extra)
            print(f"  > ANKI RESULT: {result}")
        else:
            print("  > SKIP: Not enough pipes (|) in this chunk.")
        
        print("-" * 40 + "\n")

except FileNotFoundError:
    print(f"ERROR: Could not find {FILE_PATH}")
except Exception as e:
    print(f"CRITICAL ERROR: {e}")

print("--- DEBUG COMPLETE ---")
```



Yes the code is unpolished vibecoded mess, to be refined before pushing into scripts later
