from fastapi import FastAPI
from pydantic import BaseModel,Field,computed_field
from typing import Literal,Annotated,ClassVar,Dict
import pandas as pd
from schema.user_input import user_input
from model.predict import churn_decision_engine,model

app= FastAPI()


@app.get("/")
def home():
    return{'message':'Customer churn prediction and analysis API'}

@app.get('/health')
def health_check():
    return{
        'status':'OK',
        'API last updated':"27/01/2026",
        'model_loaded':model is not None
    }


@app.post("/predict")
def predict_churn(user_input:user_input,threshold:float=0.39):
    return churn_decision_engine(user_input,threshold)