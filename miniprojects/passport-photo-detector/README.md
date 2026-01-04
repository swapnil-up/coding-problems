# Passport Photo Validation – Heuristic Pipeline

## Overview

This repository contains a small, self-contained solution for validating **passport-style photos** using deterministic computer vision heuristics.

The goal is **not biometric verification**, but *pre-validation*: automatically rejecting clearly invalid uploads before they reach human review or downstream systems.

The approach intentionally avoids cloud APIs and heavy ML frameworks. It uses:

* OpenCV (Haar cascades)
* Simple pixel statistics
* Explainable, tunable rules

This makes the system fast, local, auditable, and suitable for regulated or cost-sensitive environments (e.g. exam registration, forms, applications).

---

## What This Solves

The pipeline validates that an uploaded image:

1. Contains **exactly one human face**
2. Has a **reasonable face size and position** (passport-like framing)
3. Uses a **mostly white, uniform background**
4. Is **not blurry**
5. Does **not contain occlusions** such as:

   * Sunglasses
   * Face masks / scarves
   * Objects covering parts of the face

It explicitly rejects:

* Animals
* Objects
* Landscapes
* Group photos
* Dark or patterned backgrounds
* Blurry or low-quality images

---

## Design Philosophy

* Deterministic over probabilistic
* Explainable failures over opaque scores
* Local execution (no network dependency)
* Tunable thresholds over fixed magic values
* "Good gatekeeper" rather than perfect classifier

This is designed to reduce noise and human workload, not to replace final verification.

---

## Validation Flow

#### 1. Image Load

* Attempt to load image via OpenCV
* Fail fast if unreadable or invalid

---

#### 2. Face Detection

* Convert image to grayscale
* Run OpenCV Haar cascade (frontal face)

Rules:

* Exactly **one** face must be detected
* Zero or multiple faces are rejected

Reason codes:

* `face_count`

---

#### 3. Face Size Validation

Compute:

* `face_ratio = face_height / image_height`

Rules:

* Face must occupy a reasonable portion of the image
* Prevents tiny distant faces or extreme close-ups

Typical bounds:

* Minimum: ~20%
* Maximum: ~55%

Reason codes:

* `face_size`

---

#### 4. Face Masking

* Expand face bounding box slightly
* Mask this region out
* All background checks operate **only on non-face pixels**

This prevents white shirts, skin, or lighting on the subject from influencing background validation.

---

#### 5. White Background Check

Using remaining background pixels:

* Compute per-pixel brightness
* Count pixels above a brightness threshold
* Calculate ratio of white-ish pixels

Rules:

* Background must be predominantly white

Reason codes:

* `background_not_white`

---

#### 6. Background Uniformity Check

* Compute brightness variance of background pixels

Rules:

* Low variance indicates a flat wall or backdrop
* High variance indicates patterns, textures, or clutter

Reason codes:

* `background_not_uniform`

---

#### 7. Blur Detection

* Extract face region
* Compute Laplacian variance

Rules:

* Face must exceed a minimum sharpness score

Reason codes:

* `image_blurry`

---

#### 8. Face Occlusion Detection

Heuristic occlusion checks are applied to the detected face region:

##### Upper Face (Eyes / Sunglasses)

* Analyze top portion of face
* Low average brightness indicates sunglasses or heavy shadow

Reason codes:

* `face_occluded_upper`

##### Lower Face (Mask / Scarf)

* Analyze bottom portion of face
* Estimate skin pixel ratio using HSV thresholds
* Low skin ratio indicates masks or coverings

Reason codes:

* `face_occluded_lower`

---

## Output Format

The script outputs a JSON object to stdout.

### Success Example

```json
{
  "ok": true,
  "faces": 1,
  "white_ratio": 0.72,
  "bg_variance": 0.03,
  "face_box": [x, y, w, h],
  "blur": 185.4
}
```

### Failure Example

```json
{
  "ok": false,
  "faces": 0,
  "reason": "face_count"
}
```

This format is designed to be consumed easily by backend services (e.g. Laravel via `exec`).

---

## Known Limitations

This system intentionally accepts some imperfections:

* Non-frontal or heavily angled faces may be rejected
* Printed photos or posters may pass if well-framed
* Very bright sunglasses may bypass occlusion checks
* Some valid photos may be rejected and require re-upload

These are acceptable trade-offs for a fast, local pre-validation layer.

---

## When This Is Appropriate

* Exam registration systems
* Application forms
* KYC pre-checks
* Upload validation before human review

## When This Is Not Appropriate

* Biometric identity verification
* Legal-grade facial recognition
* Liveness detection

---

## Summary

This project demonstrates how far simple, well-chosen heuristics can go when combined carefully:

* Face detection for structure
* Pixel statistics for background validation
* Region-based analysis for occlusion detection

The result is a lightweight, explainable, and surprisingly robust passport-photo validator suitable for real-world production use as a first-line filter.
