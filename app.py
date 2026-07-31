import streamlit as st  
import pandas as pd
from eda import get_dataset_shape, get_column_names, get_data_types, get_missing_values, get_duplicated_values, get_summary_statistics, get_numerical_columns, get_categorical_columns, get_unique_values, get_correlation_matrix, get_histogram, get_boxplot, get_heatmap, get_countplot

from ai import test_model, model, prepare_context, build_prompt, generate_response
#from report import generate_report_data


st.title("🤖 AI EDA Analyzer")

st.caption(
    "Upload a dataset, explore it visually, and ask AI-powered questions."
)

st.markdown("---")

uploaded_file = st.file_uploader(
        "Upload CSV",
        type="csv"
    )

if uploaded_file is None:
    st.info("📁 Please upload a CSV file to begin analysis.")
else:
    st.success("✅ Dataset loaded successfully!")


if uploaded_file is not None:

    # ==========================
    # Read Dataset
    # ==========================
    df = pd.read_csv(uploaded_file)

    # ==========================
    # Calculate Everything
    # ==========================

    rows, columns = get_dataset_shape(df)
    missing = get_missing_values(df)
    duplicated = get_duplicated_values(df)

    column_names = get_column_names(df)
    data_types = get_data_types(df)

    summary_statistics = get_summary_statistics(df)

    numerical_columns = get_numerical_columns(df)
    categorical_columns = get_categorical_columns(df)

    unique_values = get_unique_values(df)

    correlation_matrix = get_correlation_matrix(df)


    # report_data = generate_report_data(
    #     df=df,
    #     rows=rows,
    #     columns=columns,
    #     missing_values=missing,
    #     duplicates=duplicated,
    #     column_names=column_names,
    #     data_types=data_types,
    #     summary_statistics=summary_statistics,
    #     numerical_columns=numerical_columns,
    #     categorical_columns=categorical_columns,
    #     unique_values=unique_values,
    #     correlation_matrix=correlation_matrix,
    # )

    # ==========================
    # Metrics
    # ==========================

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Rows", rows)

    with col2:
        st.metric("Columns", columns)

    with col3:
        st.metric("Missing Values", missing)

    with col4:
        st.metric("Duplicated Rows", duplicated)

    # ==========================
    # Tabs
    # ==========================

    tab1, tab2, tab3, tab4 = st.tabs(
        [
            "📄 Dataset",
            "📊 Statistics",
            "📈 Visualizations",
            "🤖 AI Assistant",
        ]
    )

    # ==========================================================
    # DATASET TAB
    # ==========================================================

    with tab1:

        st.subheader("Preview")
        st.dataframe(df.head())

        st.subheader("Columns")

        column_df = pd.DataFrame(
            {
                "Column Names": column_names
            }
        )

        st.table(column_df)

        st.subheader("Data Types")

        data_types_df = pd.DataFrame(
            list(data_types.items()),
            columns=["Column", "Data Type"]
        )

        data_types_df["Data Type"] = data_types_df["Data Type"].astype(str)

        st.table(data_types_df)

    # ==========================================================
    # STATISTICS TAB
    # ==========================================================

    with tab2:

        with st.expander("Summary Statistics", expanded=False):
            st.dataframe(summary_statistics)

        with st.expander("Column Information", expanded=False):

            columns_df = pd.DataFrame(
                {
                    "Numerical Columns": pd.Series(numerical_columns),
                    "Categorical Columns": pd.Series(categorical_columns),
                }
            )

            st.dataframe(columns_df)

        with st.expander("Unique Values", expanded=False):

            unique_values_df = unique_values.reset_index()
            unique_values_df.columns = [
                "Column",
                "Unique Values",
            ]

            st.dataframe(unique_values_df)

        with st.expander("Correlation Matrix", expanded=False):
            st.dataframe(correlation_matrix)

    # ==========================================================
    # VISUALIZATION TAB
    # ==========================================================

    with tab3:

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
            pass

    # ==========================================================
    # AI TAB
    # ==========================================================

    with tab4:

            context = prepare_context(
            shape=(rows, columns),
            missing_values=missing,
            duplicates=duplicated,
            summary_statistics=summary_statistics,
            numerical_columns=numerical_columns,
            categorical_columns=categorical_columns,
            unique_values=unique_values,
            correlation_matrix=correlation_matrix,
        )

            user_question = st.chat_input("Ask anything about your dataset...")


            if user_question:

                prompt = build_prompt(context, user_question)

                with st.spinner("🤖 Analyzing your dataset..."):

                    response = generate_response(model, prompt)

                st.markdown(response)
                pass






