import streamlit as st


def load_css():
    st.markdown(
        """
<style>

/* ========================================
            GLOBAL
======================================== */

.stApp{
    background-color:#F5F7FB;
}

.block-container{
    max-width:1250px;
    padding-top:6rem;
    padding-bottom:2rem;
}

/* ========================================
            EXISTING HEADER
======================================== */

.main-title{
    font-size:42px;
    font-weight:700;
    color:#1E3A8A;
    text-align:center;
    margin-top:8px;
    margin-bottom:5px;
    line-height:1.3;
}

.subtitle{
    text-align:center;
    color:#6B7280;
    font-size:18px;
    margin-bottom:35px;
}

/* ========================================
            LANDING PAGE
======================================== */

.hero{
    background:linear-gradient(135deg,#1E3A8A,#2563EB);
    color:white;
    padding:70px 50px;
    border-radius:22px;
    text-align:center;
    margin-bottom:40px;
    box-shadow:0 12px 30px rgba(37,99,235,.25);
}

.hero-title{
    font-size:52px;
    font-weight:700;
    margin-bottom:12px;
    color:white;
}

.hero-subtitle{
    font-size:24px;
    font-weight:500;
    margin-bottom:22px;
    color:#E5E7EB;
}

.hero-text{
    max-width:820px;
    margin:auto;
    font-size:18px;
    line-height:1.9;
    color:#F8FAFC;
}

/* ========================================
            CARDS
======================================== */

.card{
    background:white;
    padding:22px;
    border-radius:14px;
    box-shadow:0 4px 14px rgba(0,0,0,0.08);
    margin-bottom:20px;
}

.feature-card{
    background:white;
    border-radius:18px;
    padding:30px;
    box-shadow:0 8px 20px rgba(0,0,0,.08);
    transition:.3s;
    height:230px;
    margin-bottom:25px;
}

.workflow{
    background:white;
    padding:35px;
    border-radius:18px;
    text-align:center;
    box-shadow:0 8px 20px rgba(0,0,0,.08);
    font-size:18px;
    font-weight:600;
    color:#1E3A8A;
    margin-top:10px;
}

.feature-card:hover{
    transform:translateY(-6px);
    box-shadow:0 12px 28px rgba(37,99,235,.15);
}

.feature-title{
    font-size:22px;
    font-weight:700;
    color:#1E3A8A;
    margin-bottom:15px;
}

.feature-text{
    font-size:16px;
    color:#6B7280;
    line-height:1.8;
}

/* ========================================
            SECTION TITLE
======================================== */

.section-title{
    font-size:32px;
    font-weight:700;
    color:#1E3A8A;
    margin-top:45px;
    margin-bottom:25px;
}

/* ========================================
            INFO BOX
======================================== */

.info-box{
    background:white;
    padding:30px;
    border-radius:18px;
    box-shadow:0 8px 20px rgba(0,0,0,.08);
    line-height:1.9;
    font-size:17px;
    color:#4B5563;
    margin-bottom:35px;
}

/* ========================================
            REPORT
======================================== */

.report-box{
    background:#F9FAFB;
    border-left:5px solid #2563EB;
    border-radius:10px;
    padding:18px;
    line-height:1.8;
    font-size:16px;
}

/* ========================================
            FOOTER
======================================== */

.footer{
    text-align:center;
    color:#6B7280;
    font-size:15px;
    margin-top:70px;
    margin-bottom:25px;
}

.footer hr{
    border:none;
    height:1px;
    background:#D1D5DB;
    margin-bottom:20px;
}

.footer-platform{
    font-size:16px;
    font-weight:700;
    color:#1E3A8A;
    margin-bottom:4px;
}

.footer-tagline{
    font-size:14px;
    color:#6B7280;
    margin-bottom:22px;
}

.footer-developer{
    font-size:15px;
    font-weight:600;
    color:#374151;
    margin-bottom:2px;
}

.footer-role{
    font-size:13px;
    color:#6B7280;
    letter-spacing:.3px;
    margin-bottom:14px;
}

.footer-contact{
    font-size:14px;
    color:#4B5563;
    margin-bottom:18px;
}

.footer-contact a{
    color:#2563EB;
    text-decoration:none;
    font-weight:500;
    margin:0 4px;
}

.footer-contact a:hover{
    text-decoration:underline;
}

.footer-contact .divider{
    color:#D1D5DB;
    margin:0 6px;
}

.footer-copyright{
    font-size:12.5px;
    color:#9CA3AF;
}

/* ========================================
            BUTTONS
======================================== */

div.stButton > button{
    width:100%;
    height:55px;
    background:#2563EB;
    color:white;
    border:none;
    border-radius:12px;
    font-size:18px;
    font-weight:600;
    transition:.3s;
}

div.stButton > button:hover{
    background:#1D4ED8;
    transform:translateY(-2px);
    box-shadow:0 8px 18px rgba(37,99,235,.25);
    color:white;
}

</style>
        """,
        unsafe_allow_html=True,
    )