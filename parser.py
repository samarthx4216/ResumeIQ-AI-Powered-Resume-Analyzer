import fitz  # PyMuPDF
import spacy

nlp = spacy.load("en_core_web_sm")

SKILLS_DB = [
    "python", "machine learning", "deep learning", "nlp", "tensorflow", "pytorch",
    "scikit-learn", "pandas", "numpy", "sql", "mongodb", "docker", "git",
    "flask", "fastapi", "streamlit", "transformers", "bert", "opencv",
    "data analysis", "computer vision", "aws", "azure", "gcp", "keras",
    "xgboost", "matplotlib", "seaborn", "power bi", "tableau"
]

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text.lower()

def extract_entities(text):
    doc = nlp(text)
    names    = [ent.text for ent in doc.ents if ent.label_ == "PERSON"]
    orgs     = [ent.text for ent in doc.ents if ent.label_ == "ORG"]
    dates    = [ent.text for ent in doc.ents if ent.label_ == "DATE"]
    return {"names": names, "organizations": orgs, "dates": dates}

def extract_skills(text):
    found = [skill for skill in SKILLS_DB if skill in text]
    return list(set(found))

def parse_resume(pdf_path):
    text     = extract_text_from_pdf(pdf_path)
    entities = extract_entities(text)
    skills   = extract_skills(text)
    return {
        "raw_text": text,
        "entities": entities,
        "skills":   skills
    }