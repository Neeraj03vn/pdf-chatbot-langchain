# 📄 LangChain PDF Chatbot

A lightweight chatbot built with **LangChain**, **Streamlit**, and **HuggingFace**, designed to answer questions from uploaded PDF documents.

## 🚀 Features

- 📚 Upload any PDF and ask questions based on its content.
- 🧠 Powered by local HuggingFace models (FLAN-T5).
- 🛠️ Built-in calculator tool (`calc: expression`).
- 💬 Memory-enabled conversations using LangChain agents.
- 🔌 No OpenAI required — completely local and open-source!

## 🧩 Tech Stack

- Python, Streamlit
- HuggingFace Transformers
- LangChain (tools, memory, retrieval)
- FAISS (for vector store)
- Sentence Transformers (`all-MiniLM-L6-v2`)

## 🛠️ Setup Instructions

```bash
# Clone the repository
git clone https://github.com/Neeraj03vn/pdf-chatbot-langchain.git
cd your_folder

# Install dependencies
pip install -r requirements.txt

# Download and save the model locally
python model.py

# Run the Streamlit app
streamlit run app.py
