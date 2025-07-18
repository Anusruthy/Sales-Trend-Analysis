# -*- coding: utf-8 -*-
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Sales Trend Analyzer", layout="wide")
st.title("📊 Sales Trend Analysis Dashboard")

# Auto-load cleaned dataset
df = pd.read_csv("cleaned_sales_data.csv")

# Clean + preprocess
df.dropna(inplace=True)
df['Order Date'] = pd.to_datetime(df['Order Date'], errors='coerce')
df.dropna(subset=['Order Date'], inplace=True)
df['Sales'] = df['Quantity Ordered'] * df['Price Each']
df['Month'] = df['Order Date'].dt.month

# Sidebar Filters
with st.sidebar:
    st.title("Filters")

    product_filter = st.multiselect(
        "Select Product(s):",
        options=df['Product'].unique(),
        default=df['Product'].unique()
    )

    month_filter = st.multiselect(
        "Select Month(s):",
        options=sorted(df['Month'].unique()),
        default=sorted(df['Month'].unique())
    )

# Apply filters
filtered_df = df[
    (df['Product'].isin(product_filter)) &
    (df['Month'].isin(month_filter))
]

# Show filtered data
st.subheader(" Filtered Dataset Preview")
st.dataframe(filtered_df.head())

# Sales trend
st.subheader(" Sales Over Time")
sales_by_date = filtered_df.groupby(filtered_df['Order Date'].dt.date)['Sales'].sum().reset_index()
fig1 = px.line(sales_by_date, x='Order Date', y='Sales', title="Sales Trend (Filtered)")
st.plotly_chart(fig1, use_container_width=True)

# KPIs
st.subheader("📌 Key Metrics")
total_sales = filtered_df['Sales'].sum()
top_product = filtered_df.groupby('Product')['Sales'].sum().idxmax()

col1, col2 = st.columns(2)
col1.metric("Total Sales", f"₹ {total_sales:,.2f}")
col2.metric("Top Selling Product", top_product)

# Top 5 Products
st.subheader("Top 5 Products by Sales")
top_products = filtered_df.groupby('Product')['Sales'].sum().sort_values(ascending=False).head(5)
fig2 = px.bar(top_products, x=top_products.index, y=top_products.values,
              labels={'x': 'Product', 'y': 'Sales'}, title="Top 5 Products")
st.plotly_chart(fig2, use_container_width=True)
