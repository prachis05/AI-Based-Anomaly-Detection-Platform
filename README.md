AI-Driven Healthcare Anomaly Detection Platform
Overview

The AI-Driven Healthcare Anomaly Detection Platform is a real-time monitoring system designed to detect abnormal patterns in patient vital signs using machine learning. The system continuously streams patient physiological data, analyzes it using anomaly detection models, and provides alerts and visual monitoring through an interactive dashboard.

Unlike traditional healthcare monitoring systems that rely on fixed thresholds, this platform applies machine learning techniques to detect unusual patterns in vital signs such as heart rate, oxygen saturation, temperature, and blood pressure.

The system integrates real-time data streaming, anomaly detection models, database storage, and a web dashboard to demonstrate how AI can assist in early detection of potential health risks.

Key Features

Real-time patient vitals streaming using Apache Kafka

Machine learning based anomaly detection using Isolation Forest

Sliding window analysis for temporal anomaly detection

PostgreSQL database to store detected anomalies

Email alerts for high-risk anomalies

Interactive dashboard for monitoring patient health metrics

Visualization of vital signs trends using Chart.js

REST API built with Flask

System Architecture

The system follows a real-time data pipeline architecture:

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
Technologies Used
Programming Language

Python

Machine Learning

Scikit-learn (Isolation Forest)

Data Processing

Pandas

NumPy

Streaming Platform

Apache Kafka

Database

PostgreSQL

Backend

Flask

Visualization

Chart.js

Development Tools

Visual Studio Code

Git & GitHub

Project Structure
AI-Based-Anomaly-Detection-Platform
│
├── app
│   └── app.py                # Flask backend
│
├── producer
│   └── vitals_producer.py    # Kafka producer for streaming vitals
│
├── consumer
│   └── vitals_consumer.py    # Kafka consumer + ML inference
│
├── models
│   └── isolation_forest.pkl  # Trained anomaly detection model
│
├── database
│   └── human_vital_signs_dataset_2024.csv
│
├── templates
│   └── dashboard.html        # Monitoring dashboard UI
│
├── static
│   └── style.css             # Dashboard styling
│
├── requirements.txt
└── README.md
Dataset

The system uses the Human Vital Signs Dataset from Kaggle which contains simulated patient physiological data.

Vital parameters include:

Heart Rate

Respiratory Rate

Body Temperature

Oxygen Saturation (SpO₂)

Systolic Blood Pressure

Diastolic Blood Pressure

Derived HRV

Derived MAP

Dataset Source:

https://www.kaggle.com/datasets/nasirayub2/human-vital-sign-dataset

Machine Learning Model

The anomaly detection component uses Isolation Forest, an unsupervised learning algorithm designed to detect anomalies by isolating rare patterns in data.

Model Workflow

Vital sign features are extracted

Data is normalized using MinMaxScaler

Sliding window captures temporal behavior

Isolation Forest computes anomaly scores

Severity levels are classified:

Score Range	Severity
> -0.02	LOW
-0.02 to -0.06	MEDIUM
< -0.06	HIGH
Database Schema

Detected anomalies are stored in a PostgreSQL table.

Table: anomaly_logs

Column	Description
id	Primary key
timestamp	Event time
patient_id	Patient identifier
anomaly_score	Model anomaly score
severity	Risk level
heart_rate	Heart rate
spo2	Oxygen saturation
temperature	Body temperature
systolic_bp	Systolic blood pressure
diastolic_bp	Diastolic blood pressure
Dashboard

The dashboard provides real-time visualization of patient health data.

Displayed components:

Active patient monitoring

High-risk anomaly alerts

Average anomaly score

Vital sign trend charts

Severity distribution

Recent anomaly log table

Running the Project
1 Install Dependencies
pip install -r requirements.txt
2 Start Kafka Server
kafka-server-start.bat config/server.properties
3 Start Kafka Consumer
python consumer/vitals_consumer.py
4 Start Kafka Producer
python producer/vitals_producer.py
5 Run Flask Dashboard
python app/app.py

Then open:

http://127.0.0.1:5000
Example Use Cases

Hospital patient monitoring systems

ICU vital sign anomaly detection

Early detection of physiological abnormalities

Real-time healthcare analytics platforms

Future Improvements

Deep learning autoencoder based anomaly detection

Real-time WebSocket streaming dashboard

Patient-specific baseline models

Integration with wearable health devices

Explainable AI for anomaly reasoning
