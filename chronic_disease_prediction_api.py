import os
import requests

# Retrieve API keys from environment variables
rapidapi_key = os.getenv('RAPIDAPI_KEY')
rapidapi_host = os.getenv('RAPIDAPI_HOST')

# API URLs
heart_disease_api_url = "https://example-heart-disease-api.p.rapidapi.com/predict"
diabetes_api_url = "https://example-diabetes-api.p.rapidapi.com/predict"

# Headers for API Authentication
headers = {
    'x-rapidapi-host': rapidapi_host,
    'x-rapidapi-key': rapidapi_key
}

# Sample data for prediction
patient_data = {
    "age": 45,
    "sex": "male",
    "cholesterol": 230,
    "blood_pressure": 130,
    "glucose_level": 120,
    "family_history": "yes",
}

# Function to predict heart disease
def predict_heart_disease(patient_data):
    response = requests.post(heart_disease_api_url, json=patient_data, headers=headers)
    if response.status_code == 200:
        return response.json()
    return None

# Function to predict diabetes
def predict_diabetes(patient_data):
    response = requests.post(diabetes_api_url, json=patient_data, headers=headers)
    if response.status_code == 200:
        return response.json()
    return None

# Call the prediction functions
heart_disease_prediction = predict_heart_disease(patient_data)
diabetes_prediction = predict_diabetes(patient_data)

# Output results
if heart_disease_prediction:
    print("Heart Disease Prediction:", heart_disease_prediction)

if diabetes_prediction:
    print("Diabetes Prediction:", diabetes_prediction)
