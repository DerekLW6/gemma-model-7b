import streamlit as st
import requests

LOGGER = st.logger

def generate_text(prompt, max_length=500, num_return_sequences=3, temperature=0.7):
    url = "https://api-inference.huggingface.co/models/google/gemma-7b"
    headers = {"Authorization": f"Bearer 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"}  # Replace YOUR_API_TOKEN with your actual API token
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
        page_title="Text Generation with Hugging Face",
        page_icon="🤖",
    )

    st.write("# Text Generation with Hugging Face Model 🤖")

    st.sidebar.info("Enter your prompt on the left and click 'Generate'.")

    prompt = st.text_input("Enter your prompt:", "How to train a machine learning model?")

    if st.button("Generate"):
        generated_texts = generate_text(prompt)
        if generated_texts is not None:
            for i, text in enumerate(generated_texts):
                st.write(f"Generated text {i+1}: {text}")

if __name__ == "__main__":
    run()
