# Automated Resume Screening Tool

## Project Overview

The **Automated Resume Screening Tool** is an AI/NLP-based Python project that simulates how companies and HR teams screen resumes against job descriptions.

This project reads resumes in **TXT, PDF, or DOCX** format, extracts resume text, cleans the text, identifies candidate skills and experience, compares resumes with a job description, calculates a matching score, ranks candidates, and generates a final screening report.

This project is designed as an industry-oriented Python, NLP, HR Tech, and automation project for students who want to build a strong GitHub portfolio project.

---

## Problem Statement

Companies receive a large number of resumes for job openings. Manually checking every resume is time-consuming, repetitive, and sometimes inconsistent.

Recruiters need to check:

- Candidate skills
- Work experience
- Education background
- Job role relevance
- Missing must-have skills
- Overall resume-job description match

This project solves the problem by automating the first-level resume screening process using Python and NLP.

---

## Industry Relevance

Automated resume screening is widely used in HR Tech platforms and Applicant Tracking Systems.

Real-world ATS tools help companies:

- Filter resumes quickly
- Shortlist suitable candidates
- Save recruiter time
- Match resumes with job requirements
- Identify missing skills
- Organize candidate ranking reports

This project simulates a real HR screening workflow using sample resumes, synthetic resumes, and a custom job description.

It is useful for roles such as:

- Python Developer
- Data Analyst
- NLP Engineer
- HR Tech Developer
- Automation Engineer
- AI/ML Intern
- Backend Developer

---

## Features

- Extracts text from TXT resumes
- Extracts text from PDF resumes using PyPDF2
- Extracts text from DOCX resumes using python-docx
- Cleans resume and job description text
- Removes emails, URLs, punctuation, and extra spaces
- Extracts skills using keyword matching
- Extracts experience using Regex
- Compares resumes with job description
- Uses TF-IDF vectorization
- Uses cosine similarity scoring
- Calculates skill match score
- Detects matched and missing skills
- Calculates final candidate score
- Ranks candidates from highest score to lowest score
- Generates shortlist decision
- Saves final report as CSV
- Includes optional Streamlit dashboard
- Includes optional FastAPI backend

---

## Tech Stack

| Category | Technology |
|---|---|
| Programming Language | Python |
| Data Handling | Pandas, NumPy |
| NLP / ML | Scikit-learn |
| Text Vectorization | TF-IDF |
| Similarity Method | Cosine Similarity |
| Text Cleaning | Regex |
| PDF Parsing | PyPDF2 |
| DOCX Parsing | python-docx |
| Dashboard | Streamlit |
| API Backend | FastAPI |
| Server | Uvicorn |
| Version Control | Git and GitHub |

---

## Project Architecture

```text
Resume Files
     ↓
Text Extraction
     ↓
Text Cleaning
     ↓
Skill Extraction
     ↓
Experience Extraction
     ↓
Job Description Matching
     ↓
TF-IDF Vectorization
     ↓
Cosine Similarity Scoring
     ↓
Skill Gap Analysis
     ↓
Final Score Calculation
     ↓
Candidate Ranking
     ↓
CSV Report Generation
```

---

## Folder Structure

```text
Automated-Resume-Screening-Tool/
│
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── parser.py
│   │   ├── preprocessing.py
│   │   ├── skill_extractor.py
│   │   └── matcher.py
│   │
│   ├── data/
│   ├── outputs/
│   ├── uploaded_resumes/
│   └── requirements.txt
│
├── data/
│   └── job_description.txt
│
├── docs/
│   ├── project_report.md
│   ├── architecture.md
│   └── interview_questions.md
│
├── images/
│   ├── 01_folder_structure.png
│   ├── 02_sample_resumes.png
│   ├── 03_job_description.png
│   ├── 04_terminal_output.png
│   ├── 05_csv_report.png
│   ├── 06_streamlit_dashboard.png
│   ├── 07_fastapi_home.png
│   └── 08_fastapi_docs.png
│
├── outputs/
│   └── screening_results.csv
│
├── resumes/
│   ├── strong_resume_high_score.pdf
│   ├── low_score_resume.pdf
│   ├── resume_1.txt
│   ├── resume_2.txt
│   └── resume_3.txt
│
├── screenshots/
├── src/
│   ├── __init__.py
│   ├── parser.py
│   ├── preprocessing.py
│   ├── skill_extractor.py
│   ├── matcher.py
│   └── report_generator.py
│
├── app_streamlit.py
├── main.py
├── README.md
├── requirements.txt
└── .gitignore
```

