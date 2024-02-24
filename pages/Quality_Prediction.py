import streamlit as st
import numpy as np
from mlproject.pipeline.prediction import PredictionPipeline

# Set Streamlit page configuration
# st.set_page_config(
#     page_title="Wine Quality",
#     page_icon="🧑‍⚕️",
#     layout="wide")

st.header("**Wine Quality Predictor**",divider="green") # bold

with st.form("pred_form",clear_on_submit=True, border=True):
    fixed_acidity = st.number_input("fixed acidity",value=None)
    volatile_acidity = st.number_input("volatile acidity",value=None)
    citric_acid = st.number_input("citric acid",value=None)
    residual_sugar =st.number_input("residual sugar",value=None)
    chlorides =st.number_input("chlorides",value=None)
    free_sulfur_dioxide =st.number_input("free sulfur dioxide",value=None)
    total_sulfur_dioxide =st.number_input("total sulfur dioxide",value=None)
    density =st.number_input("density",value=None)
    pH =st.number_input("pH",value=None)
    sulphates =st.number_input("sulphates",value=None)
    alcohol =st.number_input("alcohol",value=None)
    submitted = st.form_submit_button("Submit")

if submitted:
    data=[
        float(fixed_acidity),
        float(volatile_acidity),
        float(citric_acid),
        float(residual_sugar),
        float(chlorides),
        float(free_sulfur_dioxide),
        float(total_sulfur_dioxide),
        float(density),
        float(pH),
        float(sulphates),
        float(alcohol)
    ]
    data = np.array(data).reshape(1,11)

    obj = PredictionPipeline()
    predicted_value = obj.predict(data)

    st.header(f"The Quality of wine:**{predicted_value}**")     