import streamlit as st
import google.generativeai as genai
import PyPDF2
import docx

st.set_page_config(page_title="AI Resume ATS Checker")

api_key = st.secrets.get("GOOGLE_API_KEY")
if not api_key:
    st.error("GOOGLE_API_KEY Streamlit Secrets me add karo")
    st.stop()

genai.configure(api_key=api_key)

def extract_text(file):
    text = ""
    if file.name.endswith(".pdf"):
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text() or ""
    elif file.name.endswith(".docx"):
        doc = docx.Document(file)
        for para in doc.paragraphs:
            text += para.text + "\n"
    return text

st.title("AI Resume ATS Checker")
st.write("Apna Resume upload karo aur Job Description paste karo.")

uploaded_file = st.file_uploader("Resume Upload karo (PDF/DOCX)", type=["pdf","docx"])
job_desc = st.text_area("Job Description yahan paste karo", height=200)

if st.button("Check ATS Score"):
    if not uploaded_file or not job_desc:
        st.warning("Dono cheezen zarori hain - Resume aur Job Description")
    else:
        with st.spinner("Checking..."):
            resume_text = extract_text(uploaded_file)
            prompt = f'''
            You are an ATS checker. Check this resume against job description.
            Resume: {resume_text[:8000]}
            Job Description: {job_desc[:5000]}
            Give: 1. ATS Score out of 100 2. Missing Keywords 3. 3 Suggestions to improve
            Answer in simple English + Urdu mix.
            '''
            try:
                model = genai.GenerativeModel("gemini-2.0-flash")
                response = model.generate_content(prompt)
                st.success("Result:")
                st.write(response.text)
            except Exception as e:
                st.error(f"Error: {e}")import streamlit as st
import google.generativeai as genai
import PyPDF2
import docx

st.set_page_config(page_title="AI Resume ATS Checker")

api_key = st.secrets.get("GOOGLE_API_KEY")
if not api_key:
    st.error("GOOGLE_API_KEY Streamlit Secrets me add karo")
    st.stop()

genai.configure(api_key=api_key)

def extract_text(file):
    text = ""
    if file.name.endswith(".pdf"):
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text() or ""
    elif file.name.endswith(".docx"):
        doc = docx.Document(file)
        for para in doc.paragraphs:
            text += para.text + "\n"
    return text

st.title("AI Resume ATS Checker")
st.write("Apna Resume upload karo aur Job Description paste karo.")

uploaded_file = st.file_uploader("Resume Upload karo (PDF/DOCX)", type=["pdf","docx"])
job_desc = st.text_area("Job Description yahan paste karo", height=200)

if st.button("Check ATS Score"):
    if not uploaded_file or not job_desc:
        st.warning("Dono cheezen zarori hain - Resume aur Job Description")
    else:
        with st.spinner("Checking..."):
            resume_text = extract_text(uploaded_file)
            prompt = f'''
            You are an ATS checker. Check this resume against job description.
            Resume: {resume_text[:8000]}
            Job Description: {job_desc[:5000]}
            Give: 1. ATS Score out of 100 2. Missing Keywords 3. 3 Suggestions to improve
            Answer in simple English + Urdu mix.
            '''
            try:
                model = genai.GenerativeModel("gemini-2.0-flash")
                response = model.generate_content(prompt)
                st.success("Result:")
                st.write(response.text)
            except Exception as e:
                st.error(f"Error: {e}")import streamlit as st
import google.generativeai as genai
import PyPDF2
import docx

st.set_page_config(page_title="AI Resume ATS Checker")

api_key = st.secrets.get("GOOGLE_API_KEY")
if not api_key:
    st.error("GOOGLE_API_KEY Streamlit Secrets me add karo")
    st.stop()

genai.configure(api_key=api_key)

def extract_text(file):
    text = ""
    if file.name.endswith(".pdf"):
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text() or ""
    elif file.name.endswith(".docx"):
        doc = docx.Document(file)
        for para in doc.paragraphs:
            text += para.text + "\n"
    return text

st.title("AI Resume ATS Checker")
st.write("Apna Resume upload karo aur Job Description paste karo.")

uploaded_file = st.file_uploader("Resume Upload karo (PDF/DOCX)", type=["pdf","docx"])
job_desc = st.text_area("Job Description yahan paste karo", height=200)

if st.button("Check ATS Score"):
    if not uploaded_file or not job_desc:
        st.warning("Dono cheezen zarori hain - Resume aur Job Description")
    else:
        with st.spinner("Checking..."):
            resume_text = extract_text(uploaded_file)
            prompt = f'''
            You are an ATS checker. Check this resume against job description.
            Resume: {resume_text[:8000]}
            Job Description: {job_desc[:5000]}
            Give: 1. ATS Score out of 100 2. Missing Keywords 3. 3 Suggestions to improve
            Answer in simple English + Urdu mix.
            '''
            try:
                model = genai.GenerativeModel("gemini-2.0-flash")
                response = model.generate_content(prompt)
                st.success("Result:")
                st.write(response.text)
            except Exception as e:
                st.error(f"Error: {e}")
