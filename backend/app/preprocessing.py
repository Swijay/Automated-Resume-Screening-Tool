import re
import string


def clean_text(text: str) -> str:
    """
    This function cleans resume and job description text.
    It removes unwanted things like emails, URLs, punctuation,
    extra spaces, and converts text into lowercase.
    """

    # If text is empty, return empty string
    if not text:
        return ""

    # Convert text to lowercase
    text = text.lower()

    # Remove website links
    text = re.sub(r"http\S+|www\S+|https\S+", " ", text)

    # Remove email addresses
    text = re.sub(r"\S+@\S+", " ", text)

    # Remove punctuation like . , ! ? : ;
    text = text.translate(str.maketrans("", "", string.punctuation))

    # Remove extra spaces
    text = re.sub(r"\s+", " ", text).strip()

    return text