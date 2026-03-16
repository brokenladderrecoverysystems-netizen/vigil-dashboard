#!/bin/bash
cat << 'PY_EOF' > main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from datetime import datetime

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/sensor-privacy/")
def get_sensor_status():
    return {
        "privacy_mode": "ACTIVE",
        "sensors": [
            {"name": "PPG (Heart Rate)", "status": "ON", "reason": "Life-Safety Monitoring"},
            {"name": "GSR (Stress)", "status": "ON", "reason": "Wellness Trends"},
            {"name": "GPS (Location)", "status": "ACTIVE (ERIS)", "reason": "Hot Zone Protection"},
            {"name": "Microphone", "status": "DISABLED", "reason": "Not required for recovery"},
            {"name": "Camera", "status": "NOT PRESENT", "reason": "Hardware Dignity Standards"}
        ],
        "last_encryption_check": str(datetime.now().strftime("%H:%M:%S"))
    }

@app.get("/api/handbook/")
def get_handbook():
    return {
        "title": "Amulet & Vigil: Dignity First Handbook",
        "philosophy": "Transparency is the foundation of trust.",
        "rights": [
            "Right to Data Transparency",
            "Right to Privacy",
            "Right to Response"
        ]
    }

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
PY_EOF
echo "✅ Privacy-Enabled Backend generated."
