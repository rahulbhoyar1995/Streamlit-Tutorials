
# File name : Restting the streamlit forms 


import streamlit as st 
import streamlit.components as stc

# Utils
import base64 
import time
timestr = time.strftime("%Y%m%d-%H%M%S")



def main():
    st.title("Streamlit Restting forms Tutorial")
    menu = ["Home","About"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.subheader("Forms Tutorial")
        #Method 1 : Context Manager Approach (with)
        with st.form(key="form", clear_on_submit = True):
            firstname = st.text_input("Firstname")
            lastname = st.text_input("Lastname")
            dob = st.date_input("Date of Birth")

            submit_button = st.form_submit_button(label="SignUp")
            # Results can be either form or outside
        if submit_button:
            st.info("Results")
            st.write(f"Hi, {firstname} {lastname}.")
            st.success(f"Hello You have created a successful {firstname}.")

    else:#
        st.subheader("About")

if __name__ == '__main__':
	main()

