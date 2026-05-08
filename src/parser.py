from pathlib import Path
import PyPDF2
import docx


def read_txt(file_path: str) -> str:
    """
    Reads text from a TXT resume file.
    """

    with open(file_path, "r", encoding="utf-8", errors="ignore") as file:
        return file.read()


def read_pdf(file_path: str) -> str:
    """
    Extracts text from a PDF resume file using PyPDF2.
    """

    text = ""

    with open(file_path, "rb") as file:
        pdf_reader = PyPDF2.PdfReader(file)

        for page in pdf_reader.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

    return text


def read_docx(file_path: str) -> str:
    """
    Extracts text from a DOCX resume file using python-docx.
    """

    document = docx.Document(file_path)
    text = ""

    for paragraph in document.paragraphs:
        text += paragraph.text + "\n"

    return text


def extract_text_from_file(file_path: str) -> str:
    """
    Detects file type and extracts text.
    Supported formats:
    - TXT
    - PDF
    - DOCX
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