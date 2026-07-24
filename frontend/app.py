import streamlit as st

from api import predict
from config import (
    DEVELOPER_NAME,
    DEVELOPER_ROLE,
    DEVELOPER_EMAIL,
    DEVELOPER_LINKEDIN,
    DEVELOPER_GITHUB,
    COPYRIGHT_YEAR,
)
from style import load_css
from utils import (
    show_prediction,
    show_images,
    show_report,
    download_report,
)

# ======================================================
# Page Configuration
# ======================================================

st.set_page_config(
    page_title="AI Medical Image Analysis",
    page_icon="🩺",
    layout="wide",
)

load_css()

# ======================================================
# Footer (shared across pages)
# ======================================================

FOOTER_HTML = f"""
<div class="footer">
<hr>
<div class="footer-platform">AI Medical Image Analysis Platform</div>
<div class="footer-tagline">AI-assisted chest X-ray analysis for educational and research purposes.</div>
<div class="footer-developer">Developed by {DEVELOPER_NAME}</div>
<div class="footer-role">{DEVELOPER_ROLE.replace(" | ", " &nbsp;|&nbsp; ")}</div>
<div class="footer-contact">
📧 <a href="mailto:{DEVELOPER_EMAIL}">{DEVELOPER_EMAIL}</a>
<span class="divider">•</span>
🔗 <a href="{DEVELOPER_LINKEDIN}" target="_blank">LinkedIn</a>
<span class="divider">|</span>
<a href="{DEVELOPER_GITHUB}" target="_blank">GitHub</a>
</div>
<div class="footer-copyright">© {COPYRIGHT_YEAR} {DEVELOPER_NAME}. For educational and research purposes only.</div>
</div>
"""

# ======================================================
# Session State
# ======================================================

if "page" not in st.session_state:
    st.session_state.page = "home"

if "result" not in st.session_state:
    st.session_state.result = None

if "uploaded_image" not in st.session_state:
    st.session_state.uploaded_image = None


# ======================================================
# Home Page
# ======================================================

