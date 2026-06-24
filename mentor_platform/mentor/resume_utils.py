import PyPDF2
from .ai_utils import get_gemini_response

def extract_text_from_pdf(pdf_file):
    reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text

def analyze_resume(pdf_file, target_role="Software Engineer"):
    resume_text = extract_text_from_pdf(pdf_file)

    prompt = f"""
    You are an expert technical recruiter. Analyze the following resume for a {target_role} position.

    Resume Text:
    {resume_text[:4000]}

    Please provide:
    1. **Overall Score** (out of 10)
    2. **Strengths** (3 bullet points)
    3. **Areas for Improvement** (3 bullet points)
    4. **Missing Keywords** for {target_role} roles
    5. **ATS Compatibility Tips**
    6. **Suggested Projects to Add**
    7. **Summary** (2 sentences)

    Format your response clearly with headers.
    """
    return get_gemini_response(prompt)