\# Iris ML Service (Local)



A minimal, reproducible Flask API that serves an Iris KNN model, containerized with Docker and deployable to Minikube/Kubernetes.



\## Prerequisites

\- Python 3.11 (for local dev)

\- Docker Desktop with WSL2 backend

\- Minikube + kubectl



\## 1) Place your trained model

Copy your `iris\_knn\_model.pkl` into `models/iris\_knn\_model.pkl`.



\## 2) Local run (optional)

```bash

pip install -r requirements.txt

python app/app.py

\# http://localhost:8080/healthz



