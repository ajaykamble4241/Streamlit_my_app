import streamlit as st
import pandas as pd
from datetime import datetime

# Title
st.title("Reporting Automation")

input_text = st.text_input("Enter the Associate Name(First, Last)")
input_text1 = st.text_input("Enter the Email ID")
input_text2 = st.text_input("Enter the Project")
input_text3 = st.text_input("Enter the Allocation(%)")
input_text4 = st.text_input("Enter the Ticket Reference Number")

# Streamlit app title
st.title('Calculate Monthly Sum of Weekly Data')



# Sidebar inputs
st.sidebar.header("Input Week Options")
end_date = st.sidebar.date_input('Select week date', datetime.now())
weekly_data = st.sidebar.number_input('Input Weekly Data:', min_value=0)

# Button to add weekly data
if st.sidebar.button('Add Weekly Data'):
    # Initialize session state DataFrame
    if 'data' not in st.session_state:
        st.session_state.data = pd.DataFrame(columns=['Associate Name(First, Last)', 'Email ID', 'Project', 'Allocation(%)', 'Date', 'Weekly_Data', 'Ticket Reference Number'])

    # Add new data to the DataFrame
    new_data = pd.DataFrame({'Date': [pd.to_datetime(end_date)], 'Weekly_Data': [weekly_data], 'Associate Name(First, Last)': [input_text], 'Email ID': [input_text1], 'Project':[input_text2], 'Allocation(%)': [input_text3], 'Ticket Reference Number': [input_text4]})
    st.session_state.data = pd.concat([st.session_state.data, new_data], ignore_index=True)


# Main content
st.subheader("Weekly Data")

# Display the DataFrame
if 'data' in st.session_state and not st.session_state.data.empty:
    st.write(st.session_state.data)

    # Ensure 'Date' is datetime
    st.session_state.data['Date'] = pd.to_datetime(st.session_state.data['Date'])

    # Select date range
    st.sidebar.header("Date Range for Monthly Sum")
    start_date = st.sidebar.date_input('Start date', st.session_state.data['Date'].min().date())
    end_date = st.sidebar.date_input('End date', st.session_state.data['Date'].max().date())

    # Convert start_date and end_date to datetime
    start_date = pd.to_datetime(start_date)
    end_date = pd.to_datetime(end_date)

    # Filter DataFrame based on selected date range
    mask = (st.session_state.data['Date'] >= start_date) & (st.session_state.data['Date'] <= end_date)
    filtered_df = st.session_state.data.loc[mask].copy()

    if not filtered_df.empty:
        # Set 'Date' column as index for resampling
        filtered_df.set_index('Date', inplace=True)

        # Calculate monthly sum of weekly data
        monthly_data = filtered_df.resample('M').sum()

        st.subheader("Monthly Sum of Weekly Data")
        st.write(monthly_data)
    else:
        st.write("No data available in the selected date range.")
else:
    st.write("No data available.")

# Button to reset index
if 'data' in st.session_state and not st.session_state.data.empty:
    if st.sidebar.button('Reset Index'):
        st.session_state.data.reset_index(inplace=True)
