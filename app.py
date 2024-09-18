import streamlit as st
import snowflake.connector
import pandas as pd
import matplotlib.pyplot as plt

# Streamlit app configuration
st.title("Stock Prices Data Viewer v0.0.1")

# Snowflake connection details
@st.cache_resource
def create_snowflake_connection():
    try:
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
    except snowflake.connector.errors.ProgrammingError as e:
        st.error(f"Programming error: {e}")
    except snowflake.connector.errors.DatabaseError as e:
        st.error(f"Database error: {e}")
    except Exception as e:
        st.error(f"Unexpected error: {e}")    

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
      
# Button to visualize OPEN_PRICE and CLOSE_PRICE
if st.button('Visualize Open and Close Prices'):
    with st.spinner("Loading data for visualization..."):
        data = fetch_stock_prices()
        df = pd.DataFrame(data)
        
        plt.figure(figsize=(10, 5))
        plt.plot(data['trade_date'], data['open_price'], label='Open Price', marker='o')
        plt.plot(data['trade_date'], data['close_price'], label='Close Price', marker='x')
        plt.title('Open vs Close Prices')
        plt.xlabel('Trade Date')
        plt.ylabel('Price')
        plt.xticks(rotation=45)
        plt.legend()
        plt.tight_layout()
        
        # Display the plot in Streamlit
        st.pyplot(plt)
