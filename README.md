# 🏥 AI-Driven Healthcare Anomaly Detection Platform

An **end-to-end real-time healthcare monitoring system** that detects abnormal patient vital signs using **machine learning, Apache Kafka streaming, PostgreSQL, and an interactive Flask dashboard**.

This project demonstrates how **AI + real-time data streaming** can be used to identify potential health risks early and assist in clinical monitoring systems.

---

# 🚀 Project Overview

Traditional healthcare monitoring systems rely on **fixed thresholds** and **manual observation**.
This platform uses **machine learning-based anomaly detection** to continuously monitor patient vital signs and detect unusual physiological patterns automatically.

The system processes **live streaming data**, analyzes it using an **Isolation Forest model**, and displays anomalies on a **real-time dashboard**.

---

# 🧠 Key Features

✅ **Real-time patient vitals streaming using Apache Kafka**
✅ **Machine learning anomaly detection (Isolation Forest)**
✅ **Sliding window temporal analysis for physiological trends**
✅ **Automated email alerts for critical health anomalies**
✅ **PostgreSQL database for storing anomaly logs**
✅ **Interactive Flask dashboard for monitoring**
✅ **Real-time visualization using Chart.js**
✅ **Patient vital sign trend analysis**

---

# ⚙️ Tech Stack

### 👩‍💻 Programming

* Python

### 🤖 Machine Learning

* Scikit-learn (Isolation Forest)

### 📊 Data Processing

* Pandas
* NumPy

### 🔄 Real-Time Streaming

* Apache Kafka

### 🗄 Database

* PostgreSQL

### 🌐 Backend

* Flask

### 📈 Visualization

* Chart.js

### 🛠 Tools

* Git & GitHub
* VS Code

---

# 🏗 System Architecture

The platform follows a **real-time data pipeline architecture**.

```text
Patient Dataset
       │
       ▼
Kafka Producer
(Simulated Patient Vitals)
       │
       ▼
Kafka Topic (patient_vitals)
       │
       ▼
Kafka Consumer
       │
       ▼
Machine Learning Model
(Isolation Forest)
       │
       ▼
Severity Classification
       │
       ▼
PostgreSQL Database
(anomaly_logs)
       │
       ▼
Flask Backend API
       │
       ▼
Real-Time Monitoring Dashboard
```

---

# 📂 Project Structure

```text
AI-Based-Anomaly-Detection-Platform
│
├── app
│   └── app.py
│
├── producer
│   └── vitals_producer.py
│
├── consumer
│   └── vitals_consumer.py
│
├── models
│   └── isolation_forest.pkl
│
├── database
│   └── human_vital_signs_dataset_2024.csv
│
├── templates
│   └── dashboard.html
│
├── static
│   └── style.css
│
├── requirements.txt
└── README.md
```

---

# 📊 Dataset

The project uses the **Human Vital Signs Dataset** containing simulated patient physiological data.

### Vital Parameters Included

• ❤️ Heart Rate
• 🫁 Respiratory Rate
• 🌡 Body Temperature
• 🫀 Oxygen Saturation (SpO₂)
• 💉 Blood Pressure
• 📉 HRV (Heart Rate Variability)
• 📈 MAP (Mean Arterial Pressure)

📌 Dataset Source:
https://www.kaggle.com/datasets/nasirayub2/human-vital-sign-dataset

---

# 🤖 Machine Learning Model

The anomaly detection component uses **Isolation Forest**, an unsupervised learning algorithm that detects anomalies by isolating rare data points.

### Model Workflow

1️⃣ Feature extraction from patient vitals
2️⃣ Feature normalization using **MinMaxScaler**
3️⃣ Sliding window captures temporal physiological behavior
4️⃣ Isolation Forest computes anomaly score
5️⃣ Score is converted into **severity level**

| Score Range    | Severity  |
| -------------- | --------- |
| > -0.02        | 🟢 LOW    |
| -0.02 to -0.06 | 🟡 MEDIUM |
| < -0.06        | 🔴 HIGH   |

---

# 🗄 Database Schema

Detected anomalies are stored in the **PostgreSQL table:**

### `anomaly_logs`

| Column        | Description              |
| ------------- | ------------------------ |
| id            | Primary key              |
| timestamp     | Event time               |
| patient_id    | Patient identifier       |
| anomaly_score | Model score              |
| severity      | Risk category            |
| heart_rate    | Heart rate               |
| spo2          | Oxygen saturation        |
| temperature   | Body temperature         |
| systolic_bp   | Systolic blood pressure  |
| diastolic_bp  | Diastolic blood pressure |

---

# 📊 Dashboard

The dashboard provides **real-time monitoring and visualization** of patient health metrics.

### Dashboard Components

📌 **KPI Cards**

* Active Patients
* High Risk Alerts
* Average Anomaly Score
* Last Detected Alert

📌 **Charts**

* Anomaly Score Trend
* Heart Rate Monitoring
* SpO₂ Monitoring
* Temperature Variation
* Blood Pressure Analysis

📌 **Anomaly Logs Table**

* Timestamp
* Patient ID
* Severity
* Vital Signs

---

# ▶️ Running the Project

### 1️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 2️⃣ Start Kafka Server

```bash
kafka-server-start.bat config/server.properties
```

### 3️⃣ Start Kafka Consumer

```bash
python consumer/vitals_consumer.py
```

### 4️⃣ Start Kafka Producer

```bash
python producer/vitals_producer.py
```

### 5️⃣ Start Flask Dashboard

```bash
python app/app.py
```

Open in browser:

```
http://127.0.0.1:5000
```

---

# 💡 Example Applications

🏥 Hospital patient monitoring systems
🫀 ICU vital sign anomaly detection
📊 Healthcare data analytics platforms
⌚ Wearable device health monitoring

---

# 🔮 Future Improvements

✨ Deep learning autoencoder anomaly detection
✨ Real-time WebSocket dashboard updates
✨ Patient-specific baseline modeling
✨ Integration with wearable health devices
✨ Explainable AI for anomaly reasoning

---


