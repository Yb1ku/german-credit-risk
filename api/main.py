from pydantic import BaseModel
from fastapi import FastAPI
import pandas as pd
import joblib

model = joblib.load("xgboost_credit_model.joblib")

app = FastAPI()

class ModelInput(BaseModel):
    Status_of_existing_checking_account: str
    Duration_in_month: int
    Credit_history: str
    Purpose: str
    Credit_amount: int
    Savings_account_bonds: str
    Present_employment_since: str
    Installment_rate: int
    Personal_status_and_sex: str
    Other_debtors: str
    Present_residence_since: int
    Property: str
    Age: int
    Other_installment_plans: str
    Housing: str
    Number_of_existing_credits: int
    Job: str
    People_liable: int
    Telephone: str
    Foreign_worker: str


@app.post("/predict")
def predict(input_data: ModelInput):
    input_df = pd.DataFrame([input_data.model_dump()])


    categorical_cols = [
        "Status_of_existing_checking_account",
        "Purpose",
        "Credit_history",
        "Savings_account_bonds",
        "Present_employment_since",
        "Personal_status_and_sex",
        "Other_debtors",
        "Property",
        "Other_installment_plans",
        "Housing",
        "Job",
        "Telephone",
        "Foreign_worker"
    ]
    for col in categorical_cols:
        input_df[col] = input_df[col].astype("category")


    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df)[0][1] # Probability of class 1 (good credit)

    return {
        "prediction": int(prediction),
        "probability": round(float(probability), 3)
    }