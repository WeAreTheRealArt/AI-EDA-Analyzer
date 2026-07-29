import streamlit as st  
import pandas as pd
from eda import get_dataset_shape, get_column_names, get_data_types, get_missing_values, get_duplicated_values, get_summary_statistics, get_numerical_columns, get_categorical_columns, get_unique_values, get_correlation_matrix, get_histogram, get_boxplot, get_heatmap, get_countplot   

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

    st.subheader("Summary Statisics")
    summary_statistics = get_summary_statistics(df)
    st.dataframe(summary_statistics)


    st.subheader("Columns information")
    numerical_columns = get_numerical_columns(df)
    categorical_columns = get_categorical_columns(df)

    columns_df = pd.DataFrame(
        {
            "Numerical Columns": pd.Series(numerical_columns),
            "Categorical Columns": pd.Series(categorical_columns)
        }
    )

    st.dataframe(columns_df)

    st.subheader("Unique Values")
    unique_values = get_unique_values(df)

    unique_values_df = unique_values.reset_index()
    unique_values_df.columns = ["Column", "Unique Values"]

    st.dataframe(unique_values_df)

    st.subheader("Correlation Matrix")
    correlation_matrix = get_correlation_matrix(df)
    st.dataframe(correlation_matrix)



    st.subheader("Visualizations")

    
    option = st.selectbox(
        "Select the Type of Plot",
        ("Histogram", "Box Plot", "Correlation Heatmap", "Count Plot"),
        index=None,
        placeholder="Select the Plot...",
    )


    if option == "Histogram":

        if not numerical_columns:
            st.warning("No numerical columns found in the dataset.")

        else:
            selected_column = st.selectbox(
                "Select Numerical Column",
                numerical_columns,
                index=None,
                placeholder="Select a column..."
            )

            if selected_column:
                fig = get_histogram(df, selected_column)
                st.pyplot(fig)

    elif option == "Box Plot":

        if not numerical_columns:
            st.warning("No numerical columns found in the dataset.")

        else:
            selected_column = st.selectbox(
                "Select Numerical Column",
                numerical_columns,
                index=None,
                placeholder="Select a column..."
            )

            if selected_column:
                fig = get_boxplot(df, selected_column)
                st.pyplot(fig)


    elif option == "Count Plot":

        if not categorical_columns:
            st.warning("No categorical columns found in the dataset.")
        else:
            selected_column = st.selectbox(
            "Select Categorical Column",
            categorical_columns,
            index=None,
            placeholder="Select Column..."
        )

            if selected_column:
                fig = get_countplot(df, selected_column)
                st.pyplot(fig)

    elif option == "Correlation Heatmap":

        if len(numerical_columns) < 2:
            st.warning("At least 2 numerical columns are required to generate a correlation heatmap.")

        else:
            correlation_matrix = get_correlation_matrix(df)
            fig = get_heatmap(correlation_matrix)
            st.pyplot(fig)

    