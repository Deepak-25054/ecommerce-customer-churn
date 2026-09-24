# E-Commerce Customer Churn Prediction

An end-to-end Machine Learning application for predicting customer churn in an e-commerce business using **XGBoost, Python, and Flask**.

The project includes data preprocessing, exploratory data analysis, machine learning model comparison, XGBoost-based churn prediction, and a Flask web application with an analytics dashboard and detailed prediction reports.

---

## Project Overview

Customer churn is an important business problem in e-commerce. Identifying customers who are likely to stop using a service can help businesses understand customer behavior and support customer retention strategies.

This project develops a machine learning system that predicts whether an e-commerce customer is likely to churn based on customer profile, shopping behavior, satisfaction, complaint history, and other behavioral attributes.

The final trained **XGBoost Classifier** is integrated into a Flask web application for real-time individual customer predictions.

---

## Problem Statement

E-commerce businesses collect information about customer behavior such as:

- Customer tenure
- Distance from warehouse
- Number of registered devices
- Preferred order category
- Satisfaction score
- Marital status
- Number of addresses
- Complaint history
- Days since last order
- Cashback amount

The objective is to use these features to predict customer churn and estimate the probability that a customer may leave the service.

---

## Objectives

- Analyze customer churn behavior using Exploratory Data Analysis.
- Clean and preprocess the customer dataset.
- Handle missing values and duplicate records.
- Compare multiple machine learning classification algorithms.
- Train an XGBoost classification model.
- Evaluate the model using classification metrics.
- Save the trained model and preprocessing pipeline.
- Deploy the model using Flask.
- Provide an interactive customer churn prediction interface.
- Provide an analytics dashboard.
- Generate a detailed prediction report for individual customers.

---

## Dataset

The project uses the **E-commerce Customer Churn** dataset.

### Dataset Source

Kaggle:

https://www.kaggle.com/datasets/samuelsomaya/e-commerce-customer-churn

### Original Dataset

- Records: 3,941
- Features: 10
- Target: Churn
- Total columns: 11

### Final Cleaned Dataset

After duplicate removal and missing-value handling:

- Records: 3,269
- Features: 10
- Target: Churn

---

## Features

The model uses the following features:

| Feature | Description |
|---|---|
| Tenure | Duration of the customer relationship |
| WarehouseToHome | Distance between warehouse and customer home |
| NumberOfDeviceRegistered | Number of devices registered by the customer |
| PreferredOrderCat | Customer's preferred order category |
| SatisfactionScore | Customer satisfaction rating |
| MaritalStatus | Customer marital status |
| NumberOfAddress | Number of addresses registered |
| Complain | Whether the customer submitted a complaint |
| DaySinceLastOrder | Number of days since the last order |
| CashbackAmount | Cashback amount received by the customer |

### Target Variable

`Churn`

- `0` → Customer is not likely to churn
- `1` → Customer is likely to churn

---

## Machine Learning Workflow

The project follows the following workflow:

```text
Dataset
   ↓
Data Cleaning
   ↓
Exploratory Data Analysis
   ↓
Feature Preparation
   ↓
Train-Test Split
   ↓
Preprocessing Pipeline
   ↓
Model Training
   ↓
Model Evaluation
   ↓
XGBoost Model Selection
   ↓
Model Serialization
   ↓
Flask Deployment
   ↓
Customer Churn Prediction
```

---

## Data Preprocessing

The preprocessing pipeline includes several steps.

### 1. Duplicate Removal

Duplicate records were identified and removed from the dataset.

### 2. Missing Value Handling

Missing numerical values were filled using the median value of the corresponding feature.

### 3. Feature Renaming

The original dataset contains:

```text
PreferedOrderCat
```

This was renamed to:

```text
PreferredOrderCat
```

### 4. Numerical Feature Scaling

Numerical features were standardized using:

```text
StandardScaler
```

### 5. Categorical Encoding

Categorical variables were converted into numerical representations using:

```text
OneHotEncoder
```

