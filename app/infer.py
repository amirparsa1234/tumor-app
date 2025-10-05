# app/infer.py
import io
from pathlib import Path
import numpy as np
from PIL import Image, ImageOps
import tflite_runtime.interpreter as tflite

IMG_H, IMG_W = 168, 168
CLASSES = ["Glioma", "Meninigioma", "Notumor", "Pituitary"]
TUMOR_CLASSES = ["Glioma", "Meninigioma", "Pituitary"]

BASE_DIR = Path(__file__).resolve().parents[1]
TFLITE_PATH = BASE_DIR / "model" / "best_model.tflite"
assert TFLITE_PATH.exists(), f"Model not found at {TFLITE_PATH}"

INTERP = tflite.Interpreter(model_path=str(TFLITE_PATH))
INTERP.allocate_tensors()
INP = INTERP.get_input_details()[0]
OUT = INTERP.get_output_details()[0]

def preprocess_image(file_bytes: bytes):
    img = Image.open(io.BytesIO(file_bytes)).convert("L")
    img = ImageOps.exif_transpose(img)
    img = img.resize((IMG_W, IMG_H))
    arr = (np.asarray(img, dtype=np.float32) / 255.0)[None, ..., None]
    return arr

def predict(file_bytes: bytes) -> dict:
    x = preprocess_image(file_bytes)
    xi = x.astype(INP["dtype"])
    INTERP.set_tensor(INP["index"], xi)
    INTERP.invoke()
    probs = INTERP.get_tensor(OUT["index"])[0]
    top_idx = int(np.argmax(probs))
    top_class = CLASSES[top_idx]
    return {
        "top_class": top_class,
        "has_tumor": bool(top_class in TUMOR_CLASSES),
        "probabilities": {cls: float(p) for cls, p in zip(CLASSES, probs)},
    }

