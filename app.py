import streamlit as st
import snowflake.connector
import pandas as pd

# Streamlit app configuration
st.title("Stock Prices Data Viewer")

# Snowflake connection details
@st.cache_resource
def create_snowflake_connection():
    conn = snowflake.connector.connect(
        user='YOUR_SNOWFLAKE_USER',
        password='YOUR_SNOWFLAKE_PASSWORD',
        account='YOUR_SNOWFLAKE_ACCOUNT',
        warehouse='YOUR_WAREHOUSE',
        database='YOUR_DATABASE',
        schema='YOUR_SCHEMA'
    )
    return conn

# Fetch data from Snowflake
def fetch_stock_prices():
    conn = create_snowflake_connection()
    query = "SELECT * FROM stock_prices;"
    data = pd.read_sql(query, conn)
    conn.close()
    return data

# Button to load and display data
if st.button('Load Stock Prices Data'):
    with st.spinner("Connecting to Snowflake and retrieving data..."):
        data = fetch_stock_prices()
        st.success("Data loaded successfully!")
        st.dataframe(data)
      
