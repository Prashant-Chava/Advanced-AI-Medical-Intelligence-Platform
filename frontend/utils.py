import streamlit as st


def show_prediction(result):
    """Display prediction and confidence."""

    prediction = result.get("prediction", "Unknown")
    confidence = result.get("confidence", 0)

    st.subheader("🩺 Prediction")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            label="Diagnosis",
            value=prediction,
        )

    with col2:
        st.metric(
            label="Confidence",
            value=f"{confidence:.2f}%",
        )


def show_images(original_image, heatmap_url):
    """Display uploaded image and Grad-CAM heatmap."""

    st.subheader("🖼️ Image Comparison")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("**Original X-ray**")
        st.image(
            original_image,
            width="stretch",
        )

    with col2:
        st.markdown("**AI Heatmap**")
        st.image(
            heatmap_url,
            width="stretch",
        )


def show_report(result):
    """Display AI-generated report."""

    report = result.get("llm_report", "")

    st.subheader("📄 AI Clinical Report")

    st.markdown(
        f"""
<div style="
padding:18px;
border-radius:12px;
background:#f8fafc;
border:1px solid #e2e8f0;
line-height:1.8;
font-size:16px;
">
{report}
</div>
""",
        unsafe_allow_html=True,
    )


def download_report(result):
    """Display PDF download button."""

    pdf_url = result.get("pdf_url")

    if pdf_url:
        st.link_button(
            "⬇ Download Medical Report",
            pdf_url,
            use_container_width=True,
        )