import streamlit as st
import time
from resume_parser import extract_text_from_pdf
from text_cleaner import clean_textr
from skill_extractor import extract_skillss
from matcher import match_resume_with_jobss



# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AI Resume Screener",
    page_icon="📄",
    layout="wide"
)

# ---------------- CSS (DECENT BACKGROUND + READABLE UI) ----------------
st.markdown("""
<style>

/* Background with soft dark overlay */
.stApp {
    background-image: linear-gradient(
        rgba(0, 0, 0, 0.55),
        rgba(0, 0, 0, 0.55)
    ),
    url("https://images.unsplash.com/photo-1521737604893-d14cc237f11d");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}

/* Main container */
.overlay {
    padding: 30px;
}

/* Titles */
.main-title {
    font-size: 42px;
    font-weight: 700;
    color: #ffffff;
    text-align: center;
}

.sub-title {
    text-align: center;
    font-size: 18px;
    color: #e0e0e0;
    margin-bottom: 35px;
}

/* Cards */
.card {
    background: rgba(255, 255, 255, 0.96);
    padding: 24px;
    border-radius: 18px;
    box-shadow: 0px 8px 25px rgba(0,0,0,0.25);
    margin-bottom: 25px;
}

/* Skill tags */
.skill-pill {
    display: inline-block;
    background-color: #eef4ff;
    color: #1a73e8;
    padding: 7px 16px;
    border-radius: 25px;
    margin: 6px;
    font-size: 14px;
    font-weight: 500;
}

/* Footer */
.footer {
    text-align: center;
    color: #dddddd;
    margin-top: 40px;
    font-size: 14px;
}

</style>
""", unsafe_allow_html=True)

# ---------------- UI START ----------------
st.markdown('<div class="overlay">', unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown('<div class="main-title">AI Resume Screening & Job Recommendation</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Upload your resume and get AI-powered job recommendations</div>', unsafe_allow_html=True)

# ---------------- UPLOAD SECTION ----------------
st.markdown('<div class="card">', unsafe_allow_html=True)
uploaded_file = st.file_uploader("📤 Upload Resume (PDF only)", type="pdf")
st.markdown('</div>', unsafe_allow_html=True)

# ---------------- PROCESS ----------------
if uploaded_file is not None:
    st.success("✅ Resume uploaded successfully")

    raw_text = extract_text_from_pdf(uploaded_file)

    if not raw_text.strip():
        st.error("❌ No text found. Please upload a text-based PDF resume.")
    else:
        cleaned_text = clean_textr(raw_text)

        # -------- SKILLS --------
        skills = extract_skillss(cleaned_text)
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("🧠 Extracted Skills")

        if skills:
            for skill in skills:
                st.markdown(f'<span class="skill-pill">{skill}</span>', unsafe_allow_html=True)
        else:
            st.write("No skills detected")

        st.markdown('</div>', unsafe_allow_html=True)

        # -------- JOB MATCHING --------
        results = match_resume_with_jobss(cleaned_text)
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("💼 Recommended Jobs")
        st.dataframe(results, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

else:
    st.info("⬆️ Upload your resume to start the analysis")

# ---------------- FOOTER ----------------
st.markdown('<div class="footer">Built with ❤️ using AI, Machine Learning & NLP</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
