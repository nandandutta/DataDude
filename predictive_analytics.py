import pandas as pd
import os
import streamlit as st
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.metrics import accuracy_score, mean_squared_error

# def create_folder(folder_name):
#     """Create a folder if it does not exist."""
#     if not os.path.exists(folder_name):
#         os.makedirs(folder_name)

def predictive_analytics():
    st.title("Predictive Analytics")

    # Create 'data_analysis' folder
    #create_folder('data_analysis')

    # Upload file
    uploaded_file = st.file_uploader("Choose a file (Excel or CSV)", type=["xlsx", "csv"])

    if uploaded_file is not None:
        # Save file to 'data_analysis' folder
        file_path = os.path.join('data_analysis', uploaded_file.name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        st.write(f"File saved to {file_path}")

        # Load data
        try:
            if uploaded_file.type == "text/csv":
                df = pd.read_csv(file_path)
            else:
                df = pd.read_excel(file_path)

            st.write("Data Preview:")
            st.dataframe(df.head())

            # Select X and Y columns
            x_cols = st.multiselect("Select X columns", df.columns)
            y_col = st.selectbox("Select Y column", df.columns)

            # Ensure Y column is a single value
            if len(y_col) > 1:
                st.error("Y column must be a single value")
                return

            # Split data into training and testing sets
            X = df[x_cols]
            y = df[y_col]
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

            # Choose algorithm
            algorithm = st.selectbox("Choose algorithm", ["Logistic Regression", "Linear Regression"])

            # Train model
            if algorithm == "Logistic Regression":
                model = LogisticRegression()
            else:
                model = LinearRegression()
            model.fit(X_train, y_train)

            # Make predictions
            y_pred = model.predict(X_test)

            # Evaluate model
            if algorithm == "Logistic Regression":
                accuracy = accuracy_score(y_test, y_pred.round())
                st.write(f"Accuracy: {accuracy:.3f}")
            else:
                mse = mean_squared_error(y_test, y_pred)
                st.write(f"Mean Squared Error: {mse:.3f}")

        except Exception as e:
            st.error(f"An error occurred: {e}")
