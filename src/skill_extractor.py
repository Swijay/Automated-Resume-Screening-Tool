import re


SKILL_KEYWORDS = [
    "python",
    "java",
    "c++",
    "sql",
    "mysql",
    "postgresql",
    "mongodb",
    "fastapi",
    "flask",
    "django",
    "rest api",
    "api",
    "machine learning",
    "deep learning",
    "data science",
    "data analysis",
    "nlp",
    "pandas",
    "numpy",
    "matplotlib",
    "seaborn",
    "scikit-learn",
    "sklearn",
    "tensorflow",
    "pytorch",
    "excel",
    "power bi",
    "tableau",
    "git",
    "github",
    "docker",
    "html",
    "css",
    "javascript",
    "react",
    "next.js",
    "tailwind css"
]


def extract_skills(text: str) -> list:
    """
    Extracts skills from resume text using keyword matching.
    """

    found_skills = []
    text_lower = text.lower()

    for skill in SKILL_KEYWORDS:
        pattern = r"\b" + re.escape(skill.lower()) + r"\b"

        if re.search(pattern, text_lower):
            found_skills.append(skill)

    return sorted(list(set(found_skills)))


def extract_experience(text: str) -> float:
    """
    Extracts years of experience from text.

    Examples:
    '1 year'       -> 1.0
    '1.5 years'    -> 1.5
    '8 months'     -> 0.67
    '2 yrs'        -> 2.0
    """

    text_lower = text.lower()

    year_patterns = [
        r"(\d+\.?\d*)\s*years",
        r"(\d+\.?\d*)\s*year",
        r"(\d+\.?\d*)\s*yrs",
        r"(\d+\.?\d*)\s*yr"
    ]

    for pattern in year_patterns:
        match = re.search(pattern, text_lower)

        if match:
            return float(match.group(1))

    month_match = re.search(r"(\d+\.?\d*)\s*months", text_lower)

    if month_match:
        months = float(month_match.group(1))
        return round(months / 12, 2)

    return 0.0