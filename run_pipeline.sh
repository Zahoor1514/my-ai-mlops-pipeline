#!/bin/bash
echo "=== [🚀] Starting Automated Containerized MLOps Loop ==="

# Step 1: Run Data Validation Pipeline
python data_pipeline.py
if [ $? -ne 0 ]; then echo "[❌] Ingestion Phase Failed"; exit 1; fi

# Step 2: Trigger Model Re-Training
python train_model.py
if [ $? -ne 0 ]; then echo "[❌] Training Phase Failed"; exit 1; fi

# Step 3: Initialize Micro-Service Prediction Validation
python serve_model.py
if [ $? -ne 0 ]; then echo "[❌] Model Serving Failed"; exit 1; fi

# Step 4: Execute Statistical Drift Gates Observability
python monitor_drift.py
if [ $? -ne 0 ]; then echo "[❌] Monitoring/Drift Phase Failed"; exit 1; fi

echo "=== [🟢] Containerized MLOps Sequence Completed Successfully! ==="
