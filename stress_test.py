import time
import random
import requests

API_URL = "http://localhost:8000"

print("🚀 Starting Production Load & Drift Simulation...")

# Baseline clear check
try:
    root_check = requests.get(f"{API_URL}/")
    print(f"Engine Connection: {root_check.json()['status']}")
except Exception:
    print("❌ Error: Live container is not running on port 8000. Run docker build first!")
    exit(1)

# Simulating 20 production users with fluctuating data metrics
for i in range(1, 21):
    # Generates standard income and randomly spikes it to trigger drift status
    simulated_income = random.choice([65000, 72000, 80000, 115000, 130000])
    
    payload = {"income": float(simulated_income)}
    
    response = requests.post(f"{API_URL}/predict", json=payload)
    data = response.json()
    
    print(f"[Request #{i}] Income: ${simulated_income} -> Score: {data['financial_index_score']} | Status: {data['status']}")
    time.sleep(0.5)  # Half second delay to mimic active users

# Final Metrics and Drift report extraction
print("\n📊 Fetching updated live metrics and systemic deviation analysis:")
metrics_resp = requests.get(f"{API_URL}/metrics").json()
for key, val in metrics_resp.items():
    print(f"👉 {key.replace('_', ' ').title()}: {val}")
