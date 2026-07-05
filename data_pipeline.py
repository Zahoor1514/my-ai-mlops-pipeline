import os
import json
import sys

RAW_DATA_PATH = "raw_data/incoming_payload.json"
CLEAN_STORE_PATH = "feature_store/clean_features.json"
LOG_DIR = "logs"

print("[⚙️] MLOps Ingestion Pipeline Initialized.")
print(f"[🔍] Scanning Inbound Features from: {RAW_DATA_PATH}\n")

if not os.path.exists(RAW_DATA_PATH):
    print(f"[❌] Fatal: Source ingestion payload missing at {RAW_DATA_PATH}")
    sys.exit(1)

# Read incoming telemetry/user features
with open(RAW_DATA_PATH, "r") as f:
    raw_dataset = json.load(f)

clean_records = []
corrupted_records = []

# Core Data Engineering Validation Rules Matrix
for record in raw_dataset:
    user_id = record.get("user_id")
    age = record.get("age")
    income = record.get("income")
    risk_score = record.get("risk_score")
    
    # Validation Integrity Gates
    if age <= 0 or age > 120:
        corrupted_records.append({"user_id": user_id, "reason": f"Invalid age value: {age}"})
        continue
    if income < 0:
        corrupted_records.append({"user_id": user_id, "reason": f"Negative income anomalies: {income}"})
        continue
    if risk_score < 0.0 or risk_score > 1.0:
        corrupted_records.append({"user_id": user_id, "reason": f"Risk score out of mathematical limits: {risk_score}"})
        continue
        
    # If all checks pass, data moves to the safe zone
    clean_records.append(record)

# Executive Actions: Saving Data States
os.makedirs("feature_store", exist_ok=True)
os.makedirs(LOG_DIR, exist_ok=True)

with open(CLEAN_STORE_PATH, "w") as f:
    json.dump(clean_records, f, indent=2)

with open(f"{LOG_DIR}/pipeline_anomalies.log", "w") as f:
    json.dump(corrupted_records, f, indent=2)

print(f"[✓] Data Pipeline Step Complete.")
print(f"    - Clean Records Ingested into Feature Store: {len(clean_records)}")
print(f"    - Corrupted Anomalies Dropped & Logged: {len(corrupted_records)}\n")

if len(clean_records) == 0:
    print("[❌] Pipeline Halted: Zero valid samples found for AI execution.")
    sys.exit(1)

print("[🎉] Success: Feature Matrix locked. Ready for Phase 2 Model Architecture Loop.")
sys.exit(0)