### 6. Preprocessing Pipeline

A Scikit-learn `ColumnTransformer` and preprocessing pipelines were used to ensure that the same preprocessing steps are applied during training and prediction.

---

## Exploratory Data Analysis

Several relationships between customer characteristics and churn were analyzed.

### Complaint and Churn

Customers with a recorded complaint showed an observed churn rate of approximately:

```text
31.81%
```

### Tenure

Tenure showed a negative correlation with churn of approximately:

```text
-0.34
```

### Preferred Order Category

Observed churn rates varied across preferred order categories.

### Satisfaction Score

Churn rates also varied across different customer satisfaction levels.

### EDA Tools

The following libraries were used:

- Pandas
- NumPy
- Matplotlib
- Seaborn

---

# Machine Learning Models

Three classification models were evaluated.

### 1. Logistic Regression

Logistic Regression was used as the baseline classification model.

### 2. Random Forest

Random Forest was used as an ensemble learning model based on multiple decision trees.

### 3. XGBoost

XGBoost was evaluated as a gradient boosting classification algorithm and was selected for deployment based on the evaluation results.

---

## Model Comparison

| Model | Accuracy | Precision | Recall | F1-Score | ROC-AUC |
|---|---:|---:|---:|---:|---:|
| Logistic Regression | 89.45% | 75.00% | 53.27% | 62.30% | 92.39% |
| Random Forest | 90.83% | 77.01% | 62.62% | 69.07% | 95.14% |
| **XGBoost** | **91.13%** | **75.26%** | **68.22%** | **71.57%** | **95.76%** |

The XGBoost model was selected for deployment based on its evaluation results, particularly its recall, F1-score, and ROC-AUC.

---

## Final Model Performance

The deployed XGBoost model achieved the following results on the held-out test dataset:

| Metric | Score |
|---|---:|
| Accuracy | **91.13%** |
| Precision | **75.26%** |
| Recall | **68.22%** |
| F1-Score | **71.57%** |
| ROC-AUC | **95.76%** |

---

## XGBoost Configuration

The final model uses the following configuration:

```python
XGBClassifier(
    n_estimators=200,
    max_depth=5,
    learning_rate=0.05,
    subsample=0.8,
    colsample_bytree=0.8,
    random_state=42,
    eval_metric="logloss"
)
```

---

# Web Application

The trained XGBoost model is deployed using **Flask**.

The application provides an interactive interface for individual customer churn prediction.

---

## Application Features

### 1. Individual Customer Prediction

Users can enter customer information through the web form.

The application returns:

- Churn prediction
- Churn probability
- Risk level

Example:

```text
Prediction: Likely to Churn
Risk: High Risk
Churn Probability: 95.04%
```

---

### 2. Analytics Dashboard

The analytics dashboard displays:

- Total customers
- Churned customers
- Non-churned customers
- Churn rate
- Number of features
- Model performance
- EDA-based churn insights

---

### 3. Detailed Prediction Report

After making an individual prediction, the application generates a detailed report containing:

- Prediction result
- Churn probability
- Risk level
- Customer information
- Shopping behavior
- Satisfaction information
- Model performance

---

## Application Architecture

```text
                   ┌─────────────────────┐
                   │   Customer Input     │
                   └──────────┬──────────┘
                              │
                              ▼
                   ┌─────────────────────┐
                   │      Flask App      │
                   └──────────┬──────────┘
                              │
                              ▼
                   ┌─────────────────────┐
                   │ Preprocessing       │
                   │ Pipeline            │
                   └──────────┬──────────┘
                              │
                              ▼
                   ┌─────────────────────┐
                   │ XGBoost Classifier   │
                   └──────────┬──────────┘
                              │
                              ▼
                   ┌─────────────────────┐
                   │ Prediction +         │
                   │ Probability          │
                   └──────────┬──────────┘
                              │
                ┌─────────────┴─────────────┐
                ▼                           ▼
        Prediction Page              Detailed Report
                │
                ▼
        Analytics Dashboard
```

