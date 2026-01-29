---

layout: page
title: Phase 1 Technical Specs
nav_exclude: true

---


# 🛠 Phase 1: Model Manager Architecture
**Project: Vigil Recovery Systems | Device: Amulet Biometric Ring**

### 1. The "Logic Engine" (Standardization)
Phase 1 focuses on the **Referee Logic**—ensuring the system standardizes compliance without removing human judgment.

* **Zero-Leakage PHI:** Data is siloed. Case managers see clinical notes; Leadership sees only aggregate capacity and compliance health.
* **Edge-AI Processing:** Biometric signals (Heart Rate, GSR, Sweat Alcohol) are processed on-device to ensure privacy and reduce latency.

### 2. Threshold & Alert Logic (The Referee)
The Model Manager uses a "Traffic Light" system to reduce staff workload:

| Signal | Logic Trigger | Action Taken |
| :--- | :--- | :--- |
| **🟢 Green** | 100% Biometric presence + No alerts | Auto-generate daily compliance log. |
| **🟡 Yellow** | Abnormal stress (GSR) or missing check-in | Suggest schedule adjustment to staff. |
| **🔴 Red** | Alcohol detected or geofence violation | Immediate incident timeline generated. |

### 3. "Human-in-the-Loop" Policy
* AI **suggests** actions; Staff **approves** them.
* This protects staff morale and ensures legal accountability stays with qualified professionals.

### 4. Security & Governance
* **Audit Logs:** Every AI-generated flag is logged for court-ready reporting.
* **Read-Only Portals:** Established for Probation and Insurance verification without giving access to private therapy data.

---

[Return to Dashboard](./index.html)

