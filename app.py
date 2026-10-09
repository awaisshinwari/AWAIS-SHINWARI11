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
            t = page.extract_text()
            if t:
                text += t
    elif file.name.endswith(".docx"):
        doc = docx.Document(file)
        for para in doc.paragraphs:
            text += para.text + "\n"
    return text

st.title("AI Resume ATS Checker")
st.write("Apna Resume upload karo aur Job Description paste karo.")

uploaded_file = st.file_uploader("Resume Upload karo (PDF/DOCX)", type=["pdf", "docx"])
job_desc = st.text_area("Job Description yahan paste karo", height=200)

if st.button("Check ATS Score"):
    if not uploaded_file or not job_desc:
        st.warning("Dono cheezen zarori hain - Resume aur Job Description")
    else:
        with st.spinner("Checking..."):
            resume_text = extract_text(uploaded_file)
            prompt = "You are ATS checker. Resume: " + resume_text[:8000] + " Job Desc: " + job_desc[:5000] + " Give ATS Score out of 100, Missing Keywords, and 3 Suggestions."
            try:
                model = genai.GenerativeModel("gemini-3.8-flash")
                response = model.generate_content(prompt)
                st.success("Result:")
                st.write(response.text)
            except Exception as err:
                st.error("Error occurred")
                st.write(str(err))
