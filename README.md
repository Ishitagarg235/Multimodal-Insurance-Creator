🛡️ Multimodal Insurance Creator

This project generates simple insurance explanations using AI and displays them through a Streamlit web interface.

🔧 Requirements

Make sure the following are installed:

Python 3.10 or above

Internet connection

A free Gemini API key

A free Hugging Face API key

📦 Project Dependencies

Install dependencies using requirements.txt:

streamlit
google-genai
huggingface-hub
python-dotenv
Pillow

📁 Project Structure
multimodal-insurance-streamlit/
│
├── app.py
├── llm.py
├── image_gen.py
├── test_llm.py
├── requirements.txt
└── .env

🔑 API Key Setup

Create a file named .env in the project root directory and add:

GEMINI_API_KEY=your_gemini_api_key_here
HF_API_KEY=your_huggingface_api_key_here


⚠️ Do not share this file.

🚀 How to Run the Project
Step 1: Open Project Folder

Open the project folder in VS Code.

Step 2: Open Terminal in VS Code

Use:

Ctrl + `


Make sure terminal path is inside the project folder.

Step 3: (Optional) Create Virtual Environment
python -m venv venv
venv\Scripts\activate

Step 4: Install Required Packages
pip install -r requirements.txt

Step 5: Test Gemini Text Generation

Run this to confirm Gemini is working:

python test_llm.py


If text output appears, Gemini is configured correctly.

Step 6: Run the Streamlit Application
streamlit run app.py


A browser window will open automatically.

✅ How to Use the App

Enter an insurance topic (example: health insurance)

Click Generate

View:

AI-generated text explanation

AI-generated visual infographic

🛑 Common Errors & Fixes
Issue	            Solution
API key error	    Check .env file
Infinite loading	Test test_llm.py
Module not found	Reinstall requirements.txt


Image not shown	Check Hugging Face API key