---

## Folder Explanation

| Folder / File | Purpose |
|---|---|
| `resumes/` | Stores sample resume files in TXT, PDF, or DOCX format |
| `data/` | Stores job description and dataset files |
| `src/` | Contains core Python modules |
| `outputs/` | Stores generated CSV screening reports |
| `images/` | Stores screenshots for GitHub README |
| `docs/` | Stores project report and documentation |
| `backend/` | Contains FastAPI backend version |
| `main.py` | Runs the main Python resume screening workflow |
| `app_streamlit.py` | Runs the optional Streamlit dashboard |
| `requirements.txt` | Contains required Python libraries |
| `.gitignore` | Prevents unnecessary files from being uploaded |

---

## Installation Guide

### 1. Clone the Repository

```bash
git clone https://github.com/Swijay/Automated-Resume-Screening-Tool.git
cd Automated-Resume-Screening-Tool
```

---

### 2. Create Virtual Environment

#### Windows

```bash
python -m venv venv
.\venv\Scripts\activate
```

#### Mac/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3. Install Required Libraries

```bash
python -m pip install -r requirements.txt
```

---

## Required Libraries

```txt
pandas
numpy
scikit-learn
PyPDF2
python-docx
streamlit
fastapi
uvicorn
python-multipart
pydantic
```

---

## How to Run the Project

### Run Main Python Project

Make sure resume files are placed inside:

```text
resumes/
```

Then run:

```bash
python main.py
```

---

## Expected Terminal Output

```text
============================================================
Automated Resume Screening Tool
============================================================

Top 10 Ranked Candidates:
              candidate_name  final_score                    decision  experience_years
0    strong_resume_high_score        85.50  Shortlisted - Strong Match              2.0
1                   resume_1        78.20  Shortlisted - Strong Match              1.5
2                   resume_2        55.30   Review - Moderate Match                1.0
3                   resume_3        34.80      Rejected - Low Match                0.67
4            low_score_resume        8.50       Rejected - Low Match                1.0

Report saved successfully at: outputs/screening_results.csv

Project executed successfully.
```

Exact scores may vary depending on resume content.

---

## Generated CSV Output

After running the project, a CSV report is generated at:

```text
outputs/screening_results.csv
```

The CSV contains:

- Candidate name
- Similarity score
- Skill match score
- Final score
- Shortlist decision
- Experience years
- Matched skills
- Missing skills
- Extracted skills
- Explanation

---

## Sample Output

| Candidate Name | Final Score | Decision | Missing Skills |
|---|---:|---|---|
| strong_resume_high_score | 85.50 | Shortlisted - Strong Match | None |
| resume_1 | 78.20 | Shortlisted - Strong Match | None |
| resume_2 | 55.30 | Review - Moderate Match | FastAPI, Machine Learning |
| resume_3 | 34.80 | Rejected - Low Match | Python, FastAPI, SQL, Machine Learning |
| low_score_resume | 8.50 | Rejected - Low Match | Python, FastAPI, SQL, Machine Learning, Git |

---

## Scoring Logic

The system calculates two main scores.

### 1. Skill Match Score

```text
Skill Match Score = Matched Required Skills / Total Required Skills × 100
```

### 2. Resume-JD Similarity Score

The system uses:

```text
TF-IDF Vectorization + Cosine Similarity
```

This compares the overall resume text with the job description.

### 3. Final Score

```text
Final Score = 50% Resume-JD Similarity Score + 50% Skill Match Score
```

---

## Shortlist Decision Logic

| Final Score | Decision |
|---:|---|
| 75% and above | Shortlisted - Strong Match |
| 50% to 74% | Review - Moderate Match |
| Below 50% | Rejected - Low Match |

---

## Run Streamlit Dashboard

To run the optional dashboard:

```bash
python -m streamlit run app_streamlit.py
```

Then open:

```text
http://localhost:8501
```

The Streamlit dashboard allows the user to:

- Upload resumes
- Enter job description
- Enter required skills
- Screen candidates
- View ranked results
- Download CSV report

---

## Run FastAPI Backend

