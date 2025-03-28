from langchain_huggingface import HuggingFaceEndpoint
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import os

hf_token = os.getenv("HUGGINGFACEHUB_API_TOKEN","")

class GPT_Model:
    def generate_response(name, experience, skills):

        model_id="openai-community/gpt2"
        model = HuggingFaceEndpoint(repo_id=model_id,max_new_tokens=500,temperature=0.7,task="text-generation",huggingfacehub_api_token=hf_token,model_kwargs={})

        resume_prompt = PromptTemplate(
        input_variables=["name", "experience", "skills"],
        template="""
        You are an expert resume writer. Create a professional resume for {name} in a well-structured format.

        **Personal Information:**
        - Name: {name}

        **Experience:**
        {experience}

        **Skills:**
        - {skills}

        Ensure the resume is well-formatted and written in a professional tone.
       """)
        chain = LLMChain(llm=model, prompt=resume_prompt)
        return chain.run(name=name, experience=experience, skills=skills)
    
