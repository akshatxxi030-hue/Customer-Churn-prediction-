Deployed demo link with streamlit- https://gle2jspvf48c5ihgqxrvvc.streamlit.app/
Deployed fast api with render -https://customer-churn-prediction-gnnf.onrender.com/predict

This project is an end-to-end customer churn prediction system that combines a machine learning model with an interactive web interface and a production-ready backend API.

The application predicts the probability that a customer will churn, helping businesses identify at-risk users and take proactive retention actions.



Overview

Customer churn is a major challenge for subscription-based platforms.
This project demonstrates how machine learning can be used to:
	•	Estimate churn probability for individual customers
	•	Adjust decision thresholds dynamically
	•	Categorize customers into risk levels
	•	Support data-driven business decisions



Application Components

Frontend
	•	Built using Streamlit
	•	Provides an interactive UI for entering customer details
	•	Includes a decision threshold slider to control sensitivity
	•	Displays churn probability, risk level, and recommendations

Backend
	•	Built using FastAPI
	•	Exposes a REST API for predictions
	•	Dockerized for consistent deployment
	•	Deployed as a public API on the cloud

Machine Learning Model
	•	Trained using scikit-learn
	•	Uses a preprocessing pipeline for categorical and numerical features
	•	Outputs a probability score used for threshold-based classification



Features
	•	Interactive customer input form
	•	Adjustable churn decision threshold
	•	Real-time churn probability prediction
	•	Risk level classification (Low / Medium / High)
	•	Business-oriented risk indicators
	•	Actionable retention recommendations
	•	Production-style API deployment



How It Works
	1.	User enters customer details in the UI
	2.	Frontend sends a request to the FastAPI backend
	3.	Backend preprocesses input data

  Tech Stack
	•	Frontend: Streamlit
	•	Backend: FastAPI
	•	ML: Scikit-learn
	•	Data Processing: Pandas, NumPy
	•	Deployment: Docker, Render

  
  Deployment
	•	Backend API is containerized using Docker
	•	Deployed as a cloud web service
	•	Frontend communicates with the backend via a public API URL
	•	Frontend and backend are deployed independently


Project Highlights
	•	Clean separation of frontend and backend
	•	Production-ready API design
	•	Threshold-based business decision logic
	•	Cloud-native deployment workflow
	•	Suitable for real-world ML use cases
  
	4.	ML model predicts churn probability
	5.	Probability is compared against a threshold
	6.	Result is returned and displayed in the UI
