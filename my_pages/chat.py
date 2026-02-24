# my_pages/chat.py
import streamlit as st
from llm import generate_text

def render():
    st.header("AI Expert Chat")
    st.markdown("Ask anything about insurance policies, coverage, claims, premiums, or specific scenarios.")

    # Chat container
    chat_container = st.container()

    # Display messages
    with chat_container:
        for msg in st.session_state.chat_messages:
            role = msg["role"]
            avatar = "🤖" if role == "assistant" else "👤"
            with st.chat_message(role, avatar=avatar):
                st.markdown(msg["content"])

    # Input
    prompt = st.chat_input("Ask your question...")

    if prompt:
        st.session_state.chat_messages.append({"role": "user", "content": prompt})
        with chat_container:
            with st.chat_message("user"):
                st.markdown(prompt)

        with st.spinner("Thinking..."):
            full_prompt = f"You are an insurance expert. Answer clearly.\nUser: {prompt}"
            response = generate_text(full_prompt)

        st.session_state.chat_messages.append({"role": "assistant", "content": response})
        with chat_container:
            with st.chat_message("assistant"):
                st.markdown(response)

        st.rerun()