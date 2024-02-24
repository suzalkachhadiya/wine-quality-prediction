import streamlit as st
import importlib


st.set_page_config(page_title="Wine Quality", page_icon="🍷")
st.title("Wine Quality Prediction")

# Create a dictionary of page names to module paths
pages = {
    "Model Train": "pages.quality_prediction.py", 
    "Quality Prediction": "pages.model_training.py"
}

# Radio button to select page
page = st.radio("Select a page", list(pages.keys()))

st.write("suzalkachhadiya111@gmail.com")

# Render selected page
# if page:
#     with st.spinner(f"Loading {page} ..."):
#         # exec(open(pages[page]).read())
#         with open('file.py', encoding='utf-8') as f:
#             code = f.read()
#             exec(code)