import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/analyze"

st.set_page_config(page_title="AI Resume Analyzer", layout="centered")

st.title("📄 AI Resume Analyzer")
st.write("Upload your resume and compare it against a job description.")

st.divider()

resume_file = st.file_uploader("Upload your resume (PDF or DOCX)")
job_description = st.text_area("Paste the job description here", height=200)

if st.button("Analyze Resume"):
    if resume_file is None or job_description.strip() == "":
        st.error("Please upload a resume and paste a job description.")
    else:
        with st.spinner("Analyzing resume..."):
            files = {"file": resume_file}
            data = {"job_description": job_description}

            response = requests.post(API_URL, files=files, data=data)

            if response.status_code == 200:
                result = response.json()

                score = result["score"]
                matched = result["matched"]
                missing = result["missing"]
                feedback = result["feedback"]

                st.subheader("📊 Match Score")
                st.progress(int(score))
                st.write(f"**{score}% match**")

                col1, col2 = st.columns(2)

                with col1:
                    st.subheader("✅ Matched Skills")
                    for skill in matched:
                        st.success(skill)

                with col2:
                    st.subheader("❌ Missing Skills")
                    for skill in missing:
                        st.error(skill)

                st.subheader("🤖 AI Feedback")
                st.info(feedback)

            else:
                st.error("Backend error. Make sure FastAPI is running.")
