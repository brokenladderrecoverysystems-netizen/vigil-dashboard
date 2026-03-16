from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import json
import os
from datetime import datetime

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

DB_FILE = "vigil_history.json"

@app.get("/api/handbook/")
def get_handbook():
    return {
        "title": "Amulet & Vigil: Dignity First Handbook",
        "philosophy": "We believe recovery is built on trust, not just tracking. This technology exists to catch you when you fall, not to push you down.",
        "rights": [
            "Right to Data Transparency: You can see what your P.O. sees.",
            "Right to Privacy: Sensors focus on life-safety, not lifestyle monitoring.",
            "Right to Response: You have the right to explain biometric spikes.",
            "Right to Support: Every alert is a call for help, not a reason for punishment."
        ],
        "protocols": {
            "haptic_alert": "If your ring vibrates, it means your vitals are unstable or you have a message. Double-tap the ring to acknowledge receipt.",
            "emergency_dispatch": "In the event of a respiratory drop, emergency services and your peer support lead are notified automatically."
        }
    }

@app.post("/api/acknowledge/")
def acknowledge_message(message_id: str):
    print(f"\n[AMULET FEEDBACK] Client confirmed receipt of Message ID: {message_id}\n")
    return {"status": "CONFIRMED", "timestamp": str(datetime.now())}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
