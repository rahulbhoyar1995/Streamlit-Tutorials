import streamlit as st
import matplotlib.pyplot as plt
import matplotlib 

import pandas as pd
import numpy as np
matplotlib.use("Agg")
import seaborn as sns
import altair as alt


def main():
    st.title("Plotting with the Pyplot")
    df = pd.read_csv("data/iris.csv")
    df2 = pd.read_csv("data/lang_data.csv")
    st.dataframe(df.head())

    #Type 1 : Bar chart 
    st.bar_chart(df["sepal_length"])

    #Type 2 : bar chart
    st.bar_chart(df[["sepal_length","petal_length"]])

    #Type 3 :Line Chart
    lang_list = df2.columns.tolist()
    lang_choices = st.multiselect("Choose Language",lang_list, default = "Python")
    new_df = df2[lang_choices]
    st.line_chart(new_df)

    # Area charts
    st.area_chart(new_df,use_container_width = True)
    
    # Create an Altair chart
    # Create some example data
    data = pd.DataFrame({
        'Category': ['A', 'B', 'C', 'D', 'E'],
        'Value': [20, 35, 30, 35, 27]
    })

    chart = alt.Chart(data).mark_circle().encode(
        x='Category',
        y='Value'
    ).properties(
        title='Example Bar Chart'
    )

    # Streamlit app
    st.title('Altair Chart Example')

    st.write("This is an example of an Altair bar chart created using Streamlit and Python.")
    st.altair_chart(chart, use_container_width = True)

if __name__ == "__main__":
    main()