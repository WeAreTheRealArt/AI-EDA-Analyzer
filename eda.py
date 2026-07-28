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