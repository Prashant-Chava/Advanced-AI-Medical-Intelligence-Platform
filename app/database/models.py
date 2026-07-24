from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Float
from sqlalchemy import DateTime
from sqlalchemy import Text

from datetime import datetime

from app.database.database import Base


class Prediction(Base):
    __tablename__ = "predictions"

    id = Column(Integer, primary_key=True, index=True)

    image_name = Column(String)

    prediction = Column(String)

    confidence = Column(Float)

    heatmap_path = Column(String)

    llm_report = Column(Text)

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )