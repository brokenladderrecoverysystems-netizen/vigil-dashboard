#!/bin/bash
cat << 'HTML_EOF' > index.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Vigil - Transparency Portal</title>
    <style>
        body { font-family: 'Segoe UI', sans-serif; background: #0b0e14; color: #fff; margin: 0; padding: 0; }
        nav { background: #161b22; padding: 15px 30px; border-bottom: 1px solid #30363d; display: flex; gap: 20px; }
        nav a { color: #8b949e; text-decoration: none; cursor: pointer; font-size: 0.9em; }
        nav a.active { color: #58a6ff; border-bottom: 2px solid #58a6ff; }
        .container { padding: 40px; max-width: 900px; margin: 0 auto; }
        .card { background: #161b22; padding: 30px; border-radius: 16px; border: 1px solid #30363d; margin-bottom: 20px; }
        .sensor-row { display: flex; justify-content: space-between; padding: 15px 0; border-bottom: 1px solid #21262d; }
        .status-dot { height: 10px; width: 10px; border-radius: 50%; display: inline-block; margin-right: 10px; }
        .dot-on { background-color: #3fb950; box-shadow: 0 0 8px #3fb950; }
        .dot-off { background-color: #8b949e; }
        .badge { background: rgba(88, 166, 255, 0.1); color: #58a6ff; padding: 4px 8px; border-radius: 5px; font-size: 0.8em; }
    </style>
</head>
<body>

<nav>
    <a class="active">CLIENT HANDBOOK & PRIVACY</a>
</nav>

<div class="container">
    <div class="card">
        <h2 style="color:#58a6ff; margin-top:0;">🛡️ Privacy & Sensor Transparency</h2>
        <p style="color:#8b949e; font-size:0.9em;">Live view of the Amulet Ring's active sensor suite. We only collect what is necessary to keep you safe.</p>
        
        <div id="sensor-list"></div>
        
        <div style="margin-top:20px; text-align:right;">
            <small id="sync-time" style="color:#3fb950;"></small>
        </div>
    </div>

    <div class="card">
        <h3>Why this data matters?</h3>
        <p style="color:#8b949e; font-size:0.9em; line-height:1.6;">By sharing your Biometric data (PPG/GSR), our <strong>Sighted Project</strong> can detect a potential overdose or anxiety spike before it becomes a crisis. Your location is only used to help you navigate away from 'Hot Zones' via our ERIS system.</p>
    </div>
</div>

<script>
    async function loadPrivacy() {
        const res = await fetch('http://localhost:8000/api/sensor-privacy/');
        const data = await res.json();
        
        document.getElementById('sync-time').innerText = "Encrypted Sync: " + data.last_encryption_check;
        document.getElementById('sensor-list').innerHTML = data.sensors.map(s => `
            <div class="sensor-row">
                <div>
                    <span class="status-dot ${s.status === 'OFF' || s.status.includes('DISABLED') ? 'dot-off' : 'dot-on'}"></span>
                    <strong>${s.name}</strong>
                </div>
                <div style="text-align:right;">
                    <span class="badge">${s.status}</span>
                    <div style="font-size:0.7em; color:#8b949e; margin-top:5px;">${s.reason}</div>
                </div>
            </div>
        `).join('');
    }

    loadPrivacy();
    setInterval(loadPrivacy, 5000); // Update every 5 seconds
</script>
</body>
</html>
HTML_EOF
echo "✅ Privacy Frontend generated."
