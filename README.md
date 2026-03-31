# 🤖 ML Chatbot (RAG-Based Multilingual Assistant)

A Retrieval-Augmented Generation (RAG) based chatbot designed to answer Machine Learning queries using web-sourced knowledge. The system supports multiple languages and provides intelligent, context-aware responses through an integrated LLM pipeline.

---

📌 Overview

This project combines **information retrieval** and **large language models (LLMs)** to deliver accurate and explainable answers. It leverages a curated Machine Learning knowledge source and enables users to interact through a clean Streamlit interface.

---

✨ Key Features

- 🔍 Retrieval-Augmented Generation (RAG)
- 🌐 Multilingual Support:
  - English
  - Hindi
  - Marathi
  - Sanskrit (experimental)
- 🧠 Context-aware responses using LLM
- ⚡ Fast inference using Groq API
- 📊 Vector search using FAISS
- 💬 Interactive chat UI using Streamlit

---

🛠️ Tech Stack

| Component           | Technology Used       |
|---------------------|-----------------------|
| Frontend UI         | Streamlit             |
| Backend Logic       | Python                |
| Vector Database     | FAISS                 |
| Embeddings          | Sentence Transformers |
| LLM API             | Groq                  |
| Framework           | LangChain             |
| Translation         | Deep Translator       |

---

⚙️ Installation & Setup

1. Clone the Repository
git clone https://github.com/Dhanshri1705/ML_Chatbot.git

cd ML_Chatbot

3. Create Virtual Environment
python -m venv venv
venv\Scripts\activate   # For Windows

4. Install Dependencies
pip install -r requirements.txt

5. Run the Application
streamlit run app.py


🔑 API Configuration
This project uses the Groq API for generating responses from the LLM.

⚠️ **Important Note:**
For ease of development and testing, the API key is currently **hardcoded in the source code**.

🔒 Security Recommendation
It is strongly recommended to **avoid hardcoding API keys** in production environments.

Instead, use environment variables:
GROQ_API_KEY=your_api_key_here
