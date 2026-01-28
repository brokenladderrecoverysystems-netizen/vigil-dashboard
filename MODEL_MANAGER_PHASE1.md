# Model Manager: Phase 1 (Core Infrastructure)
**Component:** Vigil On-Device Security Layer
**Milestone:** Initial Edge-AI Implementation

## 1. The Verification Engine (Signing)
To protect participants from unauthorized firmware changes, the Model Manager utilizes a **Manifest-First** protocol. 
* **Model Authenticity:** Every recovery-tracking model is signed with a private key at the Broken Ladder Backend.
* **On-Ring Check:** The `ModelManager` checks the signature against the `0001-tinyml-update` schema before installation.

## 2. Active APIs (Current Sprint)
We are currently implementing the following core endpoints for the Amulet ring:

* `verify()`: Cross-references the downloaded model hash with the signed manifest.
* `install()`: Unpacks the verified TinyML model into the ring's secure execution environment.
* `activate()`: Seamlessly switches from the old behavioral baseline to the updated recovery model without data gaps.

## 3. Biometric Integrity
Phase 1 ensures that **GSR (Stress)** and **PPG (Heart Rate)** sensors are calibrated via the `Manifest Schema` to prevent false positives in relapse detection.

