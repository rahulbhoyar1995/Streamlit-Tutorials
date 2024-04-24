import streamlit as st
import pandas as pd
import plotly.express as px

def main():
    st.title("Plotting in Streamlit with Plotly")
    df = pd.read_csv("data/prog_languages_data.csv")
    st.dataframe(df)

    # Pie chart
    fig = px.pie(df, values = "Sum",names ="lang", title ="Programming Languages Data - Pie Chart")
    st.plotly_chart(fig)
    
    # Bar chart
    fig2 = px.bar(df, x="lang", y ="Sum",title ="Programming Languages Data - Bar Chart")
    st.plotly_chart(fig2)

if __name__ == "__main__":
    main()