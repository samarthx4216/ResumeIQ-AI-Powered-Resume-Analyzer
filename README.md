# ResumeIQ — AI-Powered Resume Analyzer

> Match your resume to any job description in seconds using BERT, NLP, and Streamlit.

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.32+-red)
![NLP](https://img.shields.io/badge/NLP-spaCy%20%7C%20BERT-purple)
![License](https://img.shields.io/badge/License-MIT-green)

---

## What is ResumeIQ?

ResumeIQ is an end-to-end AI application that helps job seekers understand
how well their resume matches a job description — and exactly what to fix.

Most job applications are rejected by ATS (Applicant Tracking Systems) before
a human even reads them. ResumeIQ gives you the same analysis an ATS would do,
plus actionable suggestions to improve your chances.

---

## Features

- **Semantic Match Score** — Uses Sentence-BERT to compute deep semantic
  similarity between your resume and the job description (not just keyword matching)
- **Skill Gap Analysis** — Identifies exactly which skills the job requires
  that are missing from your resume
- **ATS Score** — Predicts your likelihood of passing automated screening
- **Interview Prep** — Auto-generates likely interview questions based on
  your skill matches and gaps
- **PDF Resume Parsing** — Extracts text, entities, skills directly from
  your uploaded PDF using PyMuPDF and spaCy NER

---

## Tech Stack

| Layer | Technology |
|-------|------------|
| Frontend | Streamlit |
| NLP | spaCy, Sentence-Transformers (all-MiniLM-L6-v2) |
| ML | Cosine Similarity, BERT Embeddings |
| PDF Parsing | PyMuPDF (fitz) |
| Entity Recognition | spaCy NER (en_core_web_sm) |
| Language | Python 3.10+ |

---

## Project Structure

```
resumeiq/
├── app.py                  # Main Streamlit UI
├── parser.py               # PDF text + entity extraction
├── matcher.py              # Semantic similarity scoring
├── skill_utils.py          # Skill gap detection
├── interview_questions.py  # Interview question generator
├── requirements.txt        # Dependencies
└── README.md
```

---

## How to Run Locally

**1. Clone the repository**
```bash
git clone https://github.com/YOURUSERNAME/resumeiq.git
cd resumeiq
```

**2. Create virtual environment**
```bash
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

**4. Run the app**
```bash
python -m streamlit run app.py
```

---

## How It Works

```
Your Resume (PDF)  +  Job Description (text)
        |                      |
        v                      v
  PDF Text Extraction     Keyword Extraction
  spaCy NER               spaCy NLP
        |                      |
        +----------+-----------+
                   |
        Sentence-BERT Encoding
        (all-MiniLM-L6-v2)
                   |
        Cosine Similarity Score
                   |
          +--------+--------+
          v                 v
    Skill Gap          Interview
    Analysis           Questions
```

---

## Future Improvements

- [ ] Fine-tune BERT on resume dataset for higher accuracy
- [ ] Add job scraper to auto-fetch job descriptions
- [ ] Resume rewrite suggestions using LLM
- [ ] Multi-language resume support
- [ ] User history and progress tracking

---

## Author

Built by **Samar** — Building AI projects to solve real problems.

Connect on [LinkedIn](https://linkedin.com/in/YOURPROFILE) |
View on [GitHub](https://github.com/YOURUSERNAME)

---

## License

MIT License — free to use, modify, and share.
