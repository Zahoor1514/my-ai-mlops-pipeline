import os
import json
import sys

FEATURE_STORE = "feature_store/clean_features.json"
MODEL_REGISTRY = "models"
MODEL_FILE = f"{MODEL_REGISTRY}/financial_model.bin"

print("[🧠] AI Core: Initiating Model Training Sequence.")
print(f"[🔍] Reading Verified Features From: {FEATURE_STORE}\n")

if not os.path.exists(FEATURE_STORE):
    print(f"[❌] Training Aborted: Feature matrix missing at {FEATURE_STORE}")
    sys.exit(1)

with open(FEATURE_STORE, "r") as f:
    dataset = json.load(f)

print(f"[⚙️] Training on {len(dataset)} valid training samples...")

# Simulated AI Model Training Logic (Calculating Weights weights matrix)
model_weights = {}
for record in dataset:
    user_id = record["user_id"]
    # Simple linear weight approximation logic for financial score
    calculated_score = (record["income"] * 0.001) - (record["age"] * 0.05)
    model_weights[f"user_{user_id}_prediction"] = round(calculated_score, 4)

# Saving the binary artifact to Model Registry
os.makedirs(MODEL_REGISTRY, exist_ok=True)
with open(MODEL_FILE, "w") as f:
    json.dump(model_weights, f, indent=2)

print("\n[✓] Model Optimization Complete.")
print(f"[💾] Binary Model Weights Successfully Saved to Registry: {MODEL_FILE}")
print(f"    - Matrix Elements: {list(model_weights.keys())}")
print("\n[🎉] Phase 2 Finished: Model weights registry updated and ready for Production Serving!")
sys.exit(0)
