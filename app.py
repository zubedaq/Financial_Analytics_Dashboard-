
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

st.title("💰 Financial Analytics Dashboard")

# Upload file
uploaded_file = st.file_uploader("Upload your Excel file", type=["xlsx"])

if uploaded_file:
    df = pd.read_excel(uploaded_file)

    df['Date'] = pd.to_datetime(df['Date'])
    df['Month'] = df['Date'].dt.to_period('M')

    st.subheader("📊 Raw Data")
    st.write(df)

    # KPIs
    total = df['Amount ($)'].sum()
    avg = df['Amount ($)'].mean()

    st.subheader("📌 KPIs")
    st.write(f"Total Spending: {total}")
    st.write(f"Average Spending: {avg:.2f}")

    # Category chart
    category = df.groupby('Category')['Amount ($)'].sum()

    st.subheader("📊 Category-wise Spending")
    fig1, ax1 = plt.subplots()
    category.plot(kind='bar', ax=ax1)
    st.pyplot(fig1)

    # Monthly trend
    monthly = df.groupby('Month')['Amount ($)'].sum()

    st.subheader("📈 Monthly Trend")
    fig2, ax2 = plt.subplots()
    monthly.plot(marker='o', ax=ax2)
    st.pyplot(fig2)
