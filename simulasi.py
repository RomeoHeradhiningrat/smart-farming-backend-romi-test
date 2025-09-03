import requests
import random
import time

# Ganti sesuai dengan URL Railway kamu
URL = "https://web-production-ecd56.up.railway.app/sensor"

while True:
    data = {
        "temperature": round(random.uniform(25, 35), 2),
        "humidity": round(random.uniform(60, 80), 2)
    }
    try:
        r = requests.post(URL, json=data)
        print("Sent:", data, "Response:", r.json())
    except Exception as e:
        print("Error:", e)
    time.sleep(5)  # kirim tiap 5 detik
