import os

from app.services.model_loader import model
from app.utils.image_preprocessor import preprocess_image
from app.services.gradcam import generate_gradcam
from app.services.llm_service import generate_medical_report
from app.database.crud import save_prediction
from app.services.pdf_generator import generate_pdf_report


def predict(image_path):
    # Preprocess image
    print("Step 1: Preprocessing")
    image = preprocess_image(image_path)

    # Model prediction
    print("Step 2: Model prediction")
    prediction = model.predict(image, verbose=0)[0][0]

    # Determine prediction result
    if prediction >= 0.5:
        result = "Pneumonia"
        confidence = prediction
    else:
        result = "Normal"
        confidence = 1 - prediction

    # Convert confidence to percentage
    confidence_percentage = round(float(confidence * 100), 2)

    # Generate Grad-CAM heatmap
    print("Step 3: GradCAM")
    heatmap_path = generate_gradcam(image_path)

    # Generate AI Medical Report
    print("Step 4: Gemini")
    llm_report = generate_medical_report(
        prediction=result,
        confidence=confidence_percentage
    )

    # Get image name
    image_name = os.path.basename(image_path)

    # Save everything to database
    print("Step 5: Database")
    save_prediction(
        image_name=image_name,
        prediction=result,
        confidence=confidence_percentage,
        heatmap_path=heatmap_path,
        llm_report=llm_report
    )

    # Generate PDF report
    print("Step 6: PDF")
    pdf_path = generate_pdf_report(
    image_name=image_name,
    prediction=result,
    confidence=confidence_percentage,
    heatmap_path=heatmap_path,
    llm_report=llm_report
)
    print("Step 7: Done")
    # Return API response
    return {
        "prediction": result,
        "confidence": confidence_percentage,
        "heatmap_path": heatmap_path,
        "pdf_path": pdf_path,
        "llm_report": llm_report
    }