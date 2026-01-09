SKILLS_DB = [
    "python", "sql", "machine learning", "deep learning",
    "nlp", "data analysis", "power bi", "excel",
    "tensorflow", "pandas", "numpy"
]

def extract_skillss(text):
    found_skills = []
    for skill in SKILLS_DB:
        if skill in text:
            found_skills.append(skill)
    return found_skills
