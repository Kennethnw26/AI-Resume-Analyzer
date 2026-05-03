import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/analyze"

st.set_page_config(page_title="AI Resume Analyzer", layout="centered")

st.title("AI Resume Analyzer")
st.caption("Upload your resume and a job description to see how well you match.")

st.divider()

resume_file = st.file_uploader("Resume (PDF or DOCX)", type=["pdf", "docx"])
job_description = st.text_area("Job Description", height=220, placeholder="Paste the full job posting here...")

analyze_clicked = st.button("Analyze", type="primary", use_container_width=True)

if analyze_clicked:
    if resume_file is None:
        st.error("Please upload a resume file.")
    elif not job_description.strip():
        st.error("Please paste a job description.")
    else:
        with st.spinner("Analyzing..."):
            try:
                response = requests.post(
                    API_URL,
                    files={"file": (resume_file.name, resume_file.getvalue(), resume_file.type)},
                    data={"job_description": job_description},
                    timeout=30,
                )
            except requests.exceptions.ConnectionError:
                st.error("Cannot connect to the backend. Make sure the FastAPI server is running (`uvicorn main:app` inside the Backend folder).")
                st.stop()
            except requests.exceptions.Timeout:
                st.error("The request timed out. The server may be overloaded.")
                st.stop()

        if response.status_code == 200:
            result = response.json()

            score = result["score"]
            matched = result["matched"]
            missing = result["missing"]
            extra = result.get("extra", [])
            feedback = result["feedback"]
            job_skills = result.get("job_skills", [])

            st.divider()

            # Score
            st.subheader("Match Score")
            color = "green" if score >= 65 else "orange" if score >= 40 else "red"
            st.markdown(
                f"<h1 style='color:{color}; margin:0'>{score}%</h1>",
                unsafe_allow_html=True,
            )
            st.progress(int(score) / 100)

            st.divider()

            # Skill breakdown
            col1, col2 = st.columns(2)

            with col1:
                st.subheader(f"Matched ({len(matched)})")
                if matched:
                    for skill in matched:
                        st.success(skill, icon="✓")
                else:
                    st.caption("No matching skills found.")

            with col2:
                st.subheader(f"Missing ({len(missing)})")
                if missing:
                    for skill in missing:
                        st.error(skill, icon="✗")
                else:
                    st.caption("All required skills present.")

            # Extra skills (resume skills not in job description)
            if extra:
                with st.expander(f"Other skills on your resume ({len(extra)})"):
                    st.caption("These are on your resume but not specifically required by this job.")
                    cols = st.columns(3)
                    for i, skill in enumerate(extra):
                        cols[i % 3].markdown(f"- {skill}")

            st.divider()

            # Feedback
            st.subheader("Feedback")
            st.info(feedback)

            # Stats summary
            with st.expander("Details"):
                st.markdown(f"**Skills detected in job description:** {len(job_skills)}")
                st.markdown(f"**Skills detected on resume:** {len(result.get('resume_skills', []))}")
                st.markdown(f"**Matched:** {len(matched)} / {len(job_skills)}")
                if job_skills:
                    st.markdown("**All required skills:** " + ", ".join(job_skills))

        else:
            try:
                detail = response.json().get("detail", "Unknown error")
            except Exception:
                detail = response.text or "Unknown error"
            st.error(f"Error {response.status_code}: {detail}")
