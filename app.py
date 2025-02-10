import streamlit as st
import numpy as np
import joblib
from model_loader import predict_air_quality  

# Correct mean and std values from training data
feature_stats = {
    "🌡️ Temperature (°C)": {"mean": 30.029020, "std": 6.720661},
    "💧 Humidity (%)": {"mean": 70.056120, "std": 15.863577},
    "🫁 PM2.5 (µg/m³)": {"mean": 20.142140, "std": 24.554546},
    "🌫️ PM10 (µg/m³)": {"mean": 30.218360, "std": 27.349199},
    "🌪️ NO₂ (ppm)": {"mean": 26.412100, "std": 8.895356},
    "☠️ SO₂ (ppm)": {"mean": 10.014820, "std": 6.750303},
    "🚗 CO (ppm)": {"mean": 1.500354, "std": 0.546027},
    "🏭 Proximity to Industrial Areas": {"mean": 8.425400, "std": 3.610944},
    "👥 Population Density (people/km²)": {"mean": 497.423800, "std": 152.754084}
}

st.title("🌍 Air Quality Level Prediction")

# User input fields
inputs = []
for feature, stats in feature_stats.items():
    value = st.number_input(f"Enter {feature}", value=stats["mean"])
    # Standardize input using computed mean & std
    standardized_value = (value - stats["mean"]) / stats["std"]
    inputs.append(standardized_value)

# Prediction
if st.button("🚀 Predict Air Quality"):
    prediction = predict_air_quality(inputs)
    st.subheader(f"🏷️ Predicted Air Quality: **{prediction}**")
