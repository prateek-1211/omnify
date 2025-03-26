import streamlit as st
import pandas as pd
import plotly.express as px

# Load the dataset
file_path = "DataAnalyst_Assesment_Dataset.xlsx"
df = pd.read_excel(file_path, sheet_name="Large_Fake_Bookings_With_Discre")

df['Booking Date'] = pd.to_datetime(df['Booking Date'])

# Sidebar Filters
st.sidebar.header("Filter Options")
booking_status = st.sidebar.multiselect("Select Booking Status", df['Status'].unique(), default=df['Status'].unique())
df_filtered = df[df['Status'].isin(booking_status)]

# Main Dashboard
st.title("Booking Analysis Dashboard")

# KPI Metrics
st.subheader("Key Metrics")
col1, col2, col3 = st.columns(3)
col1.metric("Total Bookings", len(df_filtered))
col2.metric("Total Revenue", f"${df_filtered['Price'].sum():,.2f}")
col3.metric("Average Booking Price", f"${df_filtered['Price'].mean():,.2f}")

# Booking Type Distribution
st.subheader("Booking Type Distribution")
fig1 = px.pie(df_filtered, names='Booking Type', title='Distribution of Booking Types')
st.plotly_chart(fig1)

# Facility Usage
st.subheader("Facility Usage")
fig2 = px.bar(df_filtered.dropna(subset=['Facility']), x='Facility', title='Bookings per Facility')
st.plotly_chart(fig2)

# Time Slot Popularity
st.subheader("Time Slot Popularity")
df_filtered['Hour'] = pd.to_datetime(df_filtered['Time Slot'], errors='coerce').dt.hour
time_counts = df_filtered['Hour'].value_counts().reset_index()
time_counts.columns = ['Hour', 'Count']
fig3 = px.bar(time_counts, x='Hour', y='Count', title='Popular Booking Hours')
st.plotly_chart(fig3)

# Booking Trends Over Time
st.subheader("Booking Trends Over Time")
df_date = df_filtered.groupby(df_filtered['Booking Date'].dt.to_period('M')).size().reset_index()
df_date.columns = ['Month', 'Count']
df_date['Month'] = df_date['Month'].astype(str)  # Convert Period to string
fig4 = px.line(df_date, x='Month', y='Count', title='Monthly Booking Trends')
st.plotly_chart(fig4)