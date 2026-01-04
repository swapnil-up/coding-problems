import cv2
import numpy as np
import sys
import json

IMAGE_PATH = sys.argv[1]

# --- CONFIG ---
WHITE_THRESHOLD = 230
MIN_WHITE_RATIO = 0.35 
MAX_BG_VARIANCE = 0.15
MIN_FACE_RATIO = 0.20
MAX_FACE_RATIO = 0.55
MIN_BLUR_SCORE = 100

# --- LOAD IMAGE ---
img = cv2.imread(IMAGE_PATH)
if img is None:
    print(json.dumps({"ok": False, "reason": "invalid_image"}))
    sys.exit(0)

h, w, _ = img.shape

# --- FACE DETECTION ---
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.3,
    minNeighbors=5
)

if len(faces) != 1:
    print(json.dumps({
        "ok": False,
        "faces": len(faces),
        "reason": "face_count"
    }))
    sys.exit(0)

(x, y, fw, fh) = faces[0]
face_ratio = fh / h

if not (MIN_FACE_RATIO <= face_ratio <= MAX_FACE_RATIO):
    print(json.dumps({
        "ok": False,
        "faces": 1,
        "face_ratio": round(face_ratio, 2),
        "reason": "face_size"
    }))
    sys.exit(0)

# --- MASK FACE REGION ---
mask = np.ones((h, w), dtype=np.uint8)

pad = int(0.08 * fw)
x1 = max(0, x - pad)
y1 = max(0, y - pad)
x2 = min(w, x + fw + pad)
y2 = min(h, y + fh + pad)

mask[y1:y2, x1:x2] = 0

bg_pixels = img[mask == 1]

# --- WHITE BACKGROUND CHECK ---
brightness = bg_pixels.mean(axis=1)
white_pixels = np.sum(brightness > 200)
white_ratio = white_pixels / len(bg_pixels)

# --- UNIFORMITY CHECK ---
brightness = bg_pixels.mean(axis=1) / 255.0
bg_variance = float(np.var(brightness))

if white_ratio < MIN_WHITE_RATIO:
    print(json.dumps({
        "ok": False,
        "faces": 1,
        "white_ratio": round(white_ratio, 2),
        "reason": "background_not_white"
    }))
    sys.exit(0)

if bg_variance > MAX_BG_VARIANCE:
    print(json.dumps({
        "ok": False,
        "faces": 1,
        "bg_variance": round(bg_variance, 2),
        "reason": "background_not_uniform"
    }))
    sys.exit(0)

# --- EYE DETECTION (after face detection, before blur check) ---
face_roi_gray = gray[y:y+fh, x:x+fw]
eye_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_eye.xml"
)
eyes = eye_cascade.detectMultiScale(
    face_roi_gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(int(fw * 0.15), int(fh * 0.15))  # Eyes should be at least 15% of face size
)

if len(eyes) < 2:
    print(json.dumps({
        "ok": False,
        "faces": 1,
        "eyes_detected": len(eyes),
        "reason": "eyes_not_visible"
    }))
    sys.exit(0)

# --- BLUR DETECTION ---
def blur_score(image_bgr):
    gray = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2GRAY)
    return cv2.Laplacian(gray, cv2.CV_64F).var()

face_roi = img[y:y+fh, x:x+fw] # check for blur in facial region
blur = blur_score(face_roi)

if blur < MIN_BLUR_SCORE:
    print(json.dumps({
        "ok": False,
        "faces": 1,
        "blur_score": round(blur, 1),
        "reason": "image_blurry"
    }))
    sys.exit(0)

# --- SUCCESS ---
print(json.dumps({
    "ok": True,
    "faces": 1,
    "white_ratio": round(white_ratio, 2),
    "bg_variance": round(bg_variance, 2),
    "face_box": [int(x), int(y), int(fw), int(fh)],
    "blur": round(blur, 2)
}))
