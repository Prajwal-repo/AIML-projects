from huggingface_hub import InferenceClient
import os

hf_token = os.getenv("HUGGINGFACEHUB_API_TOKEN","")

client = InferenceClient(
    model="openai-community/gpt2", 
    token=hf_token  
)

class GPT_Model:
    def generate_resume(name,education, experience, skills):

        prompt = f"""
You are an AI assistant that generates professional resumes in a structured format. 
Below is an example of a well-formatted resume:

---
**Name:** Jane Smith  
**Highest Education:** Mtech in CS
**Professional Summary:** I am an enthusiast and very hard working for my work.
**Experience:**  
- 7 years in Data Science, worked at Meta and IBM.  
- Specialized in machine learning and deep learning models.  

**Skills:** Python, TensorFlow, NLP, Cloud Computing  
---

Now generate a similar resume for:  

**Name:** {name}  
**Highest Education:** {education}
**Experience:** {experience}  
**Skills:** {skills}  

Ensure the resume is structured like the example.
"""

        response = client.text_generation(prompt, max_new_tokens=100, temperature=0.5)
        return response.strip()
    
