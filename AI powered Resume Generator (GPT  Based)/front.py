import streamlit as st
from gpt_model import GPT_Model

st.title("AI-Powered Resume Generator 🤖📄")

name = st.text_input("Enter your Name", "John Doe")
experience = st.text_area("Enter your Work Experience", "5 years in AI and ML, worked at Google and OpenAI.")
skills = st.text_area("Enter your Skills", "Python, Deep Learning, NLP, Data Science")

if st.button("Generate Resume"):
    with st.spinner("Generating... ⏳"):
        resume_text = GPT_Model.generate_response(name, experience, skills)
    st.subheader("Generated Resume:")
    st.write(resume_text)
