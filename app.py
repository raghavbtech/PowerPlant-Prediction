import streamlit as st
import numpy as np
import pickle

# Page config
st.set_page_config(page_title="Power Plant Prediction", layout="centered")

# Load trained model
model = pickle.load(open("power_model.pkl", "rb"))

# Custom font styling
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');

        html, body, [class*="css"] {
            font-family: 'Inter', sans-serif;
        }
        h1 {
            font-size: 2.2rem;
            font-weight: 700;
        }
        .stNumberInput label {
            font-size: 1rem;
            font-weight: 600;
        }
        .stButton > button {
            font-size: 1rem;
            font-weight: 600;
            padding: 0.5rem 2rem;
            border-radius: 8px;
        }
    </style>
""", unsafe_allow_html=True)

# Page title
st.title("⚡ Power Plant Energy Output Prediction")

st.write(
    "Predict the **Power Output (PE)** of a Combined Cycle Power Plant "
    "based on environmental conditions."
)

st.divider()

# Main page inputs
st.subheader("Enter Input Values")

col1, col2 = st.columns(2)

with col1:
    AT = st.number_input("Ambient Temperature (AT) °C", min_value=1.0, max_value=40.0, value=20.0, step=0.1)
    AP = st.number_input("Ambient Pressure (AP) mbar", min_value=990.0, max_value=1040.0, value=1010.0, step=0.1)

with col2:
    V = st.number_input("Exhaust Vacuum (V) cmHg", min_value=25.0, max_value=85.0, value=50.0, step=0.1)
    RH = st.number_input("Relative Humidity (RH) %", min_value=10.0, max_value=100.0, value=60.0, step=0.1)

st.write("")

# Prediction button
if st.button("Predict Power Output", use_container_width=True):
    features = np.array([[AT, V, AP, RH]])
    prediction = model.predict(features)
    st.success(f"Predicted Power Output: **{prediction[0]:.2f} MW**")

# Footer
st.divider()
st.caption("Developed by Raghav Chugh | Machine Learning Project")
