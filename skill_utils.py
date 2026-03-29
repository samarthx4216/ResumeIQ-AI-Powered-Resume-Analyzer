SKILLS_DB = [
    "python", "machine learning", "deep learning", "nlp", "tensorflow", "pytorch",
    "scikit-learn", "pandas", "numpy", "sql", "mongodb", "docker", "git",
    "flask", "fastapi", "streamlit", "transformers", "bert", "opencv",
    "data analysis", "computer vision", "aws", "azure", "gcp", "keras",
    "xgboost", "matplotlib", "seaborn", "power bi", "tableau", "java",
    "javascript", "react", "node", "html", "css", "linux", "spark",
    "hadoop", "excel", "communication", "leadership", "problem solving"
]

def extract_skills_from_text(text):
    text = text.lower()
    found = [skill for skill in SKILLS_DB if skill in text]
    return list(set(found))

def get_skill_gap(resume_text, jd_text):
    resume_skills = extract_skills_from_text(resume_text)
    jd_skills     = extract_skills_from_text(jd_text)
    missing       = [s for s in jd_skills if s not in resume_skills]
    common        = [s for s in jd_skills if s in resume_skills]
    return {
        "resume_skills": resume_skills,
        "jd_skills":     jd_skills,
        "common_skills": common,
        "missing_skills": missing
    }