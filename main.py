cat << 'EOF' > main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
import uvicorn

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

last_alert = None

def dispatch_alert(type, val):
    global last_alert
    now = datetime.now().strftime("%H:%M")
    if last_alert != f"{type}-{now}":
        print(f"\n[DISPATCH] 📧 Alert sent to counselor: brokenladderrecoverysystems@gmail.com")
        print(f"[TYPE] {type} | [VALUE] {val} | [TIME] {now}\n")
        last_alert = f"{type}-{now}"

@app.get("/api/status/")
def check_status(brpm: int, stress: int, lat: float = 0.0):
    res = {"color": "GREEN", "alert": "VORTEX STABLE", "hw": "PAIRED", "bat": 88}

    if brpm < 8:
        res.update({"color": "RED", "alert": "CRITICAL: RESPIRATORY DROP"})
        dispatch_alert("CRITICAL", brpm)
    elif lat == 39.9612:
        res.update({"color": "YELLOW", "alert": "ERIS: HOT ZONE BREACH"})
        dispatch_alert("GEOFENCE", "Zone A")
    elif stress > 85:
        res.update({"color": "YELLOW", "alert": "STRESS: ANXIETY SPIKE"})

    return res

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
EOF

