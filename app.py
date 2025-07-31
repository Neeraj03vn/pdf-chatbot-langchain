#app.py

import streamlit as st
from llm_loader import load_llm
from pdf import load_pdf_to_vectorstore
from agent_build import build_agent

st.set_page_config(page_title="LangChain PDF Chat", page_icon="📄", layout="wide")
st.title("📄 PDF Chatbot ")

if "vectorstore" not in st.session_state:
    st.session_state.vectorstore = None
if "qa_chain" not in st.session_state:
    st.session_state.qa_chain = None
if "agent" not in st.session_state:
    st.session_state.agent = None
if "messages" not in st.session_state:
    st.session_state.messages = []

llm = load_llm()

uploaded_pdf = st.file_uploader("Upload a PDF", type="pdf")

if uploaded_pdf is not None:
    pdf_path = "uploaded.pdf"
    with open(pdf_path, "wb") as f:
        f.write(uploaded_pdf.read())

    st.session_state.messages = []
    st.session_state.vectorstore = load_pdf_to_vectorstore(pdf_path)
    st.session_state.qa_chain, st.session_state.agent = build_agent(st.session_state.vectorstore, llm)
    st.success("✅ PDF uploaded and indexed!")

user_input = st.text_input("Ask a question ", key="input")

if user_input:
    if not st.session_state.vectorstore:
        st.warning("⚠️ Please upload a PDF first.")
    else:
        if user_input.strip().lower().startswith("calc:"):
            expression = user_input.replace("calc:", "").strip()
            response = st.session_state.agent.run(expression)
        else:
            response = st.session_state.qa_chain.run(user_input)

        st.session_state.messages.append(("user", user_input))
        st.session_state.messages.append(("bot", response))

for role, message in st.session_state.messages:
    st.markdown(f"**{'🧑 You' if role == 'user' else '🤖 Bot'}:** {message}")


