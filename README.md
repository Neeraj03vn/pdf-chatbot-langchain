# AI PDF Chatbot with LangChain & HuggingFace

An **AI-powered chatbot** that can read and understand PDF files, allowing you to ask natural language questions and get accurate answers instantly.  
The system uses **Retrieval-Augmented Generation (RAG)** with **LangChain**, **HuggingFace FLAN-T5**, and **FAISS** for semantic search.

---

## Features
- **PDF Question Answering** – Upload any PDF and ask questions directly.
- **RAG Pipeline** – Retrieves relevant PDF content before generating answers.
- **Math Support** – Includes a calculator tool for solving math problems (`calc: expression`).
- **Fast Retrieval** – Uses **FAISS** for efficient similarity search.
- **Conversational Memory** – Remembers previous chat context for follow-up questions.
- **User-Friendly UI** – Streamlit interface for easy interaction.

---

## Tech Stack
- **Programming Language:** Python
- **Frameworks & Libraries:**
  - [LangChain](https://www.langchain.com/) – RAG pipeline, memory management
  - [HuggingFace Transformers](https://huggingface.co/) – FLAN-T5 language model
  - [FAISS](https://faiss.ai/) – Vector database for semantic search
  - [Streamlit](https://streamlit.io/) – Web interface
  - [PyPDFLoader](https://python.langchain.com/docs/modules/data_connection/document_loaders/) – PDF parsing
  - RecursiveCharacterTextSplitter – Splitting PDF text into chunks

---

## Project Structure
```plaintext
.
├── app.py                 # Streamlit app – handles PDF upload & chat interface
├── agent_build.py         # Builds the LangChain agent with tools
├── llm_loader.py          # Loads HuggingFace FLAN-T5 model
├── pdf.py                 # Extracts text from PDF and creates FAISS vector store
├── tools.py               # Calculator and other utility tools
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation

## **How It Works**
- **Upload PDF** → Extracts text using PyPDFLoader.
- **Split & Embed** → Text is split into chunks and converted into embeddings (HuggingFaceEmbeddings).
- **Store in FAISS** → Embeddings are stored for fast retrieval.
-** User Question** → System retrieves top relevant chunks.
-** Generate Answer** → Chunks + question sent to HuggingFace FLAN-T5 model.
- **Respond in UI** → Displayed in Streamlit chat interface.

## Installation & Usage
1. **Clone the repository** :
  - git clone https://github.com/your-username/ai-pdf-chatbot.git
  - cd ai-pdf-chatbot
2. **Install dependencies**
  - pip install -r requirements.txt
3️. **Run the Streamlit app**
  - streamlit run app.py

## Example Usage
1. Ask about a research paper:
  - "Summarize the introduction section"

2. Do math calculations:
  - "calc: 15 * 12 + 30"
