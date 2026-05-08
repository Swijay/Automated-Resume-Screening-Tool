from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
import os
import shutil
import json
import pandas as pd

from app.parser import extract_text_from_file
from app.matcher import analyze_candidate


# =====================================================
# FASTAPI APP CONFIGURATION
# =====================================================

app = FastAPI(
    title="Automated Resume Screening Tool",
    description="ML/NLP system for screening and ranking resumes against job descriptions.",
    version="1.0.0"
)


# =====================================================
# CORS CONFIGURATION
# =====================================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# =====================================================
# FOLDER PATHS
# =====================================================

UPLOAD_DIR = "uploaded_resumes"
OUTPUT_DIR = "outputs"

os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)


# =====================================================
# HOME ROUTE
# =====================================================

@app.get("/")
def home():
    return {
        "message": "Automated Resume Screening Tool API is running successfully."
    }


# =====================================================
# SAMPLE RESUME SCREENING ROUTE
# =====================================================

@app.get("/sample-results")
def sample_results():
    """
    This route screens sample resumes stored inside:
    backend/data/resumes/
    
    If your folder is named Resume instead of resumes,
    this code will also handle that automatically.
    """

    job_description_path = "data/job_description.txt"

    # First try lowercase resumes folder
    resume_folder = "data/resumes"

    # If lowercase folder does not exist, try Resume folder
    if not os.path.exists(resume_folder):
        resume_folder = "data/Resume"

    # Check job description file
    if not os.path.exists(job_description_path):
        return {
            "error": "job_description.txt not found.",
            "expected_path": job_description_path
        }

    # Check resume folder
    if not os.path.exists(resume_folder):
        return {
            "error": "Resume folder not found.",
            "expected_path_1": "data/resumes",
            "expected_path_2": "data/Resume"
        }

    # Read job description
    with open(job_description_path, "r", encoding="utf-8") as file:
        job_description = file.read()

    # Must-have skills for screening
    must_have_skills = [
        "python",
        "fastapi",
        "sql",
        "machine learning",
        "git"
    ]

    results = []

    # Read all resume files
    for filename in os.listdir(resume_folder):
        file_path = os.path.join(resume_folder, filename)

        if os.path.isfile(file_path):
            try:
                resume_text = extract_text_from_file(file_path)

                candidate_name = os.path.splitext(filename)[0]

                result = analyze_candidate(
                    candidate_name=candidate_name,
                    resume_text=resume_text,
                    job_description=job_description,
                    must_have_skills=must_have_skills
                )

                results.append(result)

            except Exception as e:
                results.append({
                    "candidate_name": filename,
                    "error": str(e)
                })

    # If no resumes found
    if len(results) == 0:
        return {
            "message": "No resume files found inside resume folder.",
            "resume_folder_used": resume_folder
        }

    # Keep only successful results for sorting
    valid_results = [
        result for result in results
        if "final_score" in result
    ]

    error_results = [
        result for result in results
        if "error" in result
    ]

    valid_results = sorted(
        valid_results,
        key=lambda x: x["final_score"],
        reverse=True
    )

    # Save successful results to CSV
    if valid_results:
        df = pd.DataFrame(valid_results)
        df.to_csv(
            os.path.join(OUTPUT_DIR, "screening_results.csv"),
            index=False
        )

    return {
        "total_candidates": len(valid_results),
        "resume_folder_used": resume_folder,
        "ranked_candidates": valid_results,
        "errors": error_results
    }


# =====================================================
# UPLOAD RESUMES AND SCREEN ROUTE
# =====================================================

@app.post("/screen-resumes")
async def screen_resumes(
    job_description: str = Form(...),
    must_have_skills: str = Form(...),
    files: list[UploadFile] = File(...)
):
    """
    Upload multiple resumes and rank them against a job description.

    must_have_skills should be sent as JSON list string.

    Example:
    ["python", "fastapi", "sql", "machine learning", "git"]
    """

    # Convert must_have_skills string into Python list
    try:
        skills_list = json.loads(must_have_skills)
    except Exception:
        return {
            "error": "must_have_skills must be a valid JSON list.",
            "example": "[\"python\", \"fastapi\", \"sql\", \"machine learning\", \"git\"]"
        }

    results = []

    for file in files:
        file_path = os.path.join(UPLOAD_DIR, file.filename)

        # Save uploaded file
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        try:
            # Extract resume text
            resume_text = extract_text_from_file(file_path)

            candidate_name = os.path.splitext(file.filename)[0]

            # Analyze candidate
            result = analyze_candidate(
                candidate_name=candidate_name,
                resume_text=resume_text,
                job_description=job_description,
                must_have_skills=skills_list
            )

            results.append(result)

        except Exception as e:
            results.append({
                "candidate_name": file.filename,
                "error": str(e)
            })

    # Keep only successful results for sorting
    valid_results = [
        result for result in results
        if "final_score" in result
    ]

    error_results = [
        result for result in results
        if "error" in result
    ]

    valid_results = sorted(
        valid_results,
        key=lambda x: x["final_score"],
        reverse=True
    )

    # Save results to CSV
    if valid_results:
        df = pd.DataFrame(valid_results)
        df.to_csv(
            os.path.join(OUTPUT_DIR, "screening_results.csv"),
            index=False
        )

    return {
        "total_candidates": len(valid_results),
        "ranked_candidates": valid_results,
        "errors": error_results
    }