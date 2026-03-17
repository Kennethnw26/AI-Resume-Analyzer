def generate_feedback(matched, missing, score):
    feedback = []

    if score >= 80:
        feedback.append("Your resume is a strong match for this job.")
    elif score >= 50:
        feedback.append("Your resume matches some of the job requirements, but there are gaps.")
    else:
        feedback.append("Your resume currently does not match many of the job requirements.")

    if missing:
        feedback.append(
            "You should consider improving or adding experience in: " + ", ".join(missing) + "."
        )

    if matched:
        feedback.append(
            "You already demonstrate strength in: " + ", ".join(matched) + "."
        )

    return " ".join(feedback)
