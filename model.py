# model.py
# Helper script to download and save HuggingFace model locally

from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
import os


def download_model(model_name: str = "google/flan-t5-base", save_dir: str = "./hf_model"):
    print(f"Downloading model '{model_name}'...")
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

    tokenizer.save_pretrained(save_dir)
    model.save_pretrained(save_dir)
    print(f"✅ Model saved locally at '{save_dir}'")


if __name__ == "__main__":
    download_model()
