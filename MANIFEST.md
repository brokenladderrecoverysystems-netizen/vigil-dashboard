# Vigil Amulet: Technical Manifest & Security Protocol
**Project:** Broken Ladder Recovery Systems 
**Version:** 1.0.0-Alpha
**Status:** Initial Infrastructure (Phase 1)

## 1. System Overview
The Amulet is an edge-AI wearable designed for recovery support. It utilizes a TinyML model manager to process biometric signals (PPG, GSR, Temp) on-device to ensure user privacy and low latency.

## 2. Model Integrity & Signing
To prevent unauthorized or malicious firmware updates, all TinyML model updates must pass a three-tier verification process:

* **Schema Validation:** Ensures the update matches the `0001-tinyml-update` manifest schema.
* **Cryptographic Signing:** Every model is digitally signed at the backend before publication.
* **On-Device Verification:** The Amulet’s `ModelManager` verifies the signature locally before activation.

## 3. Data Privacy (The "Dignity" Standard)
* **Edge Processing:** Raw biometric streams (heart rate, skin conductance) are processed on the ring.
* **Event-Based Reporting:** Only compliance metrics and emergency alerts are transmitted to the Vigil Dashboard.
* **Zero Raw Storage:** No raw biometric data is stored long-term, reducing HIPAA liability.

## 4. Current Development Roadmap
| Component | Status | Target |
| :--- | :--- | :--- |
| Manifest Schema | In Progress | Data structure for biometric signing |
| Model Manager | Skeleton | Core verify/install/activate logic |
| Backend API | Planning | Model pull endpoints for edge updates |

