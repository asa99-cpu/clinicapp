import streamlit as st
import pandas as pd
import numpy as np

# Sample data for demonstration
data = {
    'Client ID': [1, 2, 3, 4, 5],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [30, 45, 35, 50, 40],
    'Appointment Date': pd.to_datetime(['2024-12-01', '2024-12-03', '2024-12-05', '2024-12-10', '2024-12-15']),
    'Status': ['Completed', 'Scheduled', 'Completed', 'Scheduled', 'Missed']
}

# Create a DataFrame
df = pd.DataFrame(data)

# App title and introduction
st.title("Clinic Client Dashboard")
st.write("""
Welcome to the Clinic Client Dashboard! This dashboard provides a simple view of client information, appointments, and general statistics.
""")

# Display a summary of client statistics
st.header("Client Statistics")
total_clients = len(df)
completed_appointments = df[df['Status'] == 'Completed'].shape[0]
scheduled_appointments = df[df['Status'] == 'Scheduled'].shape[0]
missed_appointments = df[df['Status'] == 'Missed'].shape[0]

st.write(f"Total Clients: {total_clients}")
st.write(f"Completed Appointments: {completed_appointments}")
st.write(f"Scheduled Appointments: {scheduled_appointments}")
st.write(f"Missed Appointments: {missed_appointments}")

# Displaying the table of client information
st.subheader("Client Information")
st.dataframe(df)

# Filter the data by appointment status (Completed, Scheduled, Missed)
status_filter = st.selectbox("Filter by Appointment Status", ['All', 'Completed', 'Scheduled', 'Missed'])

if status_filter != 'All':
    filtered_df = df[df['Status'] == status_filter]
else:
    filtered_df = df

st.write(f"Clients with {status_filter} appointments:")
st.dataframe(filtered_df)

# Visualization: Appointments over time
st.subheader("Appointments Over Time")
appointments_count = df.groupby(df['Appointment Date'].dt.date).size()
st.line_chart(appointments_count)

# Simple status summary for the clinic
st.subheader("Appointment Status Summary")
status_counts = df['Status'].value_counts()
st.bar_chart(status_counts)

# Footer
st.markdown("---")
st.write("Dashboard powered by Streamlit")
