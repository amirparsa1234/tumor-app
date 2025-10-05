from pathlib import Path
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse, FileResponse
from starlette.staticfiles import StaticFiles
from .infer import predict

app = FastAPI(title="Brain Tumor Classifier", version="1.0")

APP_DIR = Path(__file__).resolve().parent
STATIC_DIR = APP_DIR / "static"
INDEX_FILE = STATIC_DIR / "index.html"

app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")

@app.get("/", response_class=HTMLResponse)
def index():
    return FileResponse(str(INDEX_FILE)) if INDEX_FILE.exists() else HTMLResponse("<h3>Upload page missing.</h3>")

@app.post("/predict")
async def predict_ep(file: UploadFile = File(...)):
    if not file.content_type or not file.content_type.startswith("image/"):
        raise HTTPException(400, "Please upload an image file.")
    data = await file.read()
    if len(data) > 5 * 1024 * 1024:
        raise HTTPException(413, "File too large (>5MB).")
    return JSONResponse({"filename": file.filename, **predict(data)})
