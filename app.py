import streamlit as st
import tempfile
import os
from parser import parse_resume
from matcher import get_match_score
from skill_utils import get_skill_gap
from interview_questions import generate_questions
import fitz

st.set_page_config(
    page_title="Resume AI Analyzer",
    page_icon="📄",
    layout="wide"
)

st.title("📄 Resume AI Analyzer")
st.markdown("Upload your resume and paste a job description to get your match score, skill gaps, and interview prep.")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Your Resume")
    uploaded_file = st.file_uploader("Upload PDF resume", type="pdf")

with col2:
    st.subheader("Job Description")
    jd_text = st.text_area("Paste the job description here", height=200)

if uploaded_file and jd_text:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(uploaded_file.read())
        tmp_path = tmp.name

    with st.spinner("Analyzing your resume..."):
        resume_data = parse_resume(tmp_path)
        resume_text = resume_data["raw_text"]

        score = get_match_score(resume_text, jd_text)
        gap   = get_skill_gap(resume_text, jd_text)
        questions = generate_questions(gap["missing_skills"], gap["common_skills"])

    os.unlink(tmp_path)

    st.divider()

    # Match Score
    st.subheader("Match Score")
    col_a, col_b, col_c = st.columns(3)
    with col_a:
        st.metric("Overall Match", f"{score}%")
    with col_b:
        st.metric("Skills Matched", len(gap["common_skills"]))
    with col_c:
        st.metric("Skills Missing", len(gap["missing_skills"]))

    if score >= 70:
        st.success("Strong match! You're a great fit for this role.")
    elif score >= 45:
        st.warning("Moderate match. Consider adding missing skills to your resume.")
    else:
        st.error("Low match. Significant skill gaps detected.")

    st.divider()

    # Skills breakdown
    col3, col4 = st.columns(2)

    with col3:
        st.subheader("Skills You Have")
        if gap["common_skills"]:
            for skill in gap["common_skills"]:
                st.success(f"✓  {skill}")
        else:
            st.info("No matching skills found.")

    with col4:
        st.subheader("Skills to Add")
        if gap["missing_skills"]:
            for skill in gap["missing_skills"]:
                st.error(f"✗  {skill}")
        else:
            st.success("No skill gaps found!")

    st.divider()

    # Interview Questions
    st.subheader("Interview Prep Questions")
    for i, q in enumerate(questions, 1):
        label = "Strength" if q["type"] == "strength" else "Gap area"
        with st.expander(f"Q{i}: {q['skill'].title()} — {label}"):
            st.write(q["question"])

    st.divider()

    # Raw entities
    with st.expander("View extracted resume details"):
        st.json(resume_data["entities"])
        st.write("**Skills found in resume:**", resume_data["skills"])

else:
    st.info("Upload your resume PDF and paste a job description above to get started.")
