import streamlit as st
import requests

API_URL = "https://customer-churn-prediction-gnnf.onrender.com/"

st.set_page_config(page_title="Customer Churn Predictor", layout="centered")
st.title("📉 Customer Churn Prediction")

st.markdown("Enter customer details below:")


age = st.number_input("Age", min_value=0, max_value=100, value=30)
region = st.selectbox("Region", ["Asia", "Europe", "Africa"])
watch_hours = st.number_input("Monthly Watch Hours", min_value=0.0, value=5.0)
subscription_type = st.selectbox("Subscription Type", ["Basic", "Standard", "Premium"])
number_of_profiles = st.slider("Number of Profiles", 1, 5, 1)

threshold = st.sidebar.slider("Decision Threshold", 0.1, 0.9, 0.39)
st.sidebar.info("Lower threshold → higher sensitivity → more customers flagged" )
st.sidebar.info("Higher threshold → higher confidence → fewer customers flagged")
st.write(f"Selected Threshold {threshold}")
payload = {
    "age": age,
    "region": region,
    "watch_hours": watch_hours,
    "subscription_type": subscription_type,
    "number_of_profiles": number_of_profiles,
    "gender": "Other",
    "device": "Tablet",
    "payment_method": "Debit Card",
    "favorite_genre": "Documentary"
}


if st.button("Predict Churn"):
    with st.spinner("Predicting..."):
        response = requests.post(
            API_URL,
            params={"threshold": threshold},
            json=payload
        )

    if response.status_code == 200:
        result = response.json()

        st.subheader("📊 Prediction Result")

        st.metric("Churn Probability", f"{result['churn_probability']:.2f}%")
        st.metric("Risk Level", result["risk_level"])

        st.subheader("⚠️ Risk Indicators")
        for r in result["risk_indicators"]:
            st.write("•", r)

        st.subheader("✅ Recommended Actions")
        for a in result["recommended_actions"]:
            st.write("•", a)

    else:

        st.error("API Error. Please check backend.")
