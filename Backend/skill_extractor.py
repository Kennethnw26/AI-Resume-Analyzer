import spacy

# Load the English NLP model
nlp = spacy.load("en_core_web_sm")

# Our "skill vocabulary"
SKILL_KEYWORDS = [
    "python", "java", "c++", "sql", "machine learning", "deep learning",
    "data analysis", "pandas", "numpy", "tensorflow", "pytorch",
    "excel", "power bi", "tableau", "statistics", "nlp", "api", "problem solving", "communication",
    "leadership"
]

def extract_skills(text):
    """
    Receives resume text and returns a list of detected skills
    """
    doc = nlp(text.lower())
    found_skills = set()

    for skill in SKILL_KEYWORDS:
        if skill in doc.text:
            found_skills.add(skill)

    return list(found_skills)
