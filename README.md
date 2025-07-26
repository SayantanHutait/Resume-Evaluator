# Resume Fit Evaluator (with Gemini AI)

This project is an AI-powered **Resume Fit Evaluator** built with **Streamlit** and **Google Gemini AI**. It analyzes your resume against a given job description and provides:
- **Key requirements** of the job.
- **Fit Score (out of 100)**.
- **Strengths and weaknesses** of your resume.
- **Suggestions for improvements**.

---

## 🚀 Features
- **PDF Resume Upload** – Upload your resume in PDF format.
- **Job Description URL Input** – Provide a job listing URL.
- **AI-Powered Evaluation** – Uses **Google Gemini LLM** (via LangChain) to compare your resume with the job description.
- **Fit Score & Feedback** – Get actionable insights on how to improve your resume for better job alignment.

---

## 🛠️ Tech Stack
- **Python 3.10+**
- **Streamlit** – For the interactive web app.
- **LangChain** – To integrate with Gemini AI.
- **Google Gemini API** – For LLM-powered analysis.
- **PyMuPDF** – For extracting text from PDF resumes.
- **dotenv** – For managing environment variables.

---

## 📦 Installation
### 1. Clone this repository:
```bash
git clone https://github.com/your-username/resume-fit-evaluator.git
cd resume-fit-evaluator
