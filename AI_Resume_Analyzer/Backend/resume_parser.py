import pdfplumber
import docx


def extract_text_from_pdf(file) -> str:
    text_parts = []
    try:
        with pdfplumber.open(file) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text_parts.append(page_text)
    except Exception as e:
        raise ValueError(f"Failed to parse PDF: {e}")

    result = "\n".join(text_parts).strip()
    if not result:
        raise ValueError("No text could be extracted from the PDF. It may be image-based or empty.")
    return result


def extract_text_from_docx(file) -> str:
    try:
        doc = docx.Document(file)
    except Exception as e:
        raise ValueError(f"Failed to parse DOCX: {e}")

    paragraphs = [p.text for p in doc.paragraphs if p.text.strip()]
    result = "\n".join(paragraphs).strip()
    if not result:
        raise ValueError("No text could be extracted from the DOCX file.")
    return result
