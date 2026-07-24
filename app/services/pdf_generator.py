import os
from datetime import datetime

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Image
)


def generate_pdf_report(
    image_name,
    prediction,
    confidence,
    heatmap_path,
    llm_report
):
    os.makedirs("reports", exist_ok=True)

    pdf_path = os.path.join(
        "reports",
        f"{os.path.splitext(image_name)[0]}_report.pdf"
    )

    doc = SimpleDocTemplate(pdf_path)

    styles = getSampleStyleSheet()

    elements = []

    elements.append(
        Paragraph("<b>AI Medical Analysis Report</b>", styles["Title"])
    )

    elements.append(Spacer(1, 20))

    elements.append(
        Paragraph(f"<b>Image:</b> {image_name}", styles["BodyText"])
    )

    elements.append(
        Paragraph(
            f"<b>Date:</b> {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}",
            styles["BodyText"],
        )
    )

    elements.append(
        Paragraph(f"<b>Prediction:</b> {prediction}", styles["BodyText"])
    )

    elements.append(
        Paragraph(
            f"<b>Confidence:</b> {confidence:.2f}%",
            styles["BodyText"],
        )
    )

    elements.append(Spacer(1, 20))

    elements.append(
        Paragraph("<b>AI Medical Report</b>", styles["Heading2"])
    )

    llm_report = llm_report.replace("\n", "<br/>")

    elements.append(
        Paragraph(llm_report, styles["BodyText"])
    )

    elements.append(Spacer(1, 20))

    if os.path.exists(heatmap_path):
        elements.append(
            Paragraph("<b>Grad-CAM Heatmap</b>", styles["Heading2"])
        )

        elements.append(
            Image(
                heatmap_path,
                width=300,
                height=300
            )
        )

    elements.append(Spacer(1, 20))

    elements.append(
        Paragraph(
            "<b>Disclaimer:</b> This report is AI-generated and should not replace professional medical diagnosis.",
            styles["BodyText"],
        )
    )

    doc.build(elements)

    return pdf_path