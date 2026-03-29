QUESTION_TEMPLATES = {
    "python":           "Can you explain how you've used Python in a real project?",
    "machine learning": "Walk me through a machine learning model you've built end to end.",
    "deep learning":    "What deep learning architectures have you worked with?",
    "nlp":              "Describe an NLP problem you solved and your approach.",
    "sql":              "How do you optimize a slow SQL query?",
    "docker":           "How have you used Docker in your workflow?",
    "aws":              "What AWS services have you used and for what purpose?",
    "git":              "How do you handle merge conflicts in Git?",
    "tensorflow":       "Compare TensorFlow and PyTorch from your experience.",
    "pytorch":          "How did you use PyTorch for training a model?",
    "pandas":           "How do you handle missing data in a pandas DataFrame?",
    "data analysis":    "Describe a data analysis project you're proud of.",
    "computer vision":  "What computer vision tasks have you worked on?",
    "leadership":       "Tell me about a time you led a technical team.",
}

def generate_questions(missing_skills, common_skills):
    questions = []
    for skill in common_skills:
        if skill in QUESTION_TEMPLATES:
            questions.append({
                "skill": skill,
                "type": "strength",
                "question": QUESTION_TEMPLATES[skill]
            })
    for skill in missing_skills:
        questions.append({
            "skill": skill,
            "type": "gap",
            "question": f"You listed {skill} as required — do you have any exposure to it?"
        })
    return questions[:10]