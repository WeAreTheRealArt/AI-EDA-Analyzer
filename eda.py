import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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

def get_histogram(df, column):
    fig, ax = plt.subplots(figsize=(8,5))

    ax.hist(df[column], bins=8, edgecolor="black")

    ax.set_title(f"Histogram of {column}")
    ax.set_xlabel(column)
    ax.set_ylabel("Frequency")

    return fig

def get_boxplot(df, column):
    fig, ax = plt.subplots(figsize=(8,5))
    ax.boxplot(df[column])

    ax.set_title(f"Boxplot of {column}")
    ax.set_xlabel(column)
    ax.set_ylabel("Frequency")
    
    return fig
    
def get_heatmap(correlation_matrix):

    fig, ax = plt.subplots(figsize=(8,5))

    sns.heatmap(
        correlation_matrix,
        annot=True,
        cmap="coolwarm",
        ax=ax
    )

    ax.set_title("Correlation Heatmap")

    return fig

def get_countplot(df, column):
    fig, ax = plt.subplots(figsize=(8,5))
    sns.countplot(data=df, x=column, ax=ax)
    ax.set_title(f"Count Plot of {column}")

    return fig