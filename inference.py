import os
from openai import OpenAI

hf_token = os.getenv("HF_TOKEN")

client = OpenAI(
    api_key=hf_token, 
    base_url="https://api-inference.huggingface.co/v1/"
)

def run_inference():
    print("Starting inference loop...")
    if not hf_token:
        print("Please set your HF_TOKEN")
        return
    print("Environment validated! Using HF Router.")

if __name__ == "__main__":
    run_inference()
