import streamlit as st
from llama_cpp import Llama

# Load model
llm = Llama(
    model_path="./llama3-chatbot.gguf",
    n_ctx=2048,
    n_threads=4,        # Adjust depending on CPU
    n_batch=8,
)

st.title("💬 Chat with Fine-Tuned LLaMA 3")

user_input = st.text_input("You:", "")

if user_input:
    prompt = f"[INST] {user_input} [/INST]"
    output = llm(prompt, max_tokens=256, stop=["</s>"])
    response = output["choices"][0]["text"]
    st.write("🧠 LLaMA 3:", response.strip())
