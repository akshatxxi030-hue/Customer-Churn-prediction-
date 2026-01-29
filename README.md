##Deployed demo link with streamlit- https://gle2jspvf48c5ihgqxrvvc.streamlit.app/
##Deployed fast api with render -https://customer-churn-prediction-gnnf.onrender.com/predict

NOTE-- THE API IS DEPLOYED WITH RENDER SO IT MIGHT TAKE 30 SECONDS TO GIVE THE FIRST PREDIDCTION DUE TO FREE PLAN LIMITS . 
SORRY FOR THE INCONVINENCE

# 📉 Customer Churn Prediction System

An end-to-end **Machine Learning–powered Customer Churn Prediction application** built using **FastAPI** (backend), **Streamlit** (frontend), fully **Dockerized**, and **deployed on Render**.  
The system predicts whether a customer is likely to churn, allows **manual threshold tuning**, highlights **risk indicators**, and provides **actionable retention strategies**.

---


## 🧠 Project Overview

Customer churn prediction is a critical business problem where identifying at-risk customers early can significantly improve retention.  
This project delivers a **production-ready ML pipeline** that supports real-time predictions with business-oriented decision control.

---

All components are containerized using **Docker** and deployed on **Render Cloud Platform**.

---

## ✨ Key Features

- Real-time churn prediction
- Manual probability threshold adjustment
- User-driven input form
- Churn probability with binary classification
- Risk indicator identification
- Actionable customer retention recommendations
- Scalable and cloud-deployable architecture

---

## 🧾 User Inputs

The system accepts customer details such as:
- Age
- Region
- Monthly watch hours
- Subscription type (Basic / Standard / Premium)
- Number of profiles

These features are validated using **Pydantic** before inference.

---

## 🎯 Manual Threshold Control

Instead of a fixed 0.5 cutoff, users can:
- Adjust the churn probability threshold manually
- Control precision vs recall trade-off
- Align predictions with business objectives

---

## 📊 Prediction Output

The model returns:
- **Churn Probability (%)**
- **Final Prediction (Churn / No Churn)**
- **Risk Level (Low / High)**
- **Key Risk Indicators**
- **Recommended Actions**

---

## 🧠 Risk Indicators

The system identifies churn drivers such as:
- Low engagement (watch hours)
- High subscription cost
- Multiple profiles usage
- Region-based behavioral patterns

---

## 🛠️ Recommended Actions

Based on risk level, the system suggests:
- Loyalty discounts
- Personalized content recommendations
- Engagement campaigns
- Subscription plan optimization

 Tech Stack

Backend
	•	FastAPI
	•	Pydantic
	•	Scikit-learn
	•	Uvicorn

Frontend
	•	Streamlit

DevOps & Deployment
	•	Docker
	•	Render

