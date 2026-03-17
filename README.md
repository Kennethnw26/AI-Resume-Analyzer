# AI-Resume-Analyzer
AI Resume Analyzer using Streamlit and FastAPI
An AI-powered web application that analyzes resumes against job descriptions, calculates a match score, and provides actionable feedback.

Features:
- Upload PDF or DOCX resumes
- Extract skills using NLP (spaCy)
- Compare resume with job descriptions
- Generate match score
- Provide AI-driven feedback
- Interactive UI with Streamlit

Backend = FastAPI
Frontend = Streamlit
NLP = spaCy
Language = Python

Installation
1. git clone https://github.com/your-username/ai-resume-analyzer.git
2. cd ai-resume-analyzer
3. Create virtual environment: "python -m venv venv"
4. Activating virtual environment: "venv\Scripts\activate"
5. Download requires dependencies/librarie: "pip install -r requirements.txt"
6. Download spaCy model: "python -m spacy download en_core_web_sm"

Running the application
1. Start backend in 1 terminal: "uvicorn Backend.main:app --reload"
2. Start frontend in another terminal: "streamlit run frontend/app.py"
