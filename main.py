from langchainPalm2Bot import myGpt
import time
import streamlit as st

with st.sidebar:
    google_palm2_key = st.text_input("Google Palm-2 Key", key="chatbot_api_key", type="password")
    "[Get an Google Palm-2 key](https://developers.generativeai.google/)"
    "[![Source Code](https://github.com/codespaces/badge.svg)](https://codespaces.new/streamlit/llm-examples?quickstart=1)"

st.title("Prime's Lil GPT")
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    if not google_palm2_key:
        st.info("Please add your Google Palm-2 key to continue.")
        st.stop()

    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    with st.spinner('Thinking...'):
        msg = myGpt(prompt, google_palm2_key)
        msg = {"role": "assistant", "content": msg}
        st.session_state.messages.append(msg)
        st.chat_message("assistant").write(msg["content"])