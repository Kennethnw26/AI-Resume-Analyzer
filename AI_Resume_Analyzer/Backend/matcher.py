def match_skills(resume_skills: list[str], job_skills: list[str]) -> dict:
    resume_set = set(resume_skills)
    job_set = set(job_skills)

    matched = sorted(resume_set & job_set)
    missing = sorted(job_set - resume_set)
    extra = sorted(resume_set - job_set)  # skills on resume not required by job

    score = round((len(matched) / len(job_set)) * 100, 1) if job_set else 0.0

    return {
        "matched": matched,
        "missing": missing,
        "extra": extra,
        "score": score,
    }
