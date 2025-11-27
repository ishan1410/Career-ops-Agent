import streamlit as st
import os
from pypdf import PdfReader
from agent import get_agent
from dotenv import load_dotenv

# Load env vars
load_dotenv()

st.set_page_config(page_title="CareerOps Agent", page_icon="🚀")

st.title("CareerOps Agent")
st.markdown("Generate a tailored cover letter by providing a Job URL and your Resume.")

# Sidebar for API Key (Optional if already in .env)
# st.sidebar.header("Configuration")
# api_key = st.sidebar.text_input("Google API Key", type="password")
# if api_key:
#     os.environ["GOOGLE_API_KEY"] = api_key

# Inputs
job_url = st.text_input("Job Description URL", placeholder="https://boards.greenhouse.io/...")
uploaded_file = st.file_uploader("Upload Resume (PDF)", type="pdf")

if st.button("Generate Cover Letter"):
    if not job_url:
        st.error("Please enter a Job URL.")
    elif not uploaded_file:
        st.error("Please upload a resume.")
    else:
        with st.spinner("Processing..."):
            try:
                # Read PDF
                reader = PdfReader(uploaded_file)
                resume_text = ""
                for page in reader.pages:
                    resume_text += page.extract_text()
                
                if not resume_text.strip():
                    st.error("Could not extract text from the PDF. Please try a different file.")
                else:
                    # Initialize Agent
                    agent_executor = get_agent(resume_text)
                    
                    # Run Agent
                    prompt = f"Scrape the job description from the URL {job_url}. Then, search my resume for matching skills. Finally, write a cover letter tailored to this job."
                    response = agent_executor.invoke({"input": prompt})
                    
                    # Display Output
                    st.subheader("Generated Cover Letter")
                    st.markdown(response["output"])
                    
            except Exception as e:
                st.error(f"An error occurred: {e}")
