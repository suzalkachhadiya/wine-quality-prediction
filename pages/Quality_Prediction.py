import streamlit as st
import numpy as np
from mlproject.pipeline.prediction import PredictionPipeline

# Set Streamlit page configuration
st.set_page_config(
    page_title="Wine Quality",
    page_icon="🧑‍⚕️",
    layout="wide")

st.header("**Wine Quality Predictor**",divider="green") # bold

with st.form("pred_form",clear_on_submit=True, border=True):
    fixed_acidity = st.number_input("fixed acidity",value=None)
    volatile_acidity = float(st.number_input("volatile acidity",value=None))
    citric_acid = float(st.number_input("citric acid",value=None))
    residual_sugar =float(st.number_input("residual sugar",value=None))
    chlorides =float(st.number_input("chlorides",value=None))
    free_sulfur_dioxide =float(st.number_input("free sulfur dioxide",value=None))
    total_sulfur_dioxide =float(st.number_input("total sulfur dioxide",value=None))
    density =float(st.number_input("density",value=None))
    pH =float(st.number_input("pH",value=None))
    sulphates =float(st.number_input("sulphates",value=None))
    alcohol =float(st.number_input("alcohol",value=None))
    submitted = float(st.form_submit_button("Submit"))

if submitted:
    data=[
        float(fixed_acidity),
        volatile_acidity,
        citric_acid,
        residual_sugar,
        chlorides,
        free_sulfur_dioxide,
        density,
        pH,
        sulphates,
        alcohol
    ]
    data = np.array(data).reshape(1,10)

    obj = PredictionPipeline()
    predicted_value = obj.predict(data)

    st.header(f"**{predicted_value}**")