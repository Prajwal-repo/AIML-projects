import streamlit as st
from gpt_model import GPT_Model

st.title("AI-Powered Resume Generator 🤖📄")

name = st.text_input("Enter your Name", "")
education = st.text_input("Enter your highest education","")
experience = st.text_area("Enter your Work Experience", "")
skills = st.text_area("Enter your Skills", "")

if st.button("Generate Resume "):
    with st.spinner("Generating... ⏳"):
        resume_text = GPT_Model.generate_resume(name,education, experience, skills)
    st.subheader("Generated Resume:")
    st.write(resume_text)