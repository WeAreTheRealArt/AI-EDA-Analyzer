import pandas as pd

def get_dataset_shape(df):
    return df.shape

def get_column_names(df):
    return df.columns.tolist()

def get_data_types(df):
    return df.dtypes.to_dict()

def get_missing_values(df):
    return df.isnull().sum().sum()

def get_duplicated_values(df):
    return df.duplicated().sum().sum()

def get_summary_statistics(df):
    summary = df.describe()

    summary.loc["mode"] = df.mode().iloc[0]
    
    return summary

def get_numerical_columns(df):
    return df.select_dtypes(include='number').columns.tolist()

def get_categorical_columns(df):
    return df.select_dtypes(include='category').columns.tolist()

def get_unique_values(df):
    return df.nunique()

def get_correlation_matrix(df):
    return df.corr(numeric_only=True)