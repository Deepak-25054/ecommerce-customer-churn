import os
import joblib
import pandas as pd


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MODEL_PATH = os.path.join(
    BASE_DIR,
    "models",
    "xgboost_churn_model.pkl"
)

PREPROCESSOR_PATH = os.path.join(
    BASE_DIR,
    "models",
    "preprocessor.pkl"
)


# Load model and preprocessing pipeline
model = joblib.load(MODEL_PATH)
preprocessor = joblib.load(PREPROCESSOR_PATH)


def predict_churn(customer_data):
    """
    Predict whether a customer is likely to churn.

    Parameters:
        customer_data (dict): Customer feature values.

    Returns:
        tuple: Prediction and churn probability.
    """

    df = pd.DataFrame([customer_data])

    # Apply the same preprocessing used during training
    processed_data = preprocessor.transform(df)

    # Make prediction
    prediction = model.predict(processed_data)[0]

    # Get probability of churn
    churn_probability = model.predict_proba(processed_data)[0][1]

    return int(prediction), float(churn_probability)