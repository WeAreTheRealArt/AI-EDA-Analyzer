import streamlit as st  
import pandas as pd
from eda import get_dataset_shape, get_column_names, get_data_types, get_missing_values, get_duplicated_values

uploaded_file = st.file_uploader( "Upload a CSV file",type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.subheader("Preview")
    st.dataframe(df.head())


    rows, columns = get_dataset_shape(df)
    missing = get_missing_values(df)
    duplicated = get_duplicated_values(df)

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Rows", rows)

    with col2:
        st.metric("Columns", columns)

    with col3:
        st.metric("Missing Values", missing)

    with col4:
        st.metric("Duplicated Rows", duplicated)

    st.subheader("Columns")
    column_names = get_column_names(df)
    column_df = pd.DataFrame(
    {
        "Column Names": column_names
    }
    )

    st.table(column_df)

    st.subheader("DataTypes")
    data_types = get_data_types(df)
    data_types_df = pd.DataFrame(
        list(data_types.items()),
        columns=["Column", "Data Type"]
    )

    st.table(data_types_df)