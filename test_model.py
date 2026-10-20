import joblib
import pandas as pd

# Load the saved model
model = joblib.load("heart_disease_model.pkl")

print("Model loaded successfully!")

# Create one example patient
patient = pd.DataFrame([{
    "age": 55,
    "sex": 1,
    "cp": 2,
    "trestbps": 140,
    "chol": 240,
    "fbs": 0,
    "restecg": 1,
    "thalach": 150,
    "exang": 0,
    "oldpeak": 1.0,
    "slope": 2,
    "ca": 0,
    "thal": 2
}])

# Make prediction
prediction = model.predict(patient)

print("\nPrediction:")

if prediction[0] == 1:
    print("Heart disease predicted")
else:
    print("No heart disease predicted")