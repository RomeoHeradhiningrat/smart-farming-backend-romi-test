from flask import Flask, request, jsonify
from flask_cors import CORS
import threading
import random
import time
from datetime import datetime

app = Flask(__name__)
CORS(app)

# Simpan data sensor & device di memory
latest_sensor = {
    "temperature": None,
    "humidity": None,
    "timestamp": None
}
device_status = {"led": "OFF"}

# --- ROUTES ---
@app.route("/")
def home():
    return "🌱 Smart Farming Backend is running!"

@app.route("/sensor", methods=["POST"])
def update_sensor():
    global latest_sensor
    data = request.json
    latest_sensor = {
        "temperature": data.get("temperature"),
        "humidity": data.get("humidity"),
        "timestamp": datetime.utcnow().isoformat()
    }
    return jsonify({"status": "ok", "data": latest_sensor})

@app.route("/latest", methods=["GET"])
def get_latest():
    return jsonify(latest_sensor)

@app.route("/device", methods=["GET", "POST"])
def device():
    global device_status
    if request.method == "POST":
        data = request.json
        if "led" in data:
            device_status["led"] = data["led"]
    return jsonify(device_status)

# --- BACKGROUND TASK: generate dummy data otomatis ---
def generate_dummy_data():
    global latest_sensor
    while True:
        latest_sensor = {
            "temperature": round(random.uniform(25, 35), 2),
            "humidity": round(random.uniform(60, 80), 2),
            "timestamp": datetime.utcnow().isoformat()
        }
        time.sleep(5)  # update setiap 5 detik

# Jalankan thread dummy generator
threading.Thread(target=generate_dummy_data, daemon=True).start()

# --- START SERVER ---
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
