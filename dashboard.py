import time
import requests

API_URL = "http://localhost:8000"

def render_dashboard():
    while True:
        try:
            # Fetch data cleanly from production metrics engine
            metrics = requests.get(f"{API_URL}/metrics").json()
            
            # Clear screen for live monitoring animation loop
            print("\033[H\033[J", end="")
            print("================================================================")
            print("👑🎨 MLOPS ENTERPRISE REAL-TIME MONITORING DASHBOARD 🎨👑")
            print("================================================================")
            print(f"📡 System Connection  : 🟢 ACTIVE")
            print(f"📊 Total Logged Trans : {metrics.get('total_live_requests_logged', 0)}")
            print(f"📉 Historical Target  : ${metrics.get('historical_baseline_avg', 0)}")
            print(f"📈 Production Running : ${metrics.get('current_production_avg', 0)}")
            print(f"🎛️ Variance Deviation : {metrics.get('structural_deviation', '0%')}")
            print("----------------------------------------------------------------")
            print(f"🚨 ENGINE HEALTH STATUS: {metrics.get('status', 'UNKNOWN')}")
            print("================================================================")
            print("Dashboard auto-refreshing every 2 seconds... (Press Ctrl+C to Exit)")
            
        except Exception:
            print("📡 Connection Status: 🔴 Waiting for API Endpoint Matrix to re-route...")
            
        time.sleep(2)

if __name__ == "__main__":
    render_dashboard()
