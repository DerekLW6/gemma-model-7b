import streamlit as st
import requests
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)

def generate_text(prompt, max_length=6000, num_return_sequences=8, temperature=0.7):
    url = "https://api-inference.huggingface.co/models/google/gemma-7b"
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


## Old Code
# st.markdown(
    #     """
    #     Streamlit is an open-source app framework built specifically for
    #     Machine Learning and Data Science projects.
    #     **👈 Select a demo from the sidebar** to see some examples
    #     of what Streamlit can do!
    #     ### Want to learn more?
    #     - Check out [streamlit.io](https://streamlit.io)
    #     - Jump into our [documentation](https://docs.streamlit.io)
    #     - Ask a question in our [community
    #       forums](https://discuss.streamlit.io)
    #     ### See more complex demos
    #     - Use a neural net to [analyze the Udacity Self-driving Car Image
    #       Dataset](https://github.com/streamlit/demo-self-driving)
    #     - Explore a [New York City rideshare dataset](https://github.com/streamlit/demo-uber-nyc-pickups)
    # """
    # )

        # st.write("# Welcome to Streamlit! 👋")

    # st.sidebar.success("Select a demo above.")