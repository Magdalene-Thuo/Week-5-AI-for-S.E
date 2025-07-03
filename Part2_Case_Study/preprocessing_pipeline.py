import pandas as pd
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer

def preprocess_patient_data(df):
    # Drop PII columns
    df = df.drop(['name', 'SSN'], axis=1)

    # Impute missing values
    imputer = SimpleImputer(strategy='mean')
    df[['blood_pressure', 'heart_rate']] = imputer.fit_transform(df[['blood_pressure', 'heart_rate']])

    # Encode diagnosis
    encoder = OneHotEncoder(sparse=False)
    diag_encoded = encoder.fit_transform(df[['diagnosis_code']])
    
    # Normalize vitals
    scaler = StandardScaler()
    df[['blood_pressure', 'heart_rate']] = scaler.fit_transform(df[['blood_pressure', 'heart_rate']])

    return df
