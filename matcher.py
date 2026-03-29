from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2')

def get_match_score(resume_text, job_description):
    embeddings = model.encode([resume_text, job_description])
    score = cosine_similarity([embeddings[0]], [embeddings[1]])[0][0]
    return round(float(score) * 100, 2)

def get_semantic_keywords(text):
    words = list(set(text.lower().split()))
    words = [w.strip(".,!?()[]") for w in words if len(w) > 4]
    return words