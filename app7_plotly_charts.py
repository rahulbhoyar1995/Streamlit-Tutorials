# Basic Text Display functions

# Core packages
import streamlit as st 

# Additional packages
import pandas as pd 
import numpy as np 
import plotly.express as px
#Functions
def main():
    """ All code goes"""
    
    # Text
    st.title("Plotting In Streamlit with Plotly")
    df = pd.read_csv("data/prog_languages_data.csv")
    st.dataframe(df)
    
    # Pie Chart
    fig1 = px.pie(df,values="Sum", names = "lang",title="Pie Chart of Programming Languages")
    st.plotly_chart(fig1)    
    
    # Bar chart
    fig2 = px.bar(df, x ="lang", y = "Sum",title="Bar Chart of Programming Languages :")
    st.plotly_chart(fig2) 
    
    
if __name__ == "__main__":
    main()