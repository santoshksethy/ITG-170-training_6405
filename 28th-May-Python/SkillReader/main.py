from fastapi import FastAPI, UploadFile, File
import pdfplumber
from dotenv import load_dotenv
from openai import OpenAI
import os
load_dotenv()
app = FastAPI()

SKILLS = [
    "python", "java", "sql", "aws", "docker",
    "machine learning", "deep learning", "react",
    "fastapi", "flask", "django"
]

def extract_skills(text):
    text = text.lower()
    return [skill for skill in SKILLS if skill in text]


def extract_text(file: UploadFile):
    with pdfplumber.open(file.file) as pdf:
        text = "\n".join(page.extract_text() or "" for page in pdf.pages)
    return text

def analyze_resume(text: str):
    return {
        "skills": extract_skills(text)
    }


@app.post("/upload-resume")
async def upload_resume(file: UploadFile = File(...)):
    text = extract_text(file)
    structured_data = analyze_resume(text)
    return {"result": structured_data}