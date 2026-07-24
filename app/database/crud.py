from app.database.database import SessionLocal
from app.database.models import Prediction


def save_prediction(
    image_name,
    prediction,
    confidence,
    heatmap_path,
    llm_report
):
    db = SessionLocal()

    record = Prediction(
        image_name=image_name,
        prediction=prediction,
        confidence=confidence,
        heatmap_path=heatmap_path,
        llm_report=llm_report
    )

    db.add(record)
    db.commit()
    db.refresh(record)

    db.close()

    return record