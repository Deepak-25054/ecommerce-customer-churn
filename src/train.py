import os
import joblib
import pandas as pd

from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier

from src.preprocessing import (
    load_data,
    clean_data,
    prepare_features,
    create_preprocessor
)


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA_PATH = os.path.join(
    BASE_DIR,
    "data",
    "raw",
    "data_ecommerce_customer_churn.csv"
)

MODEL_DIR = os.path.join(BASE_DIR, "models")

MODEL_PATH = os.path.join(
    MODEL_DIR,
    "xgboost_churn_model.pkl"
)

PREPROCESSOR_PATH = os.path.join(
    MODEL_DIR,
    "preprocessor.pkl"
)


def train_model():
    """Train the XGBoost churn prediction model."""

    print("Loading dataset...")

    df = load_data(DATA_PATH)

    print("Original dataset shape:", df.shape)

    # Clean dataset
    df_clean = clean_data(df)

    print("Cleaned dataset shape:", df_clean.shape)

    # Separate features and target
    X, y = prepare_features(df_clean)

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.20,
        random_state=42,
        stratify=y
    )

    print("Training data:", X_train.shape)
    print("Testing data:", X_test.shape)

    # Create preprocessing pipeline
    preprocessor = create_preprocessor(X_train)

    # Fit preprocessing on training data
    X_train_processed = preprocessor.fit_transform(X_train)

    # Transform test data
    X_test_processed = preprocessor.transform(X_test)

    print("Processed training data:", X_train_processed.shape)
    print("Processed testing data:", X_test_processed.shape)

    # Create XGBoost model
    model = XGBClassifier(
        n_estimators=200,
        max_depth=5,
        learning_rate=0.05,
        subsample=0.8,
        colsample_bytree=0.8,
        random_state=42,
        eval_metric="logloss"
    )

    # Train model
    print("Training XGBoost model...")

    model.fit(X_train_processed, y_train)

    print("XGBoost training completed!")

    # Create models directory
    os.makedirs(MODEL_DIR, exist_ok=True)

    # Save model
    joblib.dump(model, MODEL_PATH)

    # Save preprocessor
    joblib.dump(preprocessor, PREPROCESSOR_PATH)

    print("\nModel saved to:")
    print(MODEL_PATH)

    print("\nPreprocessor saved to:")
    print(PREPROCESSOR_PATH)

    return model, preprocessor


if __name__ == "__main__":
    train_model()