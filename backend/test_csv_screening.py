import os
import pandas as pd

from app.matcher import analyze_candidate


# ==============================
# FILE PATHS
# ==============================

CSV_PATH = "data/resume_job_description.csv"
JOB_DESCRIPTION_PATH = "data/job_description.txt"
OUTPUT_PATH = "outputs/csv_screening_results.csv"


# ==============================
# LOAD DATASET
# ==============================

df = pd.read_csv(CSV_PATH)

print("Dataset loaded successfully")
print("Columns:", df.columns.tolist())
print("Shape:", df.shape)


# ==============================
# LOAD JOB DESCRIPTION
# ==============================

with open(JOB_DESCRIPTION_PATH, "r", encoding="utf-8") as file:
    job_description = file.read()


# ==============================
# MUST-HAVE SKILLS
# ==============================

must_have_skills = [
    "python",
    "fastapi",
    "sql",
    "machine learning",
    "git"
]


# ==============================
# SCREEN RESUMES
# ==============================

results = []

# Use first 50 resumes for fast testing
sample_df = df.head(50)

for index, row in sample_df.iterrows():
    resume_text = str(row["Resume_str"])

    candidate_name = f"Candidate_{row['ID']}"
    candidate_category = row["Category"]

    result = analyze_candidate(
        candidate_name=candidate_name,
        resume_text=resume_text,
        job_description=job_description,
        must_have_skills=must_have_skills
    )

    result["category"] = candidate_category

    results.append(result)


# ==============================
# SORT BY FINAL SCORE
# ==============================

results = sorted(results, key=lambda x: x["final_score"], reverse=True)


# ==============================
# SAVE REPORT
# ==============================

os.makedirs("outputs", exist_ok=True)

result_df = pd.DataFrame(results)
result_df.to_csv(OUTPUT_PATH, index=False)


# ==============================
# DISPLAY TOP 10 RESULTS
# ==============================

print("\nTop 10 Ranked Candidates:")
print(
    result_df[
        [
            "candidate_name",
            "category",
            "final_score",
            "recommendation",
            "matched_skills",
            "missing_skills"
        ]
    ].head(10)
)

print("\nCSV report saved at:")
print(OUTPUT_PATH)