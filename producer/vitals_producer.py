from kafka import KafkaProducer
import json
import pandas as pd
import time

# load dataset
df = pd.read_csv("database/human_vital_signs_dataset_2024.csv")

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

topic = "patient_vitals"

for _, row in df.iterrows():

    message = {
    "patient_id": row["Patient ID"],   # add this
    "heart_rate": row["Heart Rate"],
    "resp_rate": row["Respiratory Rate"],
    "temperature": row["Body Temperature"],
    "spo2": row["Oxygen Saturation"],
    "systolic_bp": row["Systolic Blood Pressure"],
    "diastolic_bp": row["Diastolic Blood Pressure"],
    "hrv": row["Derived_HRV"],
    "map": row["Derived_MAP"]
}

    producer.send(topic, message)

    print("Sent:", message)

    time.sleep(1)