Go inside the backend folder:

```bash
cd backend
```

Run the backend:

```bash
python -m uvicorn app.main:app --reload
```

Open API home:

```text
http://127.0.0.1:8000
```

Open API documentation:

```text
http://127.0.0.1:8000/docs
```

Open sample results:

```text
http://127.0.0.1:8000/sample-results
```

---

## Screenshots

Add your screenshots inside the `images/` folder.

Recommended screenshots:

| Screenshot | Description |
|---|---|
| `images/01_folder_structure.png` | VS Code project folder structure |
| `images/02_sample_resumes.png` | Sample resume files |
| `images/03_job_description.png` | Job description file |
| `images/04_terminal_output.png` | Output after running `python main.py` |
| `images/05_csv_report.png` | Generated CSV screening report |
| `images/06_streamlit_dashboard.png` | Streamlit dashboard |
| `images/07_fastapi_home.png` | FastAPI home route |
| `images/08_fastapi_docs.png` | FastAPI Swagger documentation |

Example markdown to display screenshots:

```md
![Folder Structure](image1_folderStructure.png)

![Terminal Output](images/04_terminal_output.png)

![CSV Report](images/05_csv_report.png)

![Streamlit Dashboard](images/06_streamlit_dashboard.png)
```

---

## Virtual Simulation

This project uses virtual simulation because real company ATS data is not publicly available.

The simulation includes:

- Sample resumes
- PDF resume examples
- TXT resume examples
- Custom job description
- Required skill list
- Resume-job matching
- Candidate ranking
- CSV report generation

Example simulated hiring role:

```text
Role: Python Developer

Required Skills:
Python, FastAPI, SQL, Machine Learning, Git
```

Example candidate types:

```text
Strong Candidate:
Has Python, FastAPI, SQL, Machine Learning, Git, Pandas, Scikit-learn

Low Match Candidate:
Has Photoshop, Canva, Illustrator, Branding, Video Editing
```

---

## Project Workflow

```text
1. User adds resumes to resumes folder
2. User adds job description to data/job_description.txt
3. System extracts text from resumes
4. System cleans the extracted text
5. System extracts skills and experience
6. System compares resume with job description
7. System calculates similarity score
8. System calculates skill match score
9. System calculates final score
10. System ranks candidates
11. System generates shortlist decision
12. System saves CSV report
```

---

## Learning Outcomes

By building this project, I learned:

- How resume screening systems work
- How ATS systems use keywords and job descriptions
- How to extract text from PDF, DOCX, and TXT files
- How to clean text using Regex
- How to extract skills from resume text
- How to extract experience using pattern matching
- How to use TF-IDF for text vectorization
- How to calculate cosine similarity
- How to rank candidates using score-based logic
- How to generate CSV reports using Pandas
- How to build a Streamlit dashboard
- How to create a FastAPI backend
- How to structure a GitHub-ready Python project

---

## Limitations

This is an educational simulation project. It is not a complete real-world ATS system.

Current limitations:

- Skill extraction is keyword-based
- Semantic meaning is limited
- Resume formatting may affect PDF extraction
- Real hiring decisions require human review
- Bias and fairness checks are not included
- Large-scale database storage is not included

---

## Future Improvements

- Add spaCy Named Entity Recognition
- Add Sentence Transformers for semantic matching
- Add database support using SQLite or PostgreSQL
- Add recruiter login system
- Add candidate upload history
- Add advanced analytics dashboard
- Add Docker deployment
- Add bias detection and fairness checks
- Add education and certification extraction
- Add detailed candidate profile view

---

## Use Cases

- HR resume screening
- Candidate shortlisting
- Skill gap analysis
- Recruitment automation
- ATS simulation
- Python course project
- NLP portfolio project
- Data analysis project
- AI/ML internship project

---

## Author

**Swijay Singh**

**Email:** swijaysingh@example.com

GitHub: [https://github.com/Swijay?tab=repositories]

---

## Acknowledgement

This project was created as an industry-oriented Python, NLP, and automation project for learning, portfolio building, and GitHub proof of work.

---

## Project Status

```text
Completed: Core Python version
Completed: Resume text extraction
Completed: Skill matching
Completed: TF-IDF similarity scoring
Completed: CSV report generation
Completed: Streamlit dashboard
Completed: FastAPI backend
```