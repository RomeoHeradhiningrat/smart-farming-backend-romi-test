from flask import Flask, request, jsonify

app = Flask(__name__)

# simpan data sensor terakhir
latest_data = {"temperature": None, "humidity": None}

@app.route("/sensor", methods=["POST"])
def receive_sensor():
    global latest_data
    data = request.get_json()
    latest_data = data
    return jsonify({"status": "success", "received": data})

@app.route("/api/data", methods=["GET"])
def get_data():
    return jsonify(latest_data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
