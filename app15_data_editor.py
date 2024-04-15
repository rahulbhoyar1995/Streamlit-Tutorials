
# Streamlit Data Editor

import streamlit as st 
import pandas as pd 
import time 
timestr = time.strftime("%Y%m%d-%H%M%S")



# Load Data Fxn
def load_data(data):
    return pd.read_csv(data)

def main():
    st.title("Streamlit Data Editor App")

    menu = ["Home", "About"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.subheader("Home")
        data_file = st.file_uploader("Upload CSV",type=["csv"])
        if data_file is not None:
            df = load_data(data_file)
            # Saving Form
            with st.form("editor_form"):
                edited_df = st.data_editor(df)
                save_button = st.form_submit_button("Save Data")
               
            if save_button:
                new_filename = f"{data_file.name}_{timestr}.csv"
                final_df = edited_df.to_csv()

                st.download_button(label="Download data as CSV",data=final_df,file_name=new_filename,
                                   mime='text/csv')
    
    
    else:
        st.subheader("About")

    
if __name__ == "__main__":
    main()