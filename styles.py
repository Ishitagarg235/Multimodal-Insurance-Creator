# styles.py
import streamlit as st

def apply_carbon_theme():
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@300;400;500;600&family=IBM+Plex+Mono&display=swap');

        :root {
            --ibm-blue: #0f62fe;
            --ibm-gray-10: #f4f4f4;
            --ibm-gray-90: #161616;
            --ibm-text: #161616;
            --ibm-text-secondary: #525252;
        }

        html, body, [data-testid="stAppViewContainer"] {
            font-family: 'IBM Plex Sans', sans-serif;
            background: var(--ibm-gray-10);
        }

        h1, h2, h3 {
            color: var(--ibm-text);
        }

        .stSidebar {
            background: var(--ibm-gray-90) !important;
        }

        .stSidebar .sidebar-content {
            color: white !important;
        }

        .nav-button {
            width: 100% !important;
            margin: 6px 0 !important;
            text-align: left !important;
            font-weight: 500 !important;
        }

        .nav-active {
            background: var(--ibm-blue) !important;
            color: white !important;
        }

        .section-title {
            font-size: 1.1rem;
            font-weight: 600;
            margin: 1.5rem 0 0.8rem;
            color: var(--ibm-text);
        }
    </style>
    """, unsafe_allow_html=True)