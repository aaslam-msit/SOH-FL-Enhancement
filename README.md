SOH-FL Enhancement: Adaptive Aggregation & Explainable AI for IoT Intrusion Detection

📌 Overview

This project enhances the SOH-FL (Self-labeled Personalized Federated Learning) framework for intrusion detection in heterogeneous IoT environments.
The proposed improvements address key limitations of the original method by introducing:

Adaptive Gamma Selection
SHAP-based Explainable AI (XAI)

🎯 Key Contributions

Eliminated manual tuning of aggregation parameter γ
Improved accuracy and convergence stability
Introduced interpretability into federated intrusion detection
Maintained privacy-preserving distributed learning

📊 Results

Model	Accuracy
SOH-FL	92.38%
Proposed	94.12%
Accuracy improved by 1.74%
Faster convergence (6 rounds vs 15 rounds)
Improved interpretability using SHAP

📈 Visual Results

Accuracy vs Communication Rounds

Effect of Adaptive Gamma

SHAP Feature Importance

📂 Project Structure

SOH-FL-Enhancement/
│
├── paper/ → paper SOH-FL+ (PDF)
├── figures/ → result plots
├── code/ → implementation
├── results/ → evaluation metrics
├── requirements.txt
└── README.md

🧪 Dataset

CICIDS2017 (PortScan subset)

Includes features such as:

Flow Duration
Packet Length
Flow Bytes/s
TCP Flags

⚙️ Installation

pip install -r requirements.txt

▶️ Usage

Example usage for adaptive gamma:

from adaptive_gamma import adaptive_gamma

gamma_indices = adaptive_gamma(cos_similarities)

🧠 Explainability (SHAP)

SHAP is used to interpret model predictions by:

Identifying important features
Explaining why traffic is classified as attack or benign
Improving trust in intrusion detection systems

📄 Paper

The full research paper is available in:

paper/paper SOH-FL+.pdf

👩‍💻 Authors

Ambreen Aslam
Bibi Zahra
Maaz Hassan

Department of Computing, SEECS, NUST

📚 References

W. Lu et al., SOH-FL: Intrusion Detection in Heterogeneous IoT, IEEE IoT Journal, 2025
B. McMahan et al., FedAvg, 2017
S. Lundberg and S. Lee, SHAP, NeurIPS 2017

🚀 Future Work

Real-time intrusion detection
Lightweight explainability for edge devices
Online learning for dynamic IoT environments
