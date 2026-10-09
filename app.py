import streamlit as st
import google.generativeai as genai
import pypdf
import docx
import os

def extract_text(uploaded_file):
    text = ""
    if uploaded_file.name.endswith(".pdf"):
        reader = pypdf.PdfReader(uploaded_file)
        for page in reader.pages:
            text += page.extract_text() or ""
    elif uploaded_file.name.endswith(".docx"):
        doc = docx.Document(uploaded_file)
        for para in doc.paragraphs:
            text += para.text + "\n"
    else:
        text = uploaded_file.read().decode("utf-8", errors="ignore")
    return text

# Page Config
st.set_page_config(page_title="AI Resume ATS Checker", page_icon="📄", layout="centered")
st.title("📄 AI Resume ATS Checker")
st.write("Apna Resume upload karo aur Job Description paste karo.")

# API Key
try:
    api_key = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=api_key)
except:
    st.error("GOOGLE_API_KEY Streamlit Secrets me add karo")
    st.stop()

model = genai.GenerativeModel("gemini-2.0-flash")

uploaded_resume = st.file_uploader("Resume Upload karo (PDF/DOCX)", type=["pdf", "docx"])
job_desc = st.text_area("Job Description yahan paste karo", height=200)

if st.button("Check ATS Score"):
    if not uploaded_resume or not job_desc:
        st.warning("Dono cheezein zaroori hain!")
    else:
        with st.spinner("Checking..."):
            resume_text = extract_text(uploaded_resume)
            prompt = f"""
            You are an ATS Resume Expert.
            Job Description:
            {job_desc}

            Resume:
            {resume_text}

            Give output in this format:
            1. ATS Match Score in % (e.g. 75%)
            2. Missing Keywords
            3. Strengths
            4. Improvements / Suggestions to improve resume
            5. Final Verdict

            Keep language simple and in Roman Urdu / English mix.
            """
            response = model.generate_content(prompt)
            st.success("Result Ready!")
            st.markdown(response.text)
