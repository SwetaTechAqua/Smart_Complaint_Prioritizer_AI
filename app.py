import streamlit as st
from ui.complaint_ui import complaint_ui
from pathlib import Path

# Page setup
st.set_page_config(page_title="Smart Complaint Prioritizer", layout="wide")

# Load external CSS from style file
with open("assets/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# App title and intro
st.markdown("""
    <h1 class='title'>⚡ Smart Complaint Prioritizer</h1>
    <p class='subtitle'>An AI-powered dashboard to intelligently auto-classify and prioritize utility complaints faster.</p>
""", unsafe_allow_html=True)

# Run UI
complaint_ui()
