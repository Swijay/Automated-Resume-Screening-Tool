from pathlib import Path
import PyPDF2
import docx


def read_txt(file_path: str) -> str:
    with open(file_path, "r", encoding="utf-8", errors="ignore") as file:
        return file.read()


def read_pdf(file_path: str) -> str:
    text = ""

    with open(file_path, "rb") as file:
        pdf_reader = PyPDF2.PdfReader(file)

        for page in pdf_reader.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

    return text


def read_docx(file_path: str) -> str:
    document = docx.Document(file_path)

    text = ""

    for paragraph in document.paragraphs:
        text += paragraph.text + "\n"

    return text


def extract_text_from_file(file_path: str) -> str:
    """
    Extract text from TXT, PDF, or DOCX resume.
    """

    extension = Path(file_path).suffix.lower()

    if extension == ".txt":
        return read_txt(file_path)

    elif extension == ".pdf":
        return read_pdf(file_path)

    elif extension == ".docx":
        return read_docx(file_path)

    else:
        raise ValueError("Unsupported file format. Use TXT, PDF, or DOCX.")