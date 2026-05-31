import streamlit as st
import pandas as pd
import joblib

st.title(
    "Demand Forecast Dashboard"
)

model = joblib.load(
    "demand_forecast.pkl"
)

st.write(
    "AI Demand Prediction System"
)

# Assuming you want to run the streamlit app
# If you run this cell, it will save app.py and then try to run streamlit
# You might need to install streamlit-nightly if you face issues with running it directly in Colab

# To run the Streamlit app, you would typically execute the following in a new cell:
# !streamlit run app.py
