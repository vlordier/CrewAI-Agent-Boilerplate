"""ChatGPT-like Clone UI.

This module creates a simple web-based UI for interacting with a ChatGPT-like model using Streamlit and OpenAI API, employing an object-oriented approach.
"""

import logging
import os

import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI, OpenAIError

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

# Load environment variables
load_dotenv()

st.title("CrewAI UI")
st.subheader("A simple ChatGPT-like interface using OpenAI API and Streamlit.")

try:
    api_key = os.getenv("OPENAI_API_KEY")
    if api_key is None:
        raise ValueError(
            "API key not found. Ensure the .env file is configured correctly."
        )

    client = OpenAI(api_key=api_key)

    if "openai_model" not in st.session_state:
        openai_model = os.getenv("OPENAI_MODEL_NAME")
        if openai_model is None:
            raise ValueError(
                "Model identifier not found. Check your .env configuration."
            )
        st.session_state["openai_model"] = openai_model

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("What is up?"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            try:
                stream = client.chat.completions.create(
                    model=st.session_state["openai_model"],
                    messages=[
                        {"role": m["role"], "content": m["content"]}
                        for m in st.session_state.messages
                    ],
                    stream=True,
                )
                response = st.write_stream(stream)
            except OpenAIError as e:
                st.error(f"Failed to retrieve response: {e}")
                logging.error(f"API Error: {e}")
            except Exception as e:
                st.error(f"An unexpected error occurred: {e}")
                logging.exception("Unexpected error")
            else:
                st.session_state.messages.append(
                    {"role": "assistant", "content": response}
                )
except Exception as e:
    st.error(f"An error occurred during setup: {e}")
    logging.exception("Setup error")
