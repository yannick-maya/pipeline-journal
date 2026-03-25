import streamlit as st
import pandas as pd

# Title of the app
st.title('Data Visualization Dashboard')

# Load your data
# Replace 'data.csv' with your data file
@st.cache
def load_data():
    data = pd.read_csv('data.csv')
    return data

# Display data
if st.checkbox('Show Raw Data'):
    df = load_data()
    st.write(df)

# Sample visualization - replace with actual visualizations
st.line_chart(df['column_name'])  # Replace 'column_name' with your data column