---

## Project Structure

```text
ecommerce-customer-churn/
│
├── data/
│   ├── raw/
│   │   └── data_ecommerce_customer_churn.csv
│   │
│   └── processed/
│       └── cleaned_ecommerce_customer_churn.csv
│
├── models/
│   ├── preprocessor.pkl
│   └── xgboost_churn_model.pkl
│
├── notebooks/
│   └── Deepak_Ecommerce_Customer_Churn.ipynb
│
├── results/
│
├── src/
│   ├── __init__.py
│   ├── predict.py
│   ├── preprocessing.py
│   └── train.py
│
├── static/
│   ├── css/
│   │   └── style.css
│   │
│   └── js/
│       └── script.js
│
├── templates/
│   ├── dashboard.html
│   ├── index.html
│   └── result.html
│
├── app.py
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
```

---

# Technologies Used

## Programming Language

- Python

## Machine Learning

- Scikit-learn
- XGBoost

## Data Processing

- Pandas
- NumPy

## Data Visualization

- Matplotlib
- Seaborn

## Web Development

- Flask
- HTML
- CSS
- JavaScript

## Model Serialization

- Joblib

## Development Tools

- Jupyter Notebook
- VS Code
- Git
- GitHub

---

# Installation

## 1. Clone the Repository

```bash
git clone https://github.com/Deepak-25054/ecommerce-customer-churn.git
```

## 2. Navigate to the Project Directory

```bash
cd ecommerce-customer-churn
```

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Run the Application

Start the Flask application:

```bash
python app.py
```

The application will run at:

```text
http://127.0.0.1:5000
```

Open the URL in your browser.

---

# Application URLs

### Customer Prediction

```text
http://127.0.0.1:5000/
```

### Analytics Dashboard

```text
http://127.0.0.1:5000/dashboard
```

### Detailed Prediction Report

The detailed report is generated after an individual prediction.

---

# Example Predictions

## Low-Risk Customer

Example input:

```text
Tenure: 12
Warehouse To Home: 15
Devices Registered: 3
Preferred Order Category: Laptop & Accessory
Satisfaction Score: 4
Marital Status: Married
Number of Addresses: 2
Complaint: No
Days Since Last Order: 5
Cashback Amount: 150
```

This type of customer produced a low churn probability during application testing.

---

## High-Risk Customer

Example input:

```text
Tenure: 1
Warehouse To Home: 30
Devices Registered: 5
Preferred Order Category: Mobile
Satisfaction Score: 2
Marital Status: Single
Number of Addresses: 5
Complaint: Yes
Days Since Last Order: 15
Cashback Amount: 150
```

During application testing, this configuration produced:

```text
Prediction: Likely to Churn
Risk: High Risk
Churn Probability: 95.04%
```

---

# Key Project Features

- End-to-end machine learning workflow
- Data preprocessing pipeline
- Exploratory data analysis
- Multiple model comparison
- XGBoost classification
- Model persistence using Joblib
- Flask deployment
- Real-time customer prediction
- Churn probability estimation
- Risk classification
- Analytics dashboard
- Detailed prediction report
- Responsive web interface
- Git/GitHub version control

---

# Limitations

- The model is trained on a specific e-commerce customer dataset.
- Predictions depend on the quality and distribution of input data.
- Model performance may change when applied to a different customer population.
- The current application focuses on individual customer prediction.
- Batch CSV prediction is not included in the current version.

---

# Future Scope

The project can be extended with:

- Batch CSV prediction
- Customer retention recommendations
- Model explainability using SHAP
- Automated model retraining
- Customer segmentation
- Advanced interactive analytics
- Cloud deployment
- Database integration
- Authentication and user management

---

# Author

**Deepak Rajak**

MCA Student  
Centurion University of Technology and Management, Bhubaneswar

GitHub:

https://github.com/Deepak-25054

Project Repository:

https://github.com/Deepak-25054/ecommerce-customer-churn

---

# License

This project is licensed under the MIT License.