import streamlit as st

st.title("Wine Quality Prediction")

# st.write('''
# # Welcome to the Wine Quality Prediction App!

# This app predicts the quality of wines based on their physicochemical properties.
# ''')

# st.header('Prediction Form')
# fixed_acidity = st.text_input('Enter fixed acidity:') 
# volatile_acidity = st.text_input('Enter volatile acidity:')
# citric_acid = st.text_input('Enter citric_acid:')  
# residual_sugar = st.text_input('Enter residual sugzr:')
# chlorides = st.text_input('Enter chlorides:')
# free_sulfur_dioxide=st.text_input("Enter free sulfur dioxide")
# total_sulfur_dioxide = st.text_input('Enter total sulfur dioxide:')
# density=st.text_input('Enter density:')
# pH= st.text_input('Enter pH:')
# sulphates= st.text_input('Enter sulphates:')
# alcohol= st.text_input('Enter alcohol:')


# Create a dictionary of page names to module paths
pages = {
    "Model Train": "pages/home.py", 
    "Quality Prediction": "pages/model_training.py"
}

# Radio button to select page
page = st.radio("Select a page", list(pages.keys()))

# Render selected page
if page:
    with st.spinner(f"Loading {page} ..."):
        exec(open(pages[page]).read())