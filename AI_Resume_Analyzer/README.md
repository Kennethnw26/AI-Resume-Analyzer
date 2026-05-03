# AI Resume Analyzer

An AI-powered web app that analyzes your resume against a job description, calculates a match score, and gives actionable feedback on skill gaps.

## Features

- Upload PDF or DOCX resumes
- Skill extraction using regex phrase matching with a vocabulary of ~120 skills
- Covers programming languages, frameworks, databases, cloud/DevOps, tools, and soft skills
- Match score with color-coded result (green / orange / red)
- Breakdown of matched skills, missing skills, and extra skills on your resume
- Actionable feedback with prioritized suggestions
- Input validation, file size limits, and clear error messages

## Tech Stack

| Layer    | Technology              |
|----------|-------------------------|
| Frontend | Streamlit               |
| Backend  | FastAPI + Uvicorn       |
| NLP      | spaCy (`en_core_web_sm`) |
| Parsing  | pdfplumber, python-docx |
| Language | Python 3.10+            |

## Project Structure

```
AI_Resume_Analyzer/
├── Backend/
│   ├── main.py            # FastAPI app and /analyze endpoint
│   ├── resume_parser.py   # PDF and DOCX text extraction
│   ├── skill_extractor.py # Skill vocabulary and phrase matching
│   ├── matcher.py         # Score calculation and skill diff
│   └── feedback.py        # Feedback generation
├── Frontend/
│   └── app.py             # Streamlit UI
└── requirements.txt
```

## Setup

**1. Clone the repo**
```bash
git clone https://github.com/Kennethnw26/AI-Resume-Analyzer.git
cd AI-Resume-Analyzer
```

**2. Create and activate a virtual environment**
```bash
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # macOS / Linux
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

The spaCy model is included in `requirements.txt` and installs automatically. If you need to install it manually:
```bash
python -m spacy download en_core_web_sm
```

## Running the App

Open two terminals, both with the virtual environment activated.

**Terminal 1 — Backend**
```bash
cd Backend
uvicorn main:app --reload
```
The API will be available at `http://127.0.0.1:8000`.

**Terminal 2 — Frontend**
```bash
cd Frontend
streamlit run app.py
```
The UI will open automatically at `http://localhost:8501`.
