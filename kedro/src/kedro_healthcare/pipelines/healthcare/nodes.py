
import pandas as pd

def clean_doctor_data(df: pd.DataFrame) -> pd.DataFrame:
    return df.dropna()

def clean_patient_data(df: pd.DataFrame) -> pd.DataFrame:
    return df.dropna()

def clean_insurance_data(df: pd.DataFrame) -> pd.DataFrame:
    return df.dropna()

def merge_patient_insurance(patients: pd.DataFrame, insurance: pd.DataFrame) -> pd.DataFrame:
    return patients.merge(insurance, on="Insurance_ID", how="left")

def merge_with_doctor(df: pd.DataFrame, doctors: pd.DataFrame) -> pd.DataFrame:
    return df.merge(doctors, on="Doctor_ID", how="left")

def final_transform(df: pd.DataFrame) -> pd.DataFrame:
    df["Patient_Summary"] = df["Name"] + " - " + df["Insurance_Provider"]
    return df
