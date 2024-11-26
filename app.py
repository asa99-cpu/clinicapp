import streamlit as st
import pandas as pd

# Sample data representing clinic patient information
data = {
    'Patient ID': [1, 2, 3, 4, 5],
    'Name': ['John Doe', 'Jane Smith', 'Sam Brown', 'Alice Green', 'Mike Johnson'],
    'Age': [34, 28, 45, 50, 33],
    'Appointment Date': ['2024-11-26', '2024-11-25', '2024-11-24', '2024-11-23', '2024-11-22'],
    'Visit Type': ['Routine Checkup', 'Consultation', 'Follow-up', 'Routine Checkup', 'Emergency']
}

# Convert to DataFrame for easy visualization
df = pd.DataFrame(data)

# Set up the title and layout
st.title('Clinic Data Dashboard')
st.markdown('### Overview of patients and appointments')

# Display the table
st.dataframe(df)

# Adding some simple interactive features
st.sidebar.header('Filter Data')

# Filter by age range
age_filter = st.sidebar.slider('Select age range', 20, 60, (20, 60))
filtered_data = df[(df['Age'] >= age_filter[0]) & (df['Age'] <= age_filter[1])]

st.subheader('Filtered Patient Data')
st.dataframe(filtered_data)

# Displaying statistics
st.subheader('Basic Statistics')
st.write(f"Total Patients: {len(df)}")
st.write(f"Average Age: {df['Age'].mean():.2f}")

# Create a pie chart for 'Visit Type' distribution
st.subheader('Visit Type Distribution')
visit_type_count = df['Visit Type'].value_counts()
st.write(visit_type_count)
st.bar_chart(visit_type_count)
