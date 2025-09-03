from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# Simpan data sensor & device di memory (sementara)
sensor_data = []
device_status = {"led": "OFF"}

@app.route("/")
def home():
    return "Smart Farming API - Running ✅"

# Endpoint untuk kirim data sensor
@app.route("/sensor", methods=["POST"])
def sensor():
    data = request.json
    if not data or "temperature" not in data or "humidity" not in data:
        return jsonify({"error": "Invalid data"}), 400

    entry = {
        "temperature": data["temperature"],
        "humidity": data["humidity"],
        "timestamp": datetime.now().isoformat()
    }
    sensor_data.append(entry)

    return jsonify({"message": "Data received", "data": entry}), 201

# Endpoint untuk ambil data sensor terbaru
@app.route("/latest", methods=["GET"])
def latest():
    if not sensor_data:
        return jsonify({"message": "No data yet"})
    return jsonify(sensor_data[-1])

# Endpoint untuk ubah status device
@app.route("/device", methods=["POST"])
def device():
    data = request.json
    if not data or "led" not in data:
        return jsonify({"error": "Invalid request"}), 400

    device_status["led"] = data["led"].upper()
    return jsonify({"message": "Device status updated", "status": device_status})

# Endpoint untuk cek status device
@app.route("/device", methods=["GET"])
def get_device():
    return jsonify(device_status)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
