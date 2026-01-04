import subprocess
import json
import os

TEST_DIR = "passport/test_images"
SCRIPT = "passport/passport_check.py"

stats = {
    "TP": 0,
    "TN": 0,
    "FP": 0,
    "FN": 0,
}

details = []

def run_check(image_path):
    result = subprocess.run(
        ["python3", SCRIPT, image_path],
        capture_output=True,
        text=True
    )
    return json.loads(result.stdout)

for expected in ["valid", "invalid"]:
    folder = os.path.join(TEST_DIR, expected)

    for file in os.listdir(folder):
        if not file.lower().endswith((".jpg", ".jpeg", ".png", ".avif", "webp")):
            continue

        path = os.path.join(folder, file)
        output = run_check(path)

        actual_ok = output.get("ok", False)

        if expected == "valid":
            if actual_ok:
                stats["TP"] += 1
            else:
                stats["FN"] += 1
        else:
            if actual_ok:
                stats["FP"] += 1
            else:
                stats["TN"] += 1

        details.append({
            "file": path,
            "expected": expected,
            "actual": "valid" if actual_ok else "invalid",
            **output 
        })

# --- REPORT ---
total = sum(stats.values())
accuracy = (stats["TP"] + stats["TN"]) / total if total else 0

print("\n=== RESULTS ===")
for k, v in stats.items():
    print(f"{k}: {v}")

print(f"\nAccuracy: {accuracy:.2%}")

print("\n--- False Negatives (valid rejected) ---")
for d in details:
    if d["expected"] == "valid" and d["actual"] == "invalid":
        print(d)

print("\n--- False Positives (invalid accepted) ---")
for d in details:
    if d["expected"] == "invalid" and d["actual"] == "valid":
        print(d)
