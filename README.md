# 🧠 Brain Tumor Classifier (FastAPI + TensorFlow Lite)

A lightweight web app for **brain tumor classification** built with **FastAPI** and **TensorFlow Lite**.  
Runs entirely on CPU and provides a simple web UI for image upload and prediction.

---

## 🚀 Run with Docker (Recommended)

### 1️⃣ Pull the image
```bash
docker pull amirparsab/tumor-app:latest
```

### 2️⃣ Run the container
```bash
docker run -d --name tumor-app \
  -p 8000:8000 \
  --restart unless-stopped \
  amirparsab/tumor-app:latest
```

Then open your browser at:  
👉 **http://SERVER_IP:8000**

To stop or start later:
```bash
docker stop tumor-app
docker start tumor-app
```

✅ The container auto-starts after reboot (because of `--restart unless-stopped`).

---

## 🧩 API Quick Test

```bash
curl -F "file=@/path/to/mri.jpg" http://127.0.0.1:8000/predict
```

You’ll get a JSON response like:
```json
{
  "top_class": "Glioma",
  "has_tumor": true,
  "probabilities": {
    "Glioma": 0.92,
    "Meningioma": 0.04,
    "Notumor": 0.01,
    "Pituitary": 0.03
  }
}
```

---

## 🧠 Model

The app uses:
- `model/best_model.tflite` → optimized for CPU  
- *(The `.keras` file is no longer needed)*

---

## 🔄 Updating to Latest Version

```bash
docker pull amirparsab/tumor-app:latest
docker rm -f tumor-app
docker run -d --name tumor-app -p 8000:8000 --restart unless-stopped amirparsab/tumor-app:latest
```

---

## 🧱 Tech Stack
- **Backend:** FastAPI (Python 3.11)
- **Model:** TensorFlow Lite (CPU inference)
- **Frontend:** Simple HTML upload form
- **Containerization:** Docker

---

## 🔒 Clean Repository
- Only lightweight model file (`best_model.tflite`) is included  
- No large datasets or virtual environments committed  

---

## 💡 Future Improvements
- Grad-CAM tumor localization  
- GPU-enabled version  
- Multi-service Docker Compose setup
