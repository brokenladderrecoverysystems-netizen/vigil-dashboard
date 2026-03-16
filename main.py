from fastapi import FastAPI
from datetime import datetime
import uvicorn

# --- VIGIL HARDWARE MANIFEST ---
AMULET_HARDWARE = {
    "device_name": "Amulet Smart Ring",
    "sensors": {
        "ppg": "Photoplethysmography (Heart Rate, HRV, Breathing)",
        "gsr": "Galvanic Skin Response (Stress/Anxiety)",
        "temp": "Skin Temperature (Overdose/Illness)",
        "motion": "6-Axis Accelerometer (Fall Detection)"
    },
    "compliance": {
        "billing": ["CPT 99454", "CPT 99457", "CPT T2003", "H0038"],
        "jurisdiction": "Ohio Department of Medicaid"
    }
}

# Initialize the Web Server
app = FastAPI(title="Vigil Backend API", version="4.0.0-Web")

class VigilEngine:
    def __init__(self):
        self.specs = AMULET_HARDWARE
        self.is_locked = True
        self.authorized_user_ppg = "SIGNATURE_776"

    def unlock(self, signature: str):
        """Pillar 4: Biometric Fraud Prevention"""
        if signature == self.authorized_user_ppg:
            self.is_locked = False
            return {"status": "SUCCESS", "message": "User Verified. System Unlocked."}
        return {"status": "DENIED", "message": "Unauthorized User."}

    def get_traffic_light(self, brpm: int, stress_level: int):
        """Pillar 1 & 5: Biometrics & UI Traffic Light"""
        if self.is_locked: 
            return {"error": "System Locked. Vitals offline."}
        
        if brpm < 8:
            return {"color": "RED", "alert": "Critical Vitals (Overdose Risk). Alerting EMS."}
        elif stress_level > 80:
            return {"color": "YELLOW", "alert": "High Stress/Craving. Triggering Peer Support."}
        return {"color": "GREEN", "alert": "Vitals Stable. Client Compliant."}

    def log_billing(self, trip_id: str, miles: float):
        """Pillar 3: Medicaid Transportation Billing"""
        if self.is_locked: 
            return {"error": "System Locked. Cannot log billing."}
        
        now = datetime.now().strftime("%H:%M:%S")
        return {
            "receipt": f"Trip {trip_id} | {miles} mi", 
            "status": "Ready for Ohio Medicaid", 
            "timestamp": now
        }

# Instantiate the Engine
engine = VigilEngine()

# --- WEB ENDPOINTS ---

@app.get("/")
def read_root():
    return {
        "system": "Vigil API Active", 
        "version": "4.0.0-Web",
        "device": AMULET_HARDWARE["device_name"]
    }

@app.post("/api/unlock/{signature}")
def unlock_system(signature: str):
    return engine.unlock(signature)

@app.get("/api/status/")
def check_vitals(brpm: int, stress: int):
    return engine.get_traffic_light(brpm, stress)

@app.post("/api/billing/")
def submit_billing(trip_id: str, miles: float):
    return engine.log_billing(trip_id, miles)

if __name__ == "__main__":
    print("Starting Vigil API Server on Columbus Local Network...")
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
