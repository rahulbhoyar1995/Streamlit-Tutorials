# Structuring the Streamlit App



import streamlit as st 
# And like rhis import many apps

from eda_app import run_eda_app
from ml_app import run_ml_app

def main():
    st.title("Main App")
    
    menu = ["Home", "EDA", "Machine Learning", "About"]
    choice = st.sidebar.selectbox("Menu", menu)
    
    if choice == "Home":
        st.subheader("Home")
        
    if choice == "EDA":
        st.subheader("EDA")
        run_eda_app()
        
    if choice == "Machine Learning":
        st.subheader("Machine Learning")
        st.subheader("Machine Leanring App")
        run_ml_app()
        
        
if __name__ == "__main__":
    main()
        