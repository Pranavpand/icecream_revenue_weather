import streamlit as st
import pandas as pd
from utils import load_model, preprocess_input

st.title("🍦 Ice Cream Revenue Prediction Based on Weather")

model = load_model("model.pkl")

temp = st.slider("Temperature (°C)", 0, 50, 25)
humidity = st.slider("Humidity (%)", 0, 100, 50)
wind_speed = st.slider("Wind Speed (km/h)", 0, 50, 10)
is_weekend = st.selectbox("Is it a Weekend?", ["No", "Yes"])

if st.button("Predict Revenue"):
    data = preprocess_input(temp, humidity, wind_speed, is_weekend)
    prediction = model.predict(data)[0]
    st.success(f"Predicted Ice Cream Revenue: ₹{prediction:.2f}")
