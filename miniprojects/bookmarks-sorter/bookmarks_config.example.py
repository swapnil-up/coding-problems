"""
Example configuration — copy this to bookmarks_config.py and customize.

This file is safe to commit. The actual bookmarks_config.py is gitignored.
"""

import os

SRC = os.path.join(os.path.dirname(__file__), "bookmarks.html")
OUT_DIR = os.path.dirname(__file__)

TOPIC_ORDER = [
    "tech",
    "design",
    "music",
    "other",
]

TOPIC_LABELS = {
    "tech": "Technology",
    "design": "Design",
    "music": "Music",
    "other": "Uncategorized",
}

# Map domains to their primary topic.
# The script checks this first when classifying a bookmark.
DOMAIN_TOPIC_MAP = {
    "github.com": "tech",
    "stackoverflow.com": "tech",
    "dribbble.com": "design",
    "behance.net": "design",
    "spotify.com": "music",
    "soundcloud.com": "music",
}

# Keywords in bookmark titles that add secondary tags.
# These don't change where the bookmark goes — they just add TAGS="..."
KEYWORD_TAGS = {
    "tech": r"\b(?:programming|code|software|algorithm|tutorial|api|database|linux|docker|python|javascript|react|vue)\b",
    "design": r"\b(?:design|ux|ui|typography|color|layout|figma|sketch|wireframe|prototype)\b",
    "music": r"\b(?:music|song|album|beat|melody|synth|mix|mastering|producer|ableton|fl studio)\b",
}

# If a folder name contains these strings, its contents get that topic.
FOLDER_HINTS = {
    "tech": ["programming", "code", "dev", "software", "coding"],
    "design": ["design", "ui", "ux", "art"],
    "music": ["music", "audio", "production"],
}
