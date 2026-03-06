from flask import Flask, render_template, jsonify
import psycopg2

app = Flask(__name__,
            template_folder='../templates',
            static_folder='../static')

anomaly_logs = [
    {"patient_id": "P001", "heart_rate": 155, "spo2": 78, "severity": "HIGH"},
    {"patient_id": "P002", "heart_rate": 120, "spo2": 90, "severity": "MEDIUM"},
    {"patient_id": "P003", "heart_rate": 85, "spo2": 97, "severity": "LOW"}
]


@app.route("/")
def dashboard():
    return render_template("dashboard.html")


@app.route("/api/anomalies")
def get_anomalies():

    conn = psycopg2.connect(
        host="localhost",
        database="healthcare_ai",
        user="postgres",
        password="Curriculum1#"
    )

    cursor = conn.cursor()

    cursor.execute("""
    SELECT timestamp, patient_id, anomaly_score, severity,
           heart_rate, spo2, temperature, systolic_bp, diastolic_bp
    FROM anomaly_logs
    ORDER BY timestamp DESC
    LIMIT 100
    """)

    rows = cursor.fetchall()

    anomalies = []

    for r in rows:
        anomalies.append({
            "timestamp": str(r[0]),
            "patient_id": r[1],
            "score": r[2],
            "severity": r[3],
            "heart_rate": r[4],
            "spo2": r[5],
            "temperature": r[6],
            "bp": f"{int(r[7])}/{int(r[8])}"
        })

    conn.close()

    return jsonify(anomalies)


if __name__ == "__main__":
    app.run(debug=True)