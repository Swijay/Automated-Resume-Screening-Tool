import re
import string


def clean_text(text: str) -> str:
    """
    Cleans resume and job description text.
    """

    if not text:
        return ""

    # Convert to lowercase
    text = text.lower()

    # Remove website links
    text = re.sub(r"http\S+|www\S+|https\S+", " ", text)

    # Remove email addresses
    text = re.sub(r"\S+@\S+", " ", text)

    # Remove punctuation
    text = text.translate(str.maketrans("", "", string.punctuation))

    # Remove extra spaces
    text = re.sub(r"\s+", " ", text).strip()

    return text