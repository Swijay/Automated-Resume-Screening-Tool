from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from app.preprocessing import clean_text
from app.skill_extractor import extract_skills, extract_experience


def calculate_similarity(resume_text: str, job_description: str) -> float:
    """
    Calculate resume and job description similarity using TF-IDF.
    """

    cleaned_resume = clean_text(resume_text)
    cleaned_jd = clean_text(job_description)

    documents = [cleaned_resume, cleaned_jd]

    vectorizer = TfidfVectorizer(stop_words="english")
    tfidf_matrix = vectorizer.fit_transform(documents)

    similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]

    return round(similarity * 100, 2)


def calculate_skill_match(candidate_skills: list, required_skills: list) -> float:
    """
    Calculate must-have skill match percentage.
    """

    if not required_skills:
        return 0.0

    candidate_skills_set = set(candidate_skills)
    required_skills_set = set(required_skills)

    matched_skills = candidate_skills_set.intersection(required_skills_set)

    score = (len(matched_skills) / len(required_skills_set)) * 100

    return round(score, 2)


def analyze_candidate(candidate_name: str, resume_text: str, job_description: str, must_have_skills: list) -> dict:
    """
    Analyze one candidate resume.
    """

    candidate_skills = extract_skills(resume_text)
    experience = extract_experience(resume_text)

    similarity_score = calculate_similarity(resume_text, job_description)
    skill_match_score = calculate_skill_match(candidate_skills, must_have_skills)

    matched_skills = sorted(list(set(candidate_skills).intersection(set(must_have_skills))))
    missing_skills = sorted(list(set(must_have_skills) - set(candidate_skills)))

    final_score = round((similarity_score * 0.5) + (skill_match_score * 0.5), 2)

    if final_score >= 75:
        recommendation = "Strong Match"
    elif final_score >= 50:
        recommendation = "Moderate Match"
    else:
        recommendation = "Low Match"

    return {
        "candidate_name": candidate_name,
        "similarity_score": similarity_score,
        "skill_match_score": skill_match_score,
        "final_score": final_score,
        "recommendation": recommendation,
        "experience_years": experience,
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "all_extracted_skills": candidate_skills,
        "explanation": f"{candidate_name} scored {final_score}% based on resume-job similarity and must-have skill matching."
    }