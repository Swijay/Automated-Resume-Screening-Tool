import os
import tempfile
import pandas as pd
import streamlit as st

from src.parser import extract_text_from_file
from src.matcher import analyze_candidate


st.set_page_config(
    page_title="Automated Resume Screening Tool",
    page_icon="📄",
    layout="wide"
)


st.title("📄 Automated Resume Screening Tool")
st.write(
    "Upload resumes, enter a job description, add required skills, "
    "and rank candidates automatically using NLP."
)


st.sidebar.header("Project Controls")

required_skills_input = st.sidebar.text_area(
    "Enter required skills separated by commas",
    value="python, fastapi, sql, machine learning, git"
)

required_skills = [
    skill.strip().lower()
    for skill in required_skills_input.split(",")
    if skill.strip()
]


job_description = st.text_area(
    "Enter Job Description",
    height=220,
    value="""We are hiring a Python Developer with strong knowledge of Python, FastAPI, REST API development, SQL, machine learning, data analysis, Git, and basic NLP.

The candidate should have experience in building backend APIs, working with datasets, cleaning data, and deploying machine learning models.

Must-have skills: Python, FastAPI, SQL, Machine Learning, Git."""
)


uploaded_files = st.file_uploader(
    "Upload Resume Files",
    type=["txt", "pdf", "docx"],
    accept_multiple_files=True
)


if st.button("Screen Resumes"):
    if not uploaded_files:
        st.error("Please upload at least one resume file.")

    elif not job_description.strip():
        st.error("Please enter a job description.")

    elif not required_skills:
        st.error("Please enter required skills.")

    else:
        results = []

        with st.spinner("Screening resumes..."):
            for uploaded_file in uploaded_files:
                try:
                    suffix = os.path.splitext(uploaded_file.name)[1]

                    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as temp_file:
                        temp_file.write(uploaded_file.read())
                        temp_file_path = temp_file.name

                    resume_text = extract_text_from_file(temp_file_path)

                    candidate_name = os.path.splitext(uploaded_file.name)[0]

                    result = analyze_candidate(
                        candidate_name=candidate_name,
                        resume_text=resume_text,
                        job_description=job_description,
                        required_skills=required_skills
                    )

                    results.append(result)

                    os.remove(temp_file_path)

                except Exception as error:
                    st.error(f"Error processing {uploaded_file.name}: {error}")

        if results:
            results = sorted(results, key=lambda x: x["final_score"], reverse=True)

            df = pd.DataFrame(results)

            st.success("Resume screening completed.")

            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric("Total Candidates", len(df))

            with col2:
                shortlisted_count = len(df[df["decision"].str.contains("Shortlisted")])
                st.metric("Shortlisted", shortlisted_count)

            with col3:
                average_score = round(df["final_score"].mean(), 2)
                st.metric("Average Score", average_score)

            st.subheader("Ranked Candidates")

            st.dataframe(
                df[
                    [
                        "candidate_name",
                        "similarity_score",
                        "skill_match_score",
                        "final_score",
                        "decision",
                        "experience_years",
                        "matched_skills",
                        "missing_skills",
                        "explanation"
                    ]
                ],
                use_container_width=True
            )

            os.makedirs("outputs", exist_ok=True)

            output_path = "outputs/streamlit_screening_results.csv"
            df.to_csv(output_path, index=False)

            csv_data = df.to_csv(index=False).encode("utf-8")

            st.download_button(
                label="Download CSV Report",
                data=csv_data,
                file_name="resume_screening_results.csv",
                mime="text/csv"
            )