def show_home():

    # --------------------------------------------------
    # Hero Section
    # --------------------------------------------------

    st.markdown(
        """
<div class="hero">
<div class="hero-title">
🩺 AI Medical Image Analysis Platform
</div>
<div class="hero-subtitle">
AI-Powered Chest X-ray Analysis
</div>
<div class="hero-text">
Assist healthcare professionals by analyzing chest X-ray
images using artificial intelligence. Generate AI-assisted
predictions, visualize important image regions, and
receive structured clinical reports to support
medical decision-making.
</div>
</div>
        """,
        unsafe_allow_html=True,
    )

    st.write("")

    if st.button(
        "🚀 Start Analysis",
        width="stretch",
    ):
        st.session_state.page = "analysis"
        st.rerun()

    # --------------------------------------------------
    # About
    # --------------------------------------------------

    st.markdown(
        '<div class="section-title">About the Platform</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        """
<div class="info-box">
The AI Medical Image Analysis Platform provides an easy and
intuitive way to analyze chest X-ray images using artificial
intelligence.
<br><br>
The platform generates an AI-assisted prediction, highlights
important regions of the image through visual explanations,
and produces a structured clinical report that can be reviewed
alongside the uploaded scan.
</div>
        """,
        unsafe_allow_html=True,
    )

    # --------------------------------------------------
    # Features
    # --------------------------------------------------

    st.markdown(
        '<div class="section-title">Key Features</div>',
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns(2)

    with col1:

        st.markdown(
            """
<div class="feature-card">
<div class="feature-title">
🔍 Intelligent Image Analysis
</div>
<div class="feature-text">
Upload a chest X-ray image and receive an
AI-assisted prediction within seconds.
</div>
</div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown(
            """
<div class="feature-card">
<div class="feature-title">
🩻 Visual Explanation
</div>
<div class="feature-text">
View an attention heatmap that highlights
the regions influencing the AI prediction.
</div>
</div>
            """,
            unsafe_allow_html=True,
        )

    with col2:

        st.markdown(
            """
<div class="feature-card">
<div class="feature-title">
📄 Clinical Report
</div>
<div class="feature-text">
Review a structured report containing
AI-generated clinical observations
and recommendations.
</div>
</div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown(
            """
<div class="feature-card">
<div class="feature-title">
📥 Download Report
</div>
<div class="feature-text">
Download the complete analysis report
for documentation and future reference.
</div>
</div>
            """,
            unsafe_allow_html=True,
        )

    # --------------------------------------------------
    # Workflow
    # --------------------------------------------------

    st.markdown(
        '<div class="section-title">How It Works</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        """
<div class="workflow">
📤 Upload Chest X-ray
⟶
🤖 AI Analysis
⟶
📊 Prediction
⟶
📄 Clinical Report
⟶
📥 Download Report
</div>
        """,
        unsafe_allow_html=True,
    )

    # --------------------------------------------------
    # Footer
    # --------------------------------------------------

    st.markdown(
        FOOTER_HTML,
        unsafe_allow_html=True,
    )
# ======================================================
# Analysis Page
# ======================================================

def show_analysis():

    # --------------------------------------------------
    # Navigation
    # --------------------------------------------------

    col1, col2 = st.columns([1, 5])

    with col1:
        if st.button("← Home"):
            st.session_state.page = "home"
            st.rerun()

    with col2:
        st.markdown(
            """
<div class="main-title">
🩺 AI Medical Image Analysis
</div>
<div class="subtitle">
Upload a chest X-ray image and generate an AI-assisted
medical analysis report.
</div>
            """,
            unsafe_allow_html=True,
        )

    st.divider()

    # --------------------------------------------------
    # Upload & Patient Information
    # --------------------------------------------------

    left, right = st.columns([1, 1], gap="large")

    with left:

        st.markdown(
            '<div class="section-title">📤 Upload Chest X-ray</div>',
            unsafe_allow_html=True,
        )

        uploaded_file = st.file_uploader(
            "Upload Chest X-ray",
            type=["jpg", "jpeg", "png"],
            label_visibility="collapsed",
        )

        if uploaded_file is not None:

            st.image(
                uploaded_file,
                caption="Uploaded Chest X-ray",
                use_container_width=True,
            )

    with right:

        st.markdown(
            '<div class="section-title">👤 Patient Information</div>',
            unsafe_allow_html=True,
        )

        patient_id = st.text_input(
            "Patient ID"
        )

        patient_name = st.text_input(
            "Patient Name"
        )

        age = st.number_input(
            "Age",
            min_value=1,
            max_value=120,
            value=30,
        )

        gender = st.selectbox(
            "Gender",
            [
                "Male",
                "Female",
                "Other",
            ],
        )

        doctor = st.text_input(
            "Referring Doctor"
        )

        notes = st.text_area(
            "Clinical Notes",
            height=120,
        )

    st.write("")
    st.write("")

    # --------------------------------------------------
    # Analyze Button
    # --------------------------------------------------

    analyze = st.button(
        "🔍 Analyze Scan",
        width="stretch",
    )

    # --------------------------------------------------
    # Validation & Prediction
    # --------------------------------------------------

    if analyze:

        if uploaded_file is None:
            st.error("Please upload a chest X-ray image.")
            st.stop()

        if patient_id.strip() == "":
            st.error("Please enter the Patient ID.")
            st.stop()

        if patient_name.strip() == "":
            st.error("Please enter the Patient Name.")
            st.stop()

        patient = {

            "patient_id": patient_id,
            "patient_name": patient_name,
            "age": age,
            "gender": gender,
            "doctor": doctor,
            "notes": notes,

        }

        progress = st.progress(0)

        status = st.empty()

        try:

            status.info("Uploading image...")
            progress.progress(20)

            status.info("Running AI analysis...")
            progress.progress(50)

            result = predict(
                uploaded_file,
                patient,
            )

            progress.progress(90)

            st.session_state.result = result
            st.session_state.uploaded_image = uploaded_file

            progress.progress(100)

            status.success("Analysis completed successfully.")

        except Exception as e:

            progress.empty()
            status.empty()

            st.error(str(e))

            st.stop()

        progress.empty()

    # --------------------------------------------------
    # Results
    # --------------------------------------------------

    if st.session_state.result is None:
        return

    result = st.session_state.result

    st.divider()

    st.markdown(
        '<div class="section-title">📊 Analysis Result</div>',
        unsafe_allow_html=True,
    )

    show_prediction(result)

    st.write("")

    st.markdown(
        '<div class="section-title">🩻 Image Visualization</div>',
        unsafe_allow_html=True,
    )

    show_images(
        st.session_state.uploaded_image,
        result["heatmap_url"],
    )

    st.write("")

    st.markdown(
        '<div class="section-title">📄 Clinical Report</div>',
        unsafe_allow_html=True,
    )

    show_report(result)

    st.write("")

    st.markdown(
        '<div class="section-title">📥 Download Report</div>',
        unsafe_allow_html=True,
    )

    download_report(result)

    st.markdown(
        FOOTER_HTML,
        unsafe_allow_html=True,
    )
if st.session_state.page == "home":
    show_home()
else:
    show_analysis()