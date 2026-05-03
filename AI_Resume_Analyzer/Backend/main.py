import io

from fastapi import FastAPI, HTTPException, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware

from resume_parser import extract_text_from_pdf, extract_text_from_docx
from skill_extractor import extract_skills
from matcher import match_skills
from feedback import generate_feedback

app = FastAPI(title="AI Resume Analyzer API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["POST"],
    allow_headers=["*"],
)

ALLOWED_EXTENSIONS = {".pdf", ".docx"}
MAX_FILE_SIZE_MB = 10


@app.post("/analyze")
async def analyze_resume(
    file: UploadFile = File(...),
    job_description: str = Form(...),
):
    # Validate file type
    filename = file.filename or ""
    ext = "." + filename.rsplit(".", 1)[-1].lower() if "." in filename else ""
    if ext not in ALLOWED_EXTENSIONS:
        raise HTTPException(status_code=400, detail="Only PDF and DOCX files are supported.")

    # Read file bytes with size check
    content = await file.read()
    if len(content) > MAX_FILE_SIZE_MB * 1024 * 1024:
        raise HTTPException(status_code=413, detail=f"File exceeds {MAX_FILE_SIZE_MB} MB limit.")

    if not job_description.strip():
        raise HTTPException(status_code=400, detail="Job description cannot be empty.")

    # Extract text
    file_like = io.BytesIO(content)
    try:
        if ext == ".pdf":
            resume_text = extract_text_from_pdf(file_like)
        else:
            resume_text = extract_text_from_docx(file_like)
    except ValueError as e:
        raise HTTPException(status_code=422, detail=str(e))

    # Analyze
    resume_skills = extract_skills(resume_text)
    job_skills = extract_skills(job_description)

    if not job_skills:
        raise HTTPException(
            status_code=422,
            detail="No recognizable skills found in the job description. Try including specific technologies or skill names.",
        )

    result = match_skills(resume_skills, job_skills)
    feedback = generate_feedback(result["matched"], result["missing"], result["score"])

    return {
        "score": result["score"],
        "matched": result["matched"],
        "missing": result["missing"],
        "extra": result["extra"],
        "resume_skills": resume_skills,
        "job_skills": job_skills,
        "feedback": feedback,
    }
