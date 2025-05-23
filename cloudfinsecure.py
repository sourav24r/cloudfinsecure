import streamlit as st
import boto3
import pandas as pd

# Set page title
st.set_page_config(page_title="CloudFinSecure Dashboard", layout="wide")

# DynamoDB table name
DYNAMO_TABLE_NAME = 'transactions_cloudfinsecure'

# Initialize DynamoDB resource
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(DYNAMO_TABLE_NAME)

@st.cache_data
def fetch_data():
    """Fetch all records from DynamoDB table and return as DataFrame."""
    response = table.scan()
    data = response['Items']

    while 'LastEvaluatedKey' in response:
        response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
        data.extend(response['Items'])

    return pd.DataFrame(data)

# Fetch data
df = fetch_data()

# Convert numeric columns
df['amount'] = pd.to_numeric(df['amount'], errors='coerce')
df['risk_score'] = pd.to_numeric(df['risk_score'], errors='coerce')

# Title
st.title("💼 CloudFinSecure – Employee Transaction Fraud Dashboard")

# Show filters
st.sidebar.header("🔍 Filter Transactions")
risk_level = st.sidebar.multiselect("Risk Level", options=df['risk_level'].unique(), default=list(df['risk_level'].unique()))
location = st.sidebar.multiselect("Location", options=df['location'].unique(), default=list(df['location'].unique()))

filtered_df = df[(df['risk_level'].isin(risk_level)) & (df['location'].isin(location))]

# Show KPIs
st.markdown("### 📊 Key Metrics")
col1, col2, col3 = st.columns(3)
col1.metric("Total Transactions", len(filtered_df))
col2.metric("Total Amount (₹)", f"{filtered_df['amount'].sum():,.2f}")
col3.metric("High Risk Transactions", (filtered_df['risk_level'] == 'HIGH').sum())

# Show table
st.markdown("### 📋 Transaction Details")
st.dataframe(filtered_df.sort_values(by='risk_score', ascending=False), use_container_width=True)

# Show chart
st.markdown("### 📈 Risk Level Distribution")
st.bar_chart(filtered_df['risk_level'].value_counts())


