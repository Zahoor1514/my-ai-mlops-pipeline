import os
import sqlite3
import numpy as np
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Autonomous MLOps AI Engine", version="2.0")

# Database initialization (Lightweight embedded relation layer)
DB_PATH = "feature_store/production.db"
os.makedirs("feature_store", exist_ok=True)

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS features 
                      (id INTEGER PRIMARY KEY AUTOINCREMENT, income REAL, approval_score REAL)''')
    conn.commit()
    conn.close()

init_db()

class InferencePayload(BaseModel):
    income: float

@app.get("/")
def read_root():
    return {"status": "🟢 Online", "engine": "MLOps Docker Container v2.0"}

@app.post("/predict")
def predict(payload: InferencePayload):
    # Phase 3 Sim: Load weights & dynamic trigger
    # Mocking execution loop from serve_model.py
    base_score = 50.0
    computed_index = base_score + (payload.income / 5000)
    status = "🟢 HIGH APPROVAL PROBABILITY" if computed_index > 55 else "🔴 REVIEW REQUIRED"
    
    # Live Database Layer Save (Option 2)
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO features (income, approval_score) VALUES (?, ?)", (payload.income, computed_index))
        conn.commit()
        conn.close()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database write failed: {str(e)}")

    return {
        "user_income": payload.income,
        "financial_index_score": round(computed_index, 2),
        "status": status,
        "database_sync": "✓ Ingested to production.db"
    }

@app.get("/metrics")
def get_metrics():
    # Phase 4 Sim: Drift observation scanning relation logs
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT income FROM features")
    rows = cursor.fetchall()
    conn.close()
    
    incomes = [r[0] for r in rows]
    if not incomes:
        return {"metrics": "No production data available yet.", "structural_deviation": "0.00%"}
    
    baseline_avg = 75000.00
    current_avg = np.mean(incomes)
    deviation = abs(baseline_avg - current_avg) / baseline_avg * 100
    
    return {
        "total_live_requests_logged": len(incomes),
        "historical_baseline_avg": baseline_avg,
        "current_production_avg": round(current_avg, 2),
        "structural_deviation": f"{round(deviation, 2)}%",
        "status": "🟢 STABLE" if deviation < 10 else "🚨 DRIFT DETECTED"
    }
