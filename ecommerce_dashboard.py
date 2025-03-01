# eCommerce Dashboard - Interactive Version
# This project analyzes and visualizes eCommerce sales data using Streamlit

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Streamlit page configuration
st.set_page_config(page_title="eCommerce Dashboard", layout="wide")

# Title
st.title("📊 eCommerce Sales Dashboard")

# File uploader
uploaded_file = st.file_uploader("Upload a CSV file with sales data", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file, parse_dates=["Date"])
else:
    # Sample sales data (for demo purposes)
    data = {
        'Date': pd.date_range(start='2024-01-01', periods=10, freq='D'),
        'Sales': [150, 200, 250, 180, 220, 300, 280, 260, 310, 400]
    }
    df = pd.DataFrame(data)

# Display dataframe
st.write("### Sales Data Preview", df.head())

# Calculate key performance indicators (KPIs)
average_sales = df['Sales'].mean()
max_sales = df['Sales'].max()
best_day = df[df['Sales'] == max_sales]['Date'].values[0]

total_sales = df['Sales'].sum()
num_days = df.shape[0]

# Display KPIs
st.write("### Key Performance Indicators")
st.metric(label="📈 Total Sales", value=f"€{total_sales:,}")
st.metric(label="📊 Average Daily Sales", value=f"€{average_sales:.2f}")
st.metric(label="🏆 Best Sales Day", value=best_day.strftime('%Y-%m-%d'))

# Sales trend visualization
st.write("### Sales Trend Over Time")
fig, ax = plt.subplots(figsize=(10, 5))
sns.lineplot(x='Date', y='Sales', data=df, marker='o', linewidth=2, ax=ax)
ax.set_xlabel("Date")
ax.set_ylabel("Sales (€)")
ax.set_title("Sales Trend")
ax.grid(True)
st.pyplot(fig)

# Sales distribution
st.write("### Sales Distribution")
fig, ax = plt.subplots(figsize=(8, 5))
sns.histplot(df['Sales'], bins=5, kde=True, color='blue', ax=ax)
ax.set_xlabel("Sales (€)")
ax.set_ylabel("Frequency")
ax.set_title("Sales Distribution")
st.pyplot(fig)

st.write("---")
st.write("💡 Upload your own CSV file to analyze real sales data!")
