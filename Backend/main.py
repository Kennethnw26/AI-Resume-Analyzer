from fastapi import FastAPI, UploadFile, File, Form
from Backend.resume_parser import extract_text_from_pdf, extract_text_from_docx
from Backend.skill_extractor import extract_skills
from Backend.matcher import match_skills
from Backend.feedback import generate_feedback

app = FastAPI()

@app.post("/analyze")
async def analyze_resume(
    file: UploadFile = File(...),
    job_description: str = Form(...)
):
    filename = file.filename

    if filename.endswith(".pdf"):
        resume_text = extract_text_from_pdf(file.file)
    elif filename.endswith(".docx"):
        resume_text = extract_text_from_docx(file.file)
    else:
        return {"error": "Unsupported file format"}

    resume_skills = extract_skills(resume_text)
    job_skills = extract_skills(job_description)

    result = match_skills(resume_skills, job_skills)

    feedback = generate_feedback(
        result["matched"],
        result["missing"],
        result["score"]
    )

    return {
        "resume_skills": resume_skills,
        "job_skills": job_skills,
        "matched": result["matched"],
        "missing": result["missing"],
        "score": result["score"],
        "feedback": feedback
    }
