import joblib
import numpy as np
import pandas as pd
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(title="🧠 MLOps Predictive Frontend Engine")
MODEL_PATH = "predictive_model.pkl"
DATA_LOG_PATH = "live_inference_logs.csv"

@app.get("/", response_class=HTMLResponse)
def serve_ui():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>🧠 AI Live Prediction Panel</title>
        <style>
            body { background-color: #0d1117; color: #c9d1d9; font-family: monospace; margin: 40px; }
            .container { max-width: 600px; background: #161b22; padding: 30px; border-radius: 8px; border: 1px solid #30363d; }
            h1 { color: #58a6ff; }
            .slider-group { margin: 20px 0; }
            label { display: block; margin-bottom: 5px; }
            input[type=range] { width: 100%; }
            button { background: #238636; color: white; border: none; padding: 12px 20px; font-weight: bold; cursor: pointer; border-radius: 6px; width: 100%; font-size: 1.1em; }
            button:hover { background: #2ea043; }
            #result { margin-top: 20px; padding: 15px; background: #21262d; border-radius: 6px; text-align: center; font-size: 1.3em; font-weight: bold; display: none; }
        </style>
        <script>
            async function getPrediction() {
                let f1 = document.getElementById('f1').value;
                let f2 = document.getElementById('f2').value;
                let f3 = document.getElementById('f3').value;
                
                let res = await fetch(`/predict?f1=${f1}&f2=${f2}&f3=${f3}`);
                let data = await res.json();
                
                let resultBox = document.getElementById('result');
                resultBox.style.display = 'block';
                resultBox.innerHTML = `🔮 Prediction Out: <span style="color: #58a6ff;">${data.prediction}</span> (Target Active)`;
            }
        </script>
    </head>
    <body>
        <div class="container">
            <h1>🧠 Live Inference Predictive Controller</h1>
            <p>Adjust neural feature matrix sliders below:</p>
            <div class="slider-group">
                <label>Feature 1 (Density Scaling):</label>
                <input type="range" id="f1" min="0" max="1" step="0.01" value="0.5">
            </div>
            <div class="slider-group">
                <label>Feature 2 (Entropy Variance):</label>
                <input type="range" id="f2" min="0" max="1" step="0.01" value="0.3">
            </div>
            <div class="slider-group">
                <label>Feature 3 (Friction Matrix):</label>
                <input type="range" id="f3" min="0" max="1" step="0.01" value="0.7">
            </div>
            <button onclick="getPrediction()">Execute Real-Time Inference</button>
            <div id="result"></div>
        </div>
    </body>
    </html>
    """

@app.get("/predict")
def predict(f1: float, f2: float, f3: float):
    # Load model dynamically
    try:
        model = joblib.load(MODEL_PATH)
        features = np.array([[f1, f2, f3]])
        pred = int(model.predict(features)[0])
    except Exception:
        pred = 0 # Fallback default
        
    return {"prediction": pred}
