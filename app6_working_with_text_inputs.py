# Working with Text input files
import streamlit as st

def main():
    st.title("Streamlit : Working with Text Inputs")
    
    #  Text Input
    fname = st.text_input("Enter the first name :")
    st.write(fname)
    
    # Password Input
    password = st.text_input("Enter your password :", type = "password")
    st.write(password)
    
    # Text Area
    message = st.text_area("Enter the message :", height = 100)
    st.write(message)
    
    # Numbers
    number = st.number_input("Enter the number :", 1,5)
    
    # Date Input
    my_appointment = st.date_input("Appointment")
    
    # Time
    my_time = st.time_input("My Time")
    
if __name__ == "__main__":
    main()