
# 🤖 AI-Powered Resume Generator

This project is a simple yet powerful web application that uses AI to automatically generate professional resumes based on user input.

## 🚀 Features

- Collects user's name, education, experience, and skills via a web form.
- Generates a clean and structured resume using a GPT-2 model hosted on Hugging Face.
- Built with Streamlit for an interactive user interface.

## 🛠 Tech Stack

- **Frontend/UI**: [Streamlit](https://streamlit.io/)
- **Model**: [GPT-2](https://huggingface.co/openai-community/gpt2) via Hugging Face Inference API
- **Language**: Python

## 📁 Project Structure

```
.
├── front.py         # Streamlit UI
├── gpt_model.py     # GPT resume generation logic
└── README.md        # Project documentation
```

## 🧠 How It Works

1. User enters details like name, education, work experience, and skills.
2. A structured prompt is crafted and sent to the GPT-2 model via Hugging Face's API.
3. The model returns a formatted resume, which is displayed in the app.

## 🧪 Setup Instructions

1. **Clone the repo**:
    ```bash
    git clone https://github.com/yourusername/ai-resume-generator.git
    cd ai-resume-generator
    ```

2. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Set your Hugging Face API token**:
    ```bash
    export HUGGINGFACEHUB_API_TOKEN=your_token_here
    ```

4. **Run the app**:
    ```bash
    streamlit run front.py
    ```

## 📄 Sample Output

```
**Name:** John Doe  
**Highest Education:** B.Tech in Mechanical Engineering  
**Professional Summary:** I am passionate and driven about creating innovative engineering solutions.  
**Experience:**  
- 5 years in automotive design at Tesla and Mahindra.  
- Specialized in CAD modeling and FEA analysis.  

**Skills:** AutoCAD, SolidWorks, ANSYS, Project Management  
```

## 📬 Contact

For suggestions or contributions, feel free to create an issue or a pull request.

---

Happy resume building! 🎯
