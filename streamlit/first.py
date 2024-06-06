# import module
import streamlit as st
import pandas as pd
# Title
st.title("Reporting Automation")

st.sidebar.markdown(""" Dashboard """)
select_event = st.sidebar.selectbox('Operations',
                                    ['Add record', 'Modify Record', 'Delete Record'])

if 'df' not in st.session_state:
    st.session_state.df = pd.DataFrame(columns=['Associate Name(First, Last)', 'Email ID', 'Project', 'Allocation(%)','date_of_week_data', 'Monthly Data', 'Ticket Reference Number'])

input_text = st.text_input("Enter the Associate Name(First, Last)")
input_text1 = st.text_input("Enter the Email ID")
input_text2 = st.text_input("Enter the Project")
input_text3 = st.text_input("Enter the Allocation(%)")
input_text4 = st.text_input("Enter the Weekly Data")
input_date = st.date_input("select the date")
input_date1 = st.text_date("Enter the Monthly Date")
input_text6 = st.text_input("Enter the Ticket Reference Number")



if st.button('Add Record'):
    if input_text:
        # Add the input text to the DataFrame
        new_row = {'Associate Name(First, Last)': input_text, 
                   'Email ID': input_text1,
                   'Project': input_text2,
                   'Allocation(%)': input_text3,
                   'Weekly Data': input_text4,
                   'Date of week': input_date,
                   'Monthly Data': input_date1,
                   'Ticket Reference Number': input_text6
                   }
        st.session_state.df = st.session_state.df.append(new_row, ignore_index=True)
        st.success('Text added to DataFrame!')
    else:
        st.warning('Please enter some text before adding.')

# Display the DataFrame
#st.session_state.second_df = st.session_state.df[['Associate Name(First, Last)', 'Email ID', 'Project', 'Allocation(%)', 'Weekly Data', 'Monthly Data', 'Ticket Reference Number']]
st.subheader('Output:')
st.write(st.session_state.df[['Associate Name(First, Last)', 'Email ID', 'Project', 'Allocation(%)', 'Weekly Data', 'Monthly Data', 'Ticket Reference Number']])
