# AI-Based Anomaly Detection Platform

## Project Overview
The **AI-Based Anomaly Detection Platform** is a real-time healthcare monitoring system designed to detect abnormal patterns in patient vital signs and generate alerts.

The system continuously analyzes physiological data such as:

- Heart Rate
- Oxygen Saturation (SpO₂)
- Body Temperature
- Blood Pressure

using **machine learning models**.

---

## System Architecture

Patient Vitals → Kafka Producer → Kafka Topic → Kafka Consumer → ML Model → PostgreSQL Database → Flask Backend → Dashboard & Email Alerts

---

## Key Features

- Real-time patient vitals streaming using **Apache Kafka**
- Anomaly detection using **Isolation Forest** and **Autoencoder Neural Network**
- Severity classification (**LOW, MEDIUM, HIGH**)
- Data storage using **PostgreSQL**
- Backend APIs built with **Flask**
- Interactive dashboard for monitoring patient vitals
- Automated email alerts for critical anomalies

---

## Technologies Used

- **Python** – Core programming language
- **Apache Kafka** – Real-time data streaming
- **PostgreSQL** – Database storage
- **Flask** – Backend API and dashboard
- **Scikit-learn** – Isolation Forest anomaly detection
- **TensorFlow / Keras** – Autoencoder neural network
- **Pandas / NumPy** – Data preprocessing
- **Matplotlib** – Visualization support

---

## Project Setup

### Clone Repository
git clone <repository-link>

### Create Virtual Environment
python -m venv venv

### Activate Virtual Environment
venv\Scripts\activate


### Install Dependencies
pip install -r requirements.txt



## Project Structure

```
AI-Based-Anomaly-Detection-Platform
│
├── alerts/        # Email alert system
├── backend/       # Flask backend APIs
├── consumer/      # Kafka consumer for real-time data processing
├── dashboard/     # Web dashboard interface
├── database/      # Dataset and database scripts
├── models/        # Machine learning models
├── producer/      # Kafka producer for streaming patient vitals
├── venv/          # Python virtual environment
│
├── dataset_validation.ipynb   # Dataset validation notebook
├── requirements.txt           # Python dependencies
├── README.md                  # Project documentation
```
