import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="healthcare_ai",
    user="postgres",
    password="Curriculum1#"
)

cursor = conn.cursor()

cursor.execute("""
INSERT INTO anomaly_logs
(patient_id, anomaly_score, severity, heart_rate, spo2, temperature, systolic_bp, diastolic_bp)
VALUES ('TEST', 1.23, 'HIGH', 120, 88, 38.5, 160, 100)
""")

conn.commit()

print("Inserted successfully")

conn.close()