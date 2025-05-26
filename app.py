# app.py
!pip install streamlit
import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("best_model.pkl")

# Title
st.title("🌾 Crop Recommendation System")

# Input fields
N = st.number_input("Nitrogen", 0, 140)
P = st.number_input("Phosphorus", 5, 145)
K = st.number_input("Potassium", 5, 205)
temperature = st.number_input("Temperature (°C)", 8.0, 45.0)
humidity = st.number_input("Humidity (%)", 14.0, 100.0)
ph = st.number_input("pH", 3.5, 9.5)
rainfall = st.number_input("Rainfall (mm)", 20.0, 300.0)

# Predict button
if st.button("Recommend Crop"):
    input_data = [[N, P, K, temperature, humidity, ph, rainfall]]
    prediction = model.predict(input_data)
    st.success(f"✅ Recommended Crop: {prediction[0]}")