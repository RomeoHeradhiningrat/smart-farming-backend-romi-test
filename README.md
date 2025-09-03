# 🌱 Smart Farming Backend

Backend sederhana untuk simulasi **Smart Farming** menggunakan Flask, Railway, Telegram Bot, dan Dashboard Vercel.

## 🚀 Fitur
- Kirim data sensor (temperature, humidity)
- Ambil data sensor terbaru
- Ubah status device (contoh: LED ON/OFF)
- Ambil status device

## 🔧 Endpoint
- `POST /sensor` → kirim data sensor
- `GET /latest` → ambil data sensor terbaru
- `POST /device` → ubah status device ({"led": "ON"})
- `GET /device` → lihat status device

## 📦 Cara Jalankan Lokal
```bash
pip install -r requirements.txt
python app.py
