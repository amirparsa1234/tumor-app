🧠 Brain Tumor Classifier (FastAPI + TensorFlow Lite)

A lightweight web service for brain tumor classification using a TensorFlow Lite model and FastAPI.
It provides a simple web interface (index.html) for image upload and prediction.

🚀 Quick Start (Docker)

Requirement: Docker

# Clone repository
git clone https:/github.com/amirparsa1234/tumor-app.git

cd tumor-app

# Build image
docker build -t tumor-app .

# Run container
docker run -d --name tumor-app -p 8000:8000 --restart unless-stopped tumor-app


Then open: http://SERVER_IP:8000

To stop/start the container:

docker stop tumor-app
docker start tumor-app


The flag --restart unless-stopped ensures the container auto-starts after a reboot.

🧩 Local Development (without Docker)

Requirements: Python 3.10+ and basic system libraries (libjpeg, libpng, …)
Example (Ubuntu):

sudo apt update
sudo apt install -y python3-venv libglib2.0-0 libjpeg-turbo-progs libpng16-16 zlib1g

git clone https:/github.com/amirparsa1234/tumor-app.git
cd tumor-app

python3 -m venv venv
source venv/bin/activate

pip install -r app/requirements.txt

# Run locally
uvicorn app.main:app --host 0.0.0.0 --port 8000


Visit → http://127.0.0.1:8000

🧠 Quick API Test
curl -I http://127.0.0.1:8000
# expect "200 OK"

curl -F "file=@/path/to/mri.jpg" http://127.0.0.1:8000/predict


⚠️ The .keras model file is not required.
The app only uses the best_model.tflite file for inference (optimized for CPU).

🔁 Updating on Server

When deploying new changes:

cd ~/tumor-app
git pull origin main
docker build -t tumor-app .
docker rm -f tumor-app
docker run -d --name tumor-app -p 8000:8000 --restart unless-stopped tumor-app

⚙️ Troubleshooting

❌ “python-multipart not installed”
Required for file uploads — it’s already in requirements.txt.
If you run locally and see this error:

pip install python-multipart


❌ Port 8000 already in use
Change port when starting:

uvicorn app.main:app --port 8080
# or
docker run -p 8080:8000 ...


❌ App not loading in browser
Rebuild Docker image after adding new static files:

docker build -t tumor-app .


❌ TensorFlow or CPU errors
The container uses CPU-based TensorFlow Lite.
GPU acceleration requires a different base image (not included).

🔒 Clean Repo Guidelines

Large files (datasets, .venv, temp files) are excluded in .gitignore.

Only the lightweight best_model.tflite should remain inside model/.

🧠 Notes

Frontend: basic HTML form for uploading MRI images.

Backend: FastAPI handles /predict endpoint.

Model: TensorFlow Lite inference (CPU-optimized).

Auto-restart: handled by Docker’s --restart unless-stopped.

🔄 Future Improvements

Add Grad-CAM heatmap localization (currently disabled)

Support for GPU / TensorFlow GPU

Add Docker Compose file for easier multi-service deployment
