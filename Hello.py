import streamlit as st
import requests
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)

def generate_text(prompt, max_length=13000, num_return_sequences=15, temperature=0.7):
    # url = "https://api-inference.huggingface.co/models/google/gemma-7b"
    # url = "https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.2"
    url =  "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2" # Updated URL

    headers = {"Authorization": f"Bearer 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"} 
    payload = {
        "inputs": prompt,
        "parameters": {
            "max_length": max_length,
            "num_return_sequences": num_return_sequences,
            "temperature": temperature
        }
    }

    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 200:
        generated_texts = [item['generated_text'] for item in response.json()]
        return generated_texts
    else:
        st.error(f"Error generating text: {response.text}")
        return None

def run():
    st.set_page_config(
        page_title="Streamlit App with Hugging Face",
        page_icon="👋",
    )

    st.write("# Hugging Face Free LLM 🤖")

    st.sidebar.info("Enter your prompt on the right and click 'Generate'.")

    prompt = st.text_input("Enter your prompt:", "Tell me about Duke University")

    if st.button("Generate"):
        generated_texts = generate_text(prompt)
        if generated_texts is not None:
            for i, text in enumerate(generated_texts):
                st.write(f"Generated text {i+1}: {text}")

if __name__ == "__main__":
    run()


