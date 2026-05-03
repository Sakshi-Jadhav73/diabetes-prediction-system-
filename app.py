import streamlit as st
import numpy as np
import pickle

# =========================
# Load Model & Scaler
# =========================
model = pickle.load(open("model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

# =========================
# Title
# =========================
st.title("🩺 Diabetes Prediction System")

st.write("Enter patient details below to predict diabetes:")

# =========================
# Input Fields (Same as Dataset Columns)
# =========================
preg = st.number_input("Pregnancies", min_value=0)
glucose = st.number_input("Glucose", min_value=0)
bp = st.number_input("Blood Pressure", min_value=0)
skin = st.number_input("Skin Thickness", min_value=0)
insulin = st.number_input("Insulin", min_value=0)
bmi = st.number_input("BMI", min_value=0.0)
dpf = st.number_input("Diabetes Pedigree Function", min_value=0.0)
age = st.number_input("Age", min_value=1)

# =========================
# Prediction Button
# =========================
if st.button("Predict"):

    # Convert input to array
    input_data = np.array([[preg, glucose, bp, skin, insulin, bmi, dpf, age]])

    # Scale data
    std_data = scaler.transform(input_data)

    # Prediction
    prediction = model.predict(std_data)

    # Result
    if prediction[0] == 0:
        st.success("✅ The person is NOT Diabetic")
    else:
        st.error("⚠️ The person is Diabetic")
