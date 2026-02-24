# import streamlit as st
# import json
# import pandas as pd
# from llm import generate_text
# from image_gen import generate_image

# # ─── Constants ───────────────────────────────────────────────────────────────
# INSURANCE_TYPES = [
#     "Life Insurance", "Health Insurance", "Auto Insurance", "Home Insurance",
#     "Cyber Insurance", "Travel Insurance", "Business Insurance", "Pet Insurance"
# ]

# VISUAL_STYLES = [
#     "Risk Infographic", "Coverage Map", "Claims Flow", "Risk Pyramid", "Comparison Chart"
# ]

# # ─── Session state ───────────────────────────────────────────────────────────
# if "history" not in st.session_state:
#     st.session_state.history = []

# st.set_page_config(
#     page_title="Insurance Concept Generator",
#     page_icon="🛡️",
#     layout="wide"
# )

# # ─── Main UI ─────────────────────────────────────────────────────────────────
# st.title("🛡️ Insurance Concept Generator")
# st.markdown("Generate simple explanations, risk charts and AI-generated infographics")

# # Input fields
# col1, col2 = st.columns([3, 2])
# with col1:
#     insurance_type = st.selectbox("Insurance Type", [""] + INSURANCE_TYPES)
# with col2:
#     visual_style = st.selectbox("Visual Style", [""] + VISUAL_STYLES)

# context = st.text_area(
#     "Optional context / target audience",
#     placeholder="e.g. young families, small business owners, people in flood areas...",
#     height=100
# )

# generate_button = st.button("Generate Concept", type="primary", use_container_width=True)

# if generate_button:

#     if not insurance_type:
#         st.error("Please select an insurance type.")
#         st.stop()

#     with st.spinner("Generating insurance concept..."):

#         # Build base description
#         base = insurance_type
#         if visual_style:
#             base += f" – {visual_style} style"
#         if context.strip():
#             base += f". Context: {context.strip()}"

#         # 1. Narrative explanation
#         narrative_prompt = f"""
# Explain {base} in very simple language for normal people.
# Use these exact headings:

# **Overview**
# **Main Risks**
# **What is Covered**
# **Who Usually Needs It**
# **Important Tips**
# """
#         try:
#             narrative = generate_text(narrative_prompt)
#         except Exception as e:
#             narrative = f"Error calling Gemini:\n{str(e)}"

#         # 2. Image generation prompt (used both for Gemini + directly for HF)
#         img_prompt_text = f"""
# Create a detailed, high-quality prompt for FLUX.1 or Stable Diffusion XL that generates a professional insurance infographic about {base}.
# Include: clean layout, icons, charts, risk bars or pie charts, blue-white corporate colors, modern minimalist style.
# Return **only the final prompt text** — no explanations, no markdown.
# """
#         try:
#             image_prompt = generate_text(img_prompt_text).strip()
#         except:
#             image_prompt = (
#                 f"Professional clean infographic about {insurance_type} insurance, "
#                 f"{visual_style or 'overview'}, blue and white corporate style, "
#                 "icons, charts, percentages, modern design, high resolution"
#             )

#         # 3. Risk data (for bar chart)
#         risk_prompt = f"""
# Return **only valid JSON**, nothing else. Example:

# {{
#   "risks": [
#     ["Accident", 8, "High chance of injury"],
#     ["Theft", 6, "Moderate risk of loss"],
#     ...
#   ]
# }}

# Create 4-6 realistic risks for {insurance_type} insurance.
# """
#         try:
#             raw_json = generate_text(risk_prompt)
#             cleaned = raw_json.strip().replace("```json", "").replace("```", "").strip()
#             risk_data = json.loads(cleaned)
#         except:
#             risk_data = {"risks": []}

