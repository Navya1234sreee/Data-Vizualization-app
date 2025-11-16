import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set page configuration
st.set_page_config(page_title="Data Visualization App", layout="wide")

# Title and subheader
st.title('📊 Data Visualization App')
st.subheader(
    "Upload a file and explore the data with interactive visualization.\n\n"
    "This app allows you to perform basic Exploratory Data Analysis (EDA) "
    "and visualize your data through various types of plots."
)

# Upload file (CSV or Excel)
uploaded_file = st.file_uploader("📁 Choose a CSV or Excel file", type=["csv", "xlsx"])

if uploaded_file is not None:
    # Check uploaded file type and load accordingly
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    # Display data preview
    st.write("### 🧾 Data Preview")
    st.dataframe(df.head())

    # Display basic summary
    st.write("### 📊 Data Summary")
    st.write(df.describe(include='all'))

    # Column information and search functionality
    st.write("### 🔍 Column Information")
    search_column = st.text_input("Search column name")

    if search_column:
        if search_column in df.columns:
            st.write(f"**Column:** {search_column}")
            st.write(f"Length: {len(df[search_column])}")
            st.write(f"Missing Values: {df[search_column].isnull().sum()}")
            st.write(f"Unique Values: {df[search_column].nunique()}")
        else:
            st.warning("⚠️ Column not found.")

    # Display shape of the dataframe
    st.write("### 📐 DataFrame Shape")
    st.write(f"Rows: {df.shape[0]}")
    st.write(f"Columns: {df.shape[1]}")

    # Data Visualization Section
    st.write("### 📈 Data Visualization")

    # Sidebar for plot customization
    st.sidebar.title("⚙️ Plot Settings")

    # Select columns for X and Y axes
    X_column = st.sidebar.selectbox("Select X-axis column", df.columns)
    Y_column = st.sidebar.selectbox("Select Y-axis column", df.columns)

    # Choose the plot type
    plot_type = st.sidebar.selectbox(
        "Select Plot Type",
        ["Scatter Plot", "Line Plot", "Bar Plot", "Histogram", "Box Plot"]
    )

    # Generate and display the selected plot
    plt.figure(figsize=(10, 6))

    if plot_type == "Scatter Plot":
        sns.scatterplot(data=df, x=X_column, y=Y_column)
        st.pyplot(plt)

    elif plot_type == "Line Plot":
        sns.lineplot(data=df, x=X_column, y=Y_column)
        st.pyplot(plt)

    elif plot_type == "Bar Plot":
        sns.barplot(data=df, x=X_column, y=Y_column)
        st.pyplot(plt)

    elif plot_type == "Histogram":
        sns.histplot(df[X_column], kde=True, bins=30)
        st.pyplot(plt)

    elif plot_type == "Box Plot":
        sns.boxplot(data=df, x=X_column, y=Y_column)
        st.pyplot(plt)

else:
    st.info("👆 Please upload a CSV or Excel file to get started.")
