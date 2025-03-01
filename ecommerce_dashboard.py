# eCommerce Dashboard - Interactive Version
# This project analyzes and visualizes eCommerce sales data using Streamlit

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Page Title
st.set_page_config(page_title="eCommerce Sales Dashboard", layout="wide")
st.title("📊 eCommerce Sales Dashboard")

# Upload CSV file
uploaded_file = st.file_uploader("Upload a CSV file with sales data", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    df['Date'] = pd.to_datetime(df['Date'])
    
    # Sidebar Date Filter
    st.sidebar.header("Filter Data")
    start_date = st.sidebar.date_input("Start Date", df['Date'].min())
    end_date = st.sidebar.date_input("End Date", df['Date'].max())
    
    df_filtered = df[(df['Date'] >= pd.to_datetime(start_date)) & (df['Date'] <= pd.to_datetime(end_date))]
    
    # KPI Metrics
    total_sales = df_filtered['Sales'].sum()
    avg_sales = df_filtered['Sales'].mean()
    best_day = df_filtered.loc[df_filtered['Sales'].idxmax(), 'Date']
    growth = ((df_filtered['Sales'].iloc[-1] - df_filtered['Sales'].iloc[0]) / df_filtered['Sales'].iloc[0]) * 100
    
    # KPI Display
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("💰 Total Sales", f"€{total_sales:,.0f}")
    col2.metric("📈 Avg Daily Sales", f"€{avg_sales:.2f}")
    col3.metric("🏆 Best Sales Day", best_day.strftime('%Y-%m-%d'))
    col4.metric("📊 Sales Growth", f"{growth:.2f}%")
    
    # Sales Trend Plot
    fig1 = px.line(df_filtered, x='Date', y='Sales', markers=True, title="Sales Trend Over Time")
    st.plotly_chart(fig1, use_container_width=True)
    
    # Sales Distribution
    fig2, ax = plt.subplots()
    sns.histplot(df_filtered['Sales'], kde=True, color="blue", alpha=0.5, ax=ax)
    ax.set_title("Sales Distribution")
    st.pyplot(fig2)
    
    # Display filtered data
    st.subheader("Filtered Data Preview")
    st.dataframe(df_filtered)
else:
    st.info("Please upload a CSV file to analyze the sales data.")
