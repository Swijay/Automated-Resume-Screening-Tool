from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from src.preprocessing import clean_text
from src.skill_extractor import extract_skills, extract_experience


def calculate_similarity(resume_text: str, job_description: str) -> float:
    """
    Calculates resume-job description similarity using TF-IDF and cosine similarity.
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
    Calculates how many required skills are present in the resume.
    """

    if not required_skills:
        return 0.0

    candidate_skills_set = set([skill.lower() for skill in candidate_skills])
    required_skills_set = set([skill.lower() for skill in required_skills])

    matched_skills = candidate_skills_set.intersection(required_skills_set)

    score = (len(matched_skills) / len(required_skills_set)) * 100

    return round(score, 2)


def get_shortlist_decision(final_score: float) -> str:
    """
    Gives shortlist decision based on final score.
    """

    if final_score >= 75:
        return "Shortlisted - Strong Match"

    elif final_score >= 50:
        return "Review - Moderate Match"

    else:
        return "Rejected - Low Match"


def analyze_candidate(
    candidate_name: str,
    resume_text: str,
    job_description: str,
    required_skills: list
) -> dict:
    """
    Complete analysis of one candidate resume.
    """

    candidate_skills = extract_skills(resume_text)
    experience_years = extract_experience(resume_text)

    similarity_score = calculate_similarity(resume_text, job_description)
    skill_match_score = calculate_skill_match(candidate_skills, required_skills)

    candidate_skills_set = set([skill.lower() for skill in candidate_skills])
    required_skills_set = set([skill.lower() for skill in required_skills])

    matched_skills = sorted(list(candidate_skills_set.intersection(required_skills_set)))
    missing_skills = sorted(list(required_skills_set - candidate_skills_set))

    final_score = round((similarity_score * 0.5) + (skill_match_score * 0.5), 2)

    decision = get_shortlist_decision(final_score)

    explanation = (
        f"{candidate_name} scored {final_score}%. "
        f"Resume-JD similarity is {similarity_score}%, "
        f"skill match is {skill_match_score}%, "
        f"and missing skills are: {', '.join(missing_skills) if missing_skills else 'None'}."
    )

    return {
        "candidate_name": candidate_name,
        "similarity_score": similarity_score,
        "skill_match_score": skill_match_score,
        "final_score": final_score,
        "decision": decision,
        "experience_years": experience_years,
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "all_extracted_skills": candidate_skills,
        "explanation": explanation
    }