import streamlit as st
from google import genai

# Initialize client
client = genai.Client(api_key=st.secrets["GOOGLE_API_KEY"])

def generate_text(prompt):
    response = client.models.generate_content(
        model="gemini-2.5-flash",              
        contents=f"Explain this insurance topic in very simple language:\n{prompt}"
    )
    return response.text