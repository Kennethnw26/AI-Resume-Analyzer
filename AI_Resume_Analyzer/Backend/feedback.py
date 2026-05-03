def generate_feedback(matched: list[str], missing: list[str], score: float) -> str:
    lines = []

    if score >= 85:
        lines.append(
            f"Excellent match ({score}%). Your resume aligns very well with this role."
        )
    elif score >= 65:
        lines.append(
            f"Good match ({score}%). You meet most of the core requirements, with a few gaps to address."
        )
    elif score >= 40:
        lines.append(
            f"Partial match ({score}%). You have some relevant skills, but significant gaps remain."
        )
    else:
        lines.append(
            f"Weak match ({score}%). Your current skill set covers only a small portion of what this role requires."
        )

    if matched:
        top = matched[:5]
        lines.append(f"Strengths: {', '.join(top)}" + (" and more." if len(matched) > 5 else "."))

    if missing:
        priority = missing[:5]
        lines.append(
            f"Focus on: {', '.join(priority)}"
            + (" (and others)" if len(missing) > 5 else "")
            + " to improve your chances."
        )

    if not missing:
        lines.append("You match every required skill listed in the job description.")

    return " ".join(lines)