#         # 4. Generate image (now using the working HF setup)
#         generated_image = None
#         try:
#             # Use the Gemini-generated prompt or fallback
#             final_img_prompt = image_prompt if image_prompt else (
#                 f"Clean professional infographic explaining {insurance_type} insurance, "
#                 f"{visual_style or 'concept'}, charts, icons, blue tones, corporate style"
#             )
#             print(f"[App] Calling image_gen with prompt: {final_img_prompt[:80]}...")
#             generated_image = generate_image(final_img_prompt)
#             if generated_image:
#                 print("[App] Image generated successfully")
#             else:
#                 print("[App] generate_image returned None")
#         except Exception as e:
#             print(f"[App] Image generation exception: {str(e)}")
#             st.info(f"Image generation skipped: {str(e)}")

#         # Save to history
#         st.session_state.history.append({
#             "type": insurance_type,
#             "style": visual_style or "Default",
#             "context": context.strip(),
#             "narrative": narrative,
#             "image_prompt": image_prompt,
#             "risk_data": risk_data,
#             "image": generated_image
#         })

#     # ── Results ────────────────────────────────────────────────────────────────
#     tab_narr, tab_risk, tab_prompt, tab_img = st.tabs([
#         "📝 Explanation",
#         "📊 Risk Overview",
#         "🎨 Image Prompt",
#         "🖼️  AI Image"
#     ])

#     with tab_narr:
#         st.markdown(narrative if narrative else "No narrative generated.")

#     with tab_risk:
#         if risk_data.get("risks"):
#             df = pd.DataFrame(risk_data["risks"], columns=["Risk", "Level (1-10)", "Description"])
#             st.bar_chart(df.set_index("Risk")["Level (1-10)"], height=320)
#             st.dataframe(df, hide_index=True)
#         else:
#             st.info("No risk data generated this time.")

#     with tab_prompt:
#         st.text_area(
#             "Image generation prompt (you can copy & use in other tools)",
#             image_prompt,
#             height=140
#         )

#     with tab_img:
#         if generated_image is not None:
#             st.image(generated_image, use_column_width=True,
#                      caption=f"{insurance_type} — {visual_style or 'Generated Concept'}")
#         else:
#             st.info("No image was generated.\nCheck the terminal for debug messages.")

# # ─── History ────────────────────────────────────────────────────────────────
# if st.session_state.history:
#     with st.expander(f"Previous generations ({len(st.session_state.history)})"):
#         for entry in reversed(st.session_state.history[-6:]):
#             label = f"{entry['type']} • {entry['style']}"
#             if entry['context']:
#                 label += f" • {entry['context'][:35]}{'...' if len(entry['context'])>35 else ''}"
#             st.markdown(f"**{label}**")
#             if entry.get("image"):
#                 st.image(entry["image"], width=240)
#             st.markdown("---")

# app.py
# app.py
import streamlit as st
from styles import apply_carbon_theme

apply_carbon_theme()

# Shared session state
if "page" not in st.session_state:
    st.session_state.page = "home"

if "history" not in st.session_state:
    st.session_state.history = []

if "chat_messages" not in st.session_state:
    st.session_state.chat_messages = [
        {"role": "assistant", "content": "Hi! I'm your insurance expert. How can I help you today?"}
    ]

if "detail_item" not in st.session_state:
    st.session_state.detail_item = None

# Set page config to control sidebar
st.set_page_config(
    page_title="InsuranceAI",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"  # Keeps sidebar open but no native duplicates since no 'pages/' folder
)

# Sidebar navigation
st.sidebar.title("Multimodal Insurance AI")

nav_items = [
    ("🏠 Home", "home"),
    ("◈ Creator Studio", "studio"),
    ("◉ AI Expert Chat", "chat"),
    ("⊟ History", "history"),
    ("▦ Gallery", "gallery"),
]

for label, page_key in nav_items:
    is_active = st.session_state.page == page_key
    btn_type = "primary" if is_active else "secondary"
    if st.sidebar.button(label, use_container_width=True, type=btn_type, key=f"nav_{page_key}"):
        st.session_state.page = page_key
        st.rerun()

# Route to current page
try:
    page_module = __import__(f"my_pages.{st.session_state.page}", fromlist=[""])
    page_module.render()
except ImportError as e:
    st.error(f"Page not found: {st.session_state.page}. Error: {e}")