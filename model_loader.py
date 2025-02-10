import joblib
import numpy as np

# Load the trained model from the pickle file
model = joblib.load("air_quality_model.pkl")

# Define a function for prediction
def predict_air_quality(features):
    features = np.array(features).reshape(1, -1)
    prediction = model.predict(features)[0]
    
    air_quality_labels = {0: "Good", 1: "Hazardous", 2: "Moderate", 3: "Poor"}
    return air_quality_labels[prediction]
