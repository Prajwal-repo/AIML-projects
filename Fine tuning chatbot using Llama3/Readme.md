
# 🦙 Fine-Tuned LLaMA 3 Chatbot

This project demonstrates how to fine-tune and deploy a chatbot using the LLaMA 3 language model and interact with it via a simple Streamlit interface.

## 💡 Features

- Fine-tuned chatbot on custom dataset (training performed separately).
- User-friendly web interface for conversation.
- Local inference using `llama-cpp-python`.

## 🛠 Tech Stack

- **Model**: LLaMA 3 (fine-tuned version in `.gguf` format)
- **Interface**: [Streamlit](https://streamlit.io/)
- **Backend**: [llama-cpp-python](https://github.com/abetlen/llama-cpp-python)
- **Language**: Python

## 📁 Project Structure

```
.
├── front.py                    # Streamlit UI for chatbot interaction
├── Training_model.ipynb        # Notebook for fine-tuning (not included here)
├── llama3-chatbot.gguf         # Fine-tuned model file (ensure it's in the correct path)
└── README.md                   # Project documentation
```

## 🚀 Getting Started

### 1. Install Dependencies

```bash
pip install streamlit llama-cpp-python
```

### 2. Model Setup

Place your fine-tuned `.gguf` LLaMA model file in the root directory and rename it as:

```
llama3-chatbot.gguf
```

### 3. Run the App

```bash
streamlit run front.py
```

## 💬 How It Works

1. User enters a message in the input field.
2. The message is formatted into an LLaMA-style prompt: `[INST] Your input [/INST]`
3. The model generates a response using local inference.
4. Response is displayed in the UI.

## 📌 Notes

- Ensure your system has enough resources (RAM/CPU) to run the `.gguf` model efficiently.
- Fine-tuning is handled in a separate notebook (`Training_model.ipynb`).

## 📬 Contact

For contributions or suggestions, feel free to raise a pull request or issue.

---

Happy chatting! 🤖
