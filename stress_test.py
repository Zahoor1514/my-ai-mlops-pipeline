import time
import random
import requests

API_URL = "http://localhost:8000"
HEADERS = {"X-API-KEY": "SultanSecretKey2026"} # Secured Header Token

print("🚀 Running Authed Load Testing Matrix...")

for i in range(1, 11):
    simulated_income = random.choice([120000, 135000, 140000, 150000]) # Forcing higher delta to check auto-retrain
    payload = {"income": float(simulated_income)}
    
    response = requests.post(f"{API_URL}/predict", json=payload, headers=HEADERS)
    print(f"[Transaction Logged #{i}] Injected Income: ${simulated_income} -> Response Status: {response.status_code}")
    time.sleep(0.3)

print("\n✓ Load simulation complete. Check live dashboard window!")
