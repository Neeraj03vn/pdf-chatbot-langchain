# llm_loader.py
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline
from langchain_community.llms import HuggingFacePipeline
import streamlit as st

@st.cache_resource
def load_llm(model_path="./hf_model"):
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_path)
    pipe = pipeline("text2text-generation", model=model, tokenizer=tokenizer, max_length=512)
    return HuggingFacePipeline(pipeline=pipe)
