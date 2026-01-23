Deployed link - https://f8zrb697bgvnemvadtsktm.streamlit.app/

Project Overview

This project is a Customer Churn Prediction System built using Machine Learning and Streamlit.
It predicts the probability that a customer will churn (stop using a service) based on their usage behavior and subscription details.

In addition to prediction, the system provides business-friendly explanations and actionable insights to help reduce churn.

⸻

🎯 Key Features
	•	Predicts churn probability for individual customers
	•	Uses a custom decision threshold for better business control
	•	Displays clear risk status (Low / High churn risk)
	•	Highlights key churn risk indicators using rule-based logic
	•	Suggests actions required for customer retention
	•	Clean and interactive Streamlit UI and an EDA notebook

⸻

🧠 Model Details
	•	Algorithm: Logistic Regression
	•	Why Logistic Regression?
	•	Simple and interpretable
	•	Suitable for probability-based decisions
	•	Works well for churn classification problems
	•	Input Features (example):
	•	Average watch hours
	•	Subscription type
	•	Monthly fee
	•	Number of profiles
	•	Payment method
	•	Device type
	•	User activity indicators
	•	Output:
	•	Churn probability (0–100%)
	•	Binary churn decision based on threshold

⸻



🖥️ Application Interface

The Streamlit app allows users to:
	1.	Enter customer details using sliders and dropdowns
	2.	Click Predict Churn
	3.	View:
	•	Churn probability
	•	Decision threshold
	•	Risk status
	•	Key risk indicators
	•	Suggested actions

⸻

⚙️ Tech Stack
	•	Python
	•	Pandas, NumPy
	•	Scikit-learn
	•	Streamlit
	•	Pickle
