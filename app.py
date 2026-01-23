import pandas as pd
import numpy as np
import streamlit as st
import pickle

 
@st.cache_resource
def load_model():
    with open("churn_model.pkl","rb") as f:
        return pickle.load(f)
    
artifacts=load_model()
model=artifacts["model"]
threshold=artifacts["threshold"]

st.title("Customer Churn prediction ")
@st._cache_data
def load_data():
    return pd.read_csv("data.csv")
df=load_data()

st.sidebar.header("Decision Settings")
threshold=st.sidebar.slider(
    "Select a threshold",
    min_value=0.10,
    max_value=0.90,
    value=float(threshold),
    step=0.01
)
st.sidebar.write(
    "Lower threshold - Catches more churners\n" 
    "\nHigher threshold - Fewer false alarms (Can miss some churners)"
)
st.write(f"Using threshold : **{threshold:.2f}**")
Defaults={
    "gender":"Other",
    "device":"Tablet",
    "payment_method":"Debit Card",
    "favorite_genre":"Drama"
}
monthly_price_map={
    "Basic":8.99,
    "Standard":13.99,
    "Premium":17.99
}

st.subheader("Enter Customer Details")
with st.form("customer_form"):
    age=st.number_input("Age",min_value=10,max_value=100,value=30)   
    region=st.selectbox("region",["Africa","Europe","Asia","South America","North America","Oceania"])
    watch_hours=st.number_input("Average watch hours(monthly)",min_value=0.0,value=5.0)
    avg_watch_time_per_day=watch_hours/30
    subscription_type=st.selectbox("subscription_type",["Basic","Standard","Premium"])
    number_of_profiles=st.slider("Number of Profiles",min_value=1,max_value=5,value=1)
    submit=st.form_submit_button("Predict Churn")

monthly_fee=monthly_price_map[subscription_type]

if submit:
    user_df=pd.DataFrame([{
        "age":age,
        "avg_watch_time_per_day":avg_watch_time_per_day,
        "region":region,
        "subscription_type":subscription_type,
        "number_of_profiles":number_of_profiles,
        "watch_hours":watch_hours, 
        "gender":Defaults["gender"],
        "device":Defaults["device"],
        "payment_method":Defaults["payment_method"],
        "favorite_genre":Defaults["favorite_genre"],
        "monthly_fee":monthly_fee

    }])


if submit:
    # Predict churn probability
    churn_prob=model.predict_proba(user_df)[0][1]

    # Apply threshold
    churn_pred = int(churn_prob >= threshold)
    

    st.subheader("Prediction Result")

    st.write(f"*Churn Probability:* {churn_prob:.2%}")
    st.write(f"*Decision Threshold:* {threshold:.2f}")

    if churn_pred == 1:
        st.error("🔴 High Risk of Churn")
    else:
        st.success("🟢 Low Risk of Churn")


    st.subheader("Key Risk Indicators")
    reasons = []

    if user_df["watch_hours"].iloc[0] < 8:
        reasons.append("Low recent watch time")

    if user_df["number_of_profiles"].iloc[0] > 3:
        reasons.append("Number of profile is less")

    if user_df["subscription_type"].iloc[0] == "Basic":
        reasons.append("Low-tier subscription plan")

    if reasons:
        explanation="* Customer may churn due to " + " ," .join (reasons) +  "."
    else:
        explanation="No major churn risk factors detected"
    st.write(explanation)

    def generate_actions(user_df, churn_prob):
    actions = []

    
    # 🔹 Engagement-based actions
    if watch_hours < 8:
        actions.append(" Recommend trending and personalized content")
        actions.append(" Send re-engagement email with content suggestions")

   
    
    # 🔹 Subscription value actions
    if subscription_type == "Basic":
        actions.append(" Offer upgrade to Standard or Premium plan")

    # 🔹 Family / multi-user incentives
    if num_profiles > 1:
        actions.append(" Promote family-friendly or multi-profile content")

    # 🔹 High churn probability fallback
    if churn_prob > 0.6:
        actions.append(" Provide exclusive retention offer")
        actions.append(" Priority customer support outreach")

    # If no actions triggered
    if not actions:
        actions.append("✅ No immediate action required")

    return actions

    st.write(actions)

@st.cache_resource
def load_pr_curve():
    with open("pr_curve.pkl","rb") as f:
        return pickle.load(f)
pr_data=load_pr_curve()
precision=pr_data["precision"]
recall=pr_data["recall"]
thresholds=pr_data["thresholds"]

import matplotlib.pyplot as plt
fig, ax = plt.subplots(figsize=(8, 5))

ax.plot(thresholds, precision[:-1], label="Precision")
ax.plot(thresholds, recall[:-1], label="Recall")

# Vertical line for user-selected threshold
ax.axvline(
    x=threshold,
    color="red",
    linestyle="--",
    label=f"Selected threshold = {threshold:.2f}"
)

ax.set_xlabel("Threshold")
ax.set_ylabel("Score")
ax.set_title("Precision & Recall vs Threshold")
ax.legend()
ax.grid(True)

st.pyplot(fig)




