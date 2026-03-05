# AI-Based-Anomaly-Detection-Platform
AI-Based Anomaly Detection Platform
Project Overview

The AI-Based Anomaly Detection Platform is a real-time healthcare monitoring system designed to detect abnormal patterns in patient vital signs and generate early alerts. The system continuously analyzes physiological data streams such as heart rate, oxygen saturation (SpO₂), body temperature, and blood pressure using machine learning models.

Instead of relying on static thresholds, the platform uses advanced anomaly detection algorithms to identify unusual patterns in real time and notify healthcare administrators about potential health risks.

System Architecture

Patient Vitals → Kafka Producer → Kafka Topic → Kafka Consumer → ML Model → PostgreSQL Database → Flask Backend → Dashboard & Email Alerts

Key Features

Real-time patient vitals streaming using Apache Kafka

Anomaly detection using Isolation Forest and Autoencoder Neural Network

Severity classification (LOW, MEDIUM, HIGH)

Data storage using PostgreSQL

Backend APIs built with Flask

Interactive dashboard for monitoring patient vitals

Automated email alerts for critical anomalies

Technologies Used
Technology	Purpose
Python	- Core programming language
Apache Kafka	 - Real-time data streaming
PostgreSQL - 	Database storage
Flask - 	Backend API and dashboard
Scikit-learn - Isolation Forest anomaly detection
TensorFlow / Keras - Autoencoder neural network
Pandas / NumPy - Data preprocessing
Matplotlib -	Visualization support

Project Setup
1 Clone the Repository
git clone <repository-link>
cd AI-Based-Anomaly-Detection-Platform

2 Create Virtual Environment
python -m venv venv

3 Activate Virtual Environment
Windows:
venv\Scripts\activate

4 Install Dependencies
pip install -r requirements.txt

venv\Scripts\activate
4 Install Dependencies
pip install -r requirements.txt
