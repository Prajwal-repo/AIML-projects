from langchain_huggingface import HuggingFaceEndpoint
import os

hf_token = os.getenv("HUGGINGFACEHUB_API_TOKEN","")
class GPT_Model:
    def generate_response(self,text_input):
        model_id="openai-community/gpt2"
        self.model = HuggingFaceEndpoint(repo_id=model_id,max_new_tokens=150,temperature=0.7,task="text-generation",huggingfacehub_api_token=hf_token,model_kwargs={})
        response = self.model.invoke(text_input)
        return response
    

