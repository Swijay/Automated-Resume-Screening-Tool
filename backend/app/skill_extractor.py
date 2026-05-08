import re


SKILL_KEYWORDS = [
    "python",
    "sql",
    "fastapi",
    "machine learning",
    "git",
    "pandas",
    "numpy",
    "scikit-learn",
    "nlp",
    "docker",
    "next.js",
    "react"
]


def extract_skills(text: str) -> list:
    """
    Extract skills from resume text using keyword matching.
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
    Extract years of experience from resume text.
    """

    text_lower = text.lower()

    year_patterns = [
        r"(\d+\.?\d*)\s*years",
        r"(\d+\.?\d*)\s*year",
        r"(\d+\.?\d*)\s*yrs"
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