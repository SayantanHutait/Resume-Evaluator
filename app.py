import os
from dotenv import load_dotenv
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate
from langchain_community.document_loaders import PyMuPDFLoader
from langchain_community.document_loaders import WebBaseLoader
from langchain.schema.runnable import RunnableLambda, RunnableSequence

load_dotenv()
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")
os.environ["LANGSMITH_API_KEY"] = os.getenv("LANGSMITH_API_KEY")
os.environ["LANGSMITH_TRACING"] = os.getenv("LANGSMITH_TRACING")



llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0.3)


score_prompt = ChatPromptTemplate.from_template("""
You are an expert resume reviewer.

Compare the following resume with the job description (write in simple text. not bold or *) and:
- Give Requirements of the Job descripton in short
- Give a Fit Score out of 100
- List strengths and weaknesses
- Suggest improvements in short

Resume:
{resume}

Job Description:
{job}
""")


chain = score_prompt | llm


def load_resume(file_path):
    loader = PyMuPDFLoader(file_path)
    docs = loader.load()
    return "\n".join([doc.page_content for doc in docs])

def job_des(url):
    loader = WebBaseLoader(url)
    docs = loader.load()
    return "\n".join([doc.page_content for doc in docs])

# Streamlit UI
st.set_page_config(page_title="Resume Fit Evaluator", layout="centered")
st.title("Resume Fit Evaluator with Gemini AI")
st.write("Upload your resume and provide a job listing URL to get a fit score and feedback.")

uploaded_file = st.file_uploader("Upload your resume (PDF)", type=["pdf"])
job_url = st.text_input("Enter Job Description URL")

evaluate_clicked = st.button("Evaluate", key="evaluate_button")

if evaluate_clicked:
    if uploaded_file and job_url:
        with st.spinner("Reading your resume and job description..."):
            # Save uploaded file temporarily
            with open("temp_resume.pdf", "wb") as f:
                f.write(uploaded_file.getbuffer())

            resume_text = load_resume("temp_resume.pdf")
            job_description = job_des(job_url)

            # Run chain
            result = chain.invoke({
                "resume": resume_text,
                "job": job_description
            })

            st.success("✅ Evaluation Complete!")
            st.subheader("Fit Evaluation:")
            st.write(result.content)

    else:
        st.warning("⚠️ Please upload a resume and enter a job URL.")
