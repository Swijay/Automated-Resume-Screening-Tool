import os
from pathlib import Path

from src.parser import extract_text_from_file
from src.matcher import analyze_candidate
from src.report_generator import save_report, print_top_candidates


RESUME_FOLDER = "resumes"
JOB_DESCRIPTION_PATH = "data/job_description.txt"
OUTPUT_PATH = "outputs/screening_results.csv"


def load_job_description(file_path: str) -> str:
    """
    Loads job description from text file.
    """

    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


def get_resume_files(folder_path: str) -> list:
    """
    Returns all TXT, PDF, and DOCX resume files from resumes folder.
    """

    supported_extensions = [".txt", ".pdf", ".docx"]

    resume_files = []

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        extension = Path(filename).suffix.lower()

        if os.path.isfile(file_path) and extension in supported_extensions:
            resume_files.append(file_path)

    return resume_files


def main():
    print("=" * 60)
    print("Automated Resume Screening Tool")
    print("=" * 60)

    if not os.path.exists(JOB_DESCRIPTION_PATH):
        print(f"Job description not found at: {JOB_DESCRIPTION_PATH}")
        return

    if not os.path.exists(RESUME_FOLDER):
        print(f"Resume folder not found at: {RESUME_FOLDER}")
        return

    job_description = load_job_description(JOB_DESCRIPTION_PATH)

    required_skills = [
        "python",
        "fastapi",
        "sql",
        "machine learning",
        "git"
    ]

    resume_files = get_resume_files(RESUME_FOLDER)

    if not resume_files:
        print("No TXT, PDF, or DOCX resumes found inside resumes folder.")
        return

    results = []

    for resume_file in resume_files:
        try:
            resume_text = extract_text_from_file(resume_file)

            candidate_name = Path(resume_file).stem

            result = analyze_candidate(
                candidate_name=candidate_name,
                resume_text=resume_text,
                job_description=job_description,
                required_skills=required_skills
            )

            results.append(result)

        except Exception as error:
            print(f"Error processing {resume_file}: {error}")

    results = sorted(results, key=lambda x: x["final_score"], reverse=True)

    print_top_candidates(results, top_n=10)

    save_report(results, OUTPUT_PATH)

    print("\nProject executed successfully.")


if __name__ == "__main__":
    main()