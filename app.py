
import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("healthcare_risk_model.pkl")

# Page settings
st.set_page_config(
    page_title="Healthcare Risk Prediction",
    page_icon="🏥",
    layout="centered"
)

# Application title
st.title("🏥 Healthcare Risk Prediction System")
st.write("Enter the details below to predict the health risk category.")

# Patient information
st.subheader("Patient Information")

disease = st.selectbox(
    "Select Disease",
    ["Asthma", "Diabetes", "Hypertension", "Migraine",
     "Stroke", "Pneumonia", "Influenza", "Bronchitis",
     "Osteoporosis", "Hyperthyroidism", "Other"]
)

age = st.number_input("Enter Age", min_value=19, max_value=90, value=25)

gender = st.selectbox("Select Gender", ["female", "male"])

st.subheader("Symptoms")

fever = st.selectbox("Fever", ["Yes", "No"])
cough = st.selectbox("Cough", ["Yes", "No"])
fatigue = st.selectbox("Fatigue", ["Yes", "No"])
difficulty_breathing = st.selectbox(
    "Difficulty Breathing", ["Yes", "No"]
)

st.subheader("Health Information")

blood_pressure = st.selectbox("Blood Pressure Category", [0, 1, 2])
cholesterol_level = st.selectbox("Cholesterol Category", [0, 1, 2])

# Prediction
if st.button("Predict Risk Level"):

    input_data = pd.DataFrame([{
        "disease": disease,
        "fever": fever,
        "cough": cough,
        "fatigue": fatigue,
        "difficulty_breathing": difficulty_breathing,
        "age": age,
        "gender": gender,
        "blood_pressure": blood_pressure,
        "cholesterol_level": cholesterol_level
    }])

    prediction = model.predict(input_data)[0]

    st.subheader("Prediction Result")
    st.success(f"Predicted Risk Level: {prediction}")

    st.warning(
        "Educational project only. This prediction is not a medical "
        "diagnosis or a basis for treatment. Consult a qualified "
        "healthcare professional."
    )
