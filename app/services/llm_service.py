import os

from dotenv import load_dotenv
from google import genai

# Load environment variables
load_dotenv()

# Create Gemini client
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def generate_medical_report(prediction, confidence):
    prompt = f"""
You are an AI Medical Assistant.

A deep learning model analyzed a chest X-ray.

Prediction: {prediction}
Confidence: {confidence:.2f}%

Generate a professional medical report.

Do not repeat the prediction or confidence score because they are already displayed separately.

Include only these sections:

Clinical Interpretation:
Recommendation:
Disclaimer:

Keep the report under 200 words.

Do not use Markdown.
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text