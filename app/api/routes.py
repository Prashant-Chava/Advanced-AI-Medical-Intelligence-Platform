from fastapi import APIRouter, UploadFile, File, Form, Request
import os
import shutil

from app.services.predictor import predict

router = APIRouter()


@router.post("/predict")
async def predict_pneumonia(
    request: Request,
    file: UploadFile = File(...),

    patient_id: str = Form(...),
    patient_name: str = Form(...),
    age: int = Form(...),
    gender: str = Form(...),
    doctor: str = Form(...),
    notes: str = Form(...),
):
    upload_folder = "uploads"
    os.makedirs(upload_folder, exist_ok=True)

    file_path = os.path.join(upload_folder, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    print("Saved to:", file_path)
    print("File size:", os.path.getsize(file_path))

    result = predict(file_path)

    result["patient"] = {
        "patient_id": patient_id,
        "patient_name": patient_name,
        "age": age,
        "gender": gender,
        "doctor": doctor,
        "notes": notes,
    }

    result["heatmap_url"] = (
        str(request.base_url)
        + result["heatmap_path"].replace("\\", "/")
    )

    result["pdf_url"] = (
        str(request.base_url)
        + result["pdf_path"].replace("\\", "/")
    )

    return result