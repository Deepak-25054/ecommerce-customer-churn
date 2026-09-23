import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder


TARGET_COLUMN = "Churn"


def load_data(file_path):
    """Load the e-commerce customer churn dataset."""
    return pd.read_csv(file_path)


def clean_data(df):
    """Clean the dataset."""

    df = df.copy()

    # Remove duplicate rows
    df = df.drop_duplicates().reset_index(drop=True)

    # Fix the original dataset spelling
    if "PreferedOrderCat" in df.columns:
        df = df.rename(
            columns={
                "PreferedOrderCat": "PreferredOrderCat"
            }
        )

    # Fill missing numerical values
    for column in [
        "Tenure",
        "WarehouseToHome",
        "DaySinceLastOrder"
    ]:
        df[column] = df[column].fillna(df[column].median())

    # Remove duplicates again
    df = df.drop_duplicates().reset_index(drop=True)

    return df


def prepare_features(df):
    """Separate features and target."""

    X = df.drop(columns=[TARGET_COLUMN])
    y = df[TARGET_COLUMN]

    return X, y


def create_preprocessor(df):
    """Create preprocessing pipeline."""

    numerical_features = [
        "Tenure",
        "WarehouseToHome",
        "NumberOfDeviceRegistered",
        "SatisfactionScore",
        "NumberOfAddress",
        "Complain",
        "DaySinceLastOrder",
        "CashbackAmount"
    ]

    categorical_features = [
        "PreferredOrderCat",
        "MaritalStatus"
    ]

    numerical_pipeline = Pipeline([
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", StandardScaler())
    ])

    categorical_pipeline = Pipeline([
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("encoder", OneHotEncoder(handle_unknown="ignore"))
    ])

    preprocessor = ColumnTransformer([
        ("num", numerical_pipeline, numerical_features),
        ("cat", categorical_pipeline, categorical_features)
    ])

    return preprocessor


def get_feature_names(preprocessor):
    """Get processed feature names."""

    return preprocessor.get_feature_names_out().tolist()