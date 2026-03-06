from kafka import KafkaConsumer
import json
import joblib
import numpy as np
import smtplib
from email.mime.text import MIMEText
import psycopg2

# ------------------------------
# DATABASE CONNECTION
# ------------------------------

conn = psycopg2.connect(
    host="localhost",
    database="healthcare_ai",
    user="postgres",
    password="YOUR PASSWORD HERE"
)

cursor = conn.cursor()

print("Connected to PostgreSQL")

# ------------------------------
# EMAIL CONFIGURATION
# ------------------------------

EMAIL_SENDER = "SENDER'S EMAIL"
EMAIL_PASSWORD = "YOUR PASSWORD HERE"
EMAIL_RECEIVER = "RECEIVER'S EMAIL"


def send_email_alert(patient_id, data, score, explanations):

    subject = "Critical Health Anomaly Detected"

    body = f"""
Critical Health Anomaly Detected

Patient ID: {patient_id}

Anomaly Score: {score}

Heart Rate: {data['heart_rate']}
SpO2: {data['spo2']}
Temperature: {data['temperature']}
Blood Pressure: {data['systolic_bp']}/{data['diastolic_bp']}

Explainability:
"""

    for e in explanations:
        body += f"- {e}\n"

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = EMAIL_SENDER
    msg["To"] = EMAIL_RECEIVER

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(EMAIL_SENDER, EMAIL_PASSWORD)
        server.send_message(msg)
        server.quit()

        print("📧 Email alert sent!")

    except Exception as e:
        print("Email sending failed:", e)


# ------------------------------
# LOAD ML MODELS
# ------------------------------

iso_model = joblib.load("models/isolation_forest.pkl")
scaler = joblib.load("models/scaler.pkl")

print("ML models loaded")

# ------------------------------
# KAFKA CONSUMER
# ------------------------------

consumer = KafkaConsumer(
    "patient_vitals",
    bootstrap_servers="localhost:9092",
    value_deserializer=lambda m: json.loads(m.decode("utf-8"))
)

print("Kafka consumer started")

# ------------------------------
# SEVERITY CLASSIFICATION
# ------------------------------

def classify_severity(score):

    if score > -0.02:
        return "LOW"

    elif score > -0.06:
        return "MEDIUM"

    else:
        return "HIGH"


# ------------------------------
# EXPLAINABILITY
# ------------------------------

def explain_vitals(data):

    explanations = []

    if data["heart_rate"] > 120:
        explanations.append("Heart Rate elevated")

    if data["spo2"] < 92:
        explanations.append("Oxygen saturation decreased")

    if data["temperature"] > 38:
        explanations.append("Body temperature elevated")

    if data["systolic_bp"] > 160:
        explanations.append("Systolic blood pressure elevated")

    return explanations


# ------------------------------
# STREAM PROCESSING
# ------------------------------

from collections import deque

window = deque(maxlen=5)

for message in consumer:

    data = message.value
    patient_id = data.get("patient_id", "unknown")

    vitals = [
        data["heart_rate"],
        data["resp_rate"],
        data["temperature"],
        data["spo2"],
        data["systolic_bp"],
        data["diastolic_bp"],
        data["hrv"],
        data["map"]
    ]

    vitals_scaled = scaler.transform([vitals])[0]

    print("\nReceived:", data)

    # add to sliding window
    window.append(vitals_scaled)

    if len(window) < 5:
        print("Waiting for full window...")
        continue

    # flatten window
    window_array = np.array(window).flatten().reshape(1, -1)

    score = iso_model.decision_function(window_array)[0]

    severity = classify_severity(score)

    print("Anomaly Score:", score)
    print("Severity:", severity)

    # save to database
    cursor.execute("""
    INSERT INTO anomaly_logs
    (patient_id, anomaly_score, severity, heart_rate, spo2, temperature, systolic_bp, diastolic_bp)
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
    """,
    (
        patient_id,
        float(score),
        severity,
        data["heart_rate"],
        data["spo2"],
        data["temperature"],
        data["systolic_bp"],
        data["diastolic_bp"]
    ))

    conn.commit()

    print("Saved anomaly to database")

    if severity == "HIGH":

        explanations = explain_vitals(data)

        print("\n⚠ Health Anomaly Explanation")

        for e in explanations:
            print("-", e)

        send_email_alert(patient_id, data, score, explanations)
