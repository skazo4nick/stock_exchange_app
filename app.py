import streamlit as st
import snowflake.connector
import pandas as pd

# Streamlit app configuration
st.title("Stock Prices Data Viewer v0.0.1")

# Snowflake connection details
@st.cache_resource
def create_snowflake_connection():
    conn = snowflake.connector.connect(
        user=st.secrets["snowflake"]["user"],
        password=st.secrets["snowflake"]["password"],
        account=st.secrets["snowflake"]["account"],
        role=st.secrets["snowflake"]["role"],
        warehouse=st.secrets["snowflake"]["warehouse"],
        database=st.secrets["snowflake"]["database"],
        schema=st.secrets["snowflake"]["schema"]
    )
    return conn

# Fetch data from Snowflake
def fetch_stock_prices():
    conn = create_snowflake_connection()
    query = "SELECT * FROM stock_schema.stock_prices;"
    data = pd.read_sql(query, conn)
    conn.close()
    return data

# Button to load and display data
if st.button('Load Stock Prices Data'):
    with st.spinner("Connecting to Snowflake and retrieving data..."):
        data = fetch_stock_prices()
        st.success("Data loaded successfully!")
        st.dataframe(data)
      
