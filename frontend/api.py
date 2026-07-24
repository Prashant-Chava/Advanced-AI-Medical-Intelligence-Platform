import requests

API_URL = "https://advanced-ai-medical-intelligence-platform-pdd0.onrender.com"

def predict(image_file, patient):
    """
    Send the uploaded X-ray and patient details to the FastAPI backend.
    """

    files = {
        "file": (
            image_file.name,
            image_file.getvalue(),
            image_file.type,
        )
    }

    data = {
        "patient_id": patient["patient_id"],
        "patient_name": patient["patient_name"],
        "age": str(patient["age"]),
        "gender": patient["gender"],
        "doctor": patient["doctor"],
        "notes": patient["notes"],
    }

    response = requests.post(
        f"{API_URL}/predict",
        files=files,
        data=data,
        timeout=120,
    )

    response.raise_for_status()

    return response.json()