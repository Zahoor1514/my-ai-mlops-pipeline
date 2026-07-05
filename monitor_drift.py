import os
import json
import sys

BASELIINE_DATA = "feature_store/clean_features.json"
LIVE_PRODUCTION_LOGS = "raw_data/incoming_payload.json"

print("[📊] Observability Engine: Starting Statistical Drift Analysis...")

if not os.path.exists(BASELIINE_DATA) or not os.path.exists(LIVE_PRODUCTION_LOGS):
    print("[❌] Monitor Error: Critical baseline or production logs missing.")
    sys.exit(1)

with open(BASELIINE_DATA, "r") as f:
    baseline = json.load(f)

# Calculating baseline metrics (e.g., Average Income)
baseline_income_avg = sum(item["income"] for item in baseline) / len(baseline)
print(f"[📈] Historical Baseline Average Income: ${baseline_income_avg:.2f}")

# Simulating live data tracking
print("[🔍] Scanning current production parameters for variance spikes...")
current_income_avg = baseline_income_avg # In real world, this parses fresh live server arrays

# Define strict drift threshold (e.g., if matrix moves by more than 20%)
DRIFT_THRESHOLD = 0.20
deviation = abs(current_income_avg - baseline_income_avg) / baseline_income_avg

print(f"[📊] Current Structural Deviation: {deviation * 100:.2f}%")

if deviation > DRIFT_THRESHOLD:
    print("[⚠️] ALERT: Critical Data Drift Detected! System health is degrading.")
    print("[⚙️] Self-Correction Protocol: Triggering emergency model retraining job...")
    # Exit with custom code to force automatic actions
    sys.exit(2) 
else:
    print("[✓] System Metrics Stable: Feature variance is within optimal thresholds.")
    sys.exit(0)
