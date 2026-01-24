from fastapi import FastAPI
from pydantic import BaseModel,Field,computed_field
from typing import Literal,Annotated,ClassVar,Dict
import pickle
import pandas as pd

with open("churn_model.pkl","rb") as f:
    bundle=pickle.load(f)
    model=bundle["model"]

app= FastAPI()

# Pydantic model to validate data

class user_input(BaseModel):
    age:Annotated[int,Field(...,ge=0,le=100)]
    region:Annotated[str,Field(...,description="Enter the region user belongs to")]
    watch_hours:Annotated[float,Field(...,description="Enter the monthly watch time")]
    subscription_type:Annotated[Literal["Basic","Standard","Premium"],Field(...,description="Enter the subscription type")]
    number_of_profiles:Annotated[int,Field(...,ge=1,le=5,description="Enter the number of profiles user has")]
    gender:Literal["Male","Female","Other"]="Other"
    device:Literal['TV', 'Mobile', 'Laptop', 'Desktop', 'Tablet']="Tablet"
    payment_method:Literal['Gift Card', 'Crypto', 'Debit Card', 'PayPal', 'Credit Card']="Debit Card"
    favorite_genre:Literal['Action', 'Sci-Fi', 'Drama', 'Horror', 'Romance', 'Comedy','Documentary']="Documentary"
    
    monthly_price_map:ClassVar[Dict[str,float]]={
    "Basic":8.99,
    "Standard":13.99,
    "Premium":17.99
}
    @computed_field
    @property
    def avg_watch_time_per_day(self) ->float:
        return self.watch_hours/30
    
    @computed_field
    @property
    def monthly_fee(self) -> float:
        return self.monthly_price_map[self.subscription_type]
    
# Creating a dataframe
def user_df(user_input):
    return pd.DataFrame([user_input.model_dump()])

# Preprocessing and prediction from the pipeline
def predict(user_input):
    df=user_df(user_input)
    return float(model.predict_proba(df)[0][1])

# Manual threshold
def apply_threshold(prob,threshold):
    return prob>=threshold


# Risk indicators
def risk_indicators(user_input,churn_prob):
    indicators = []
    if user_input.watch_hours <8:
        indicators.append("Low recent watch time")

    
    if user_input.subscription_type=="Basic":
        indicators.append("Low-tier subscription")
    
    if churn_prob>0.7:
        indicators.append("Very high churn probabiltiy")
    return indicators


def generate_actions(user_input, churn_prob):
        actions=[]

        watch_hours = user_input.watch_hours
        monthly_fee = user_input.monthly_fee
        subscription_type = user_input.subscription_type
        num_profiles = user_input.number_of_profiles

    # 🔹 Engagement-based actions
        if watch_hours < 8:
            actions.append(" Recommend trending and personalized content")
            actions.append(" Send re-engagement email with content suggestions")

    

    # 🔹 Subscription value actions
        if subscription_type == "Basic":
            actions.append(" Offer upgrade to Standard or Premium plan")

    # 🔹 Family / multi-user incentives
        if num_profiles > 3:
            actions.append(" Promote family-friendly or multi-profile content to keep engaged")

    # 🔹 High churn probability fallback
        if churn_prob > 0.7:
            actions.append(" Provide exclusive retention offer")
            actions.append(" Priority customer support outreach")

    # If no actions triggered
        if not actions:
            actions.append(" No immediate action required")

        return actions
        
def churn_decision_engine(user_input, threshold=0.39):
    churn_prob = predict(user_input)
    churn_percent=round(churn_prob*100)
    risk_level = "High" if churn_prob >= threshold else "Low"

    indicators = risk_indicators(user_input, churn_prob)
    actions = generate_actions(user_input, churn_prob)

    return {
        "churn_probability": churn_percent,
        
        "threshold": threshold,
        "risk_level": risk_level,
        "risk_indicators": indicators,
        "recommended_actions": actions
    }

@app.post("/predict")
def predict_churn(user_input:user_input,threshold:float=0.39):
    return churn_decision_engine(user_input,threshold)