from app.preprocessing import clean_text


sample_text = """
Rahul Sharma!!! 
Email: rahul@example.com
LinkedIn: https://linkedin.com/in/rahul

I am a Python Developer with FastAPI, SQL, Git, and Machine Learning experience.
"""

cleaned_text = clean_text(sample_text)

print("Original Text:")
print(sample_text)

print("\nCleaned Text:")
print(cleaned_text)