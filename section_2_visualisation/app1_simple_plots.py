import streamlit as st
import matplotlib.pyplot as plt
import matplotlib 

import pandas as pd
import numpy as np
matplotlib.use("Agg")
import seaborn as sns



def main():
    st.title("Plotting with the Pyplot")
    df = pd.read_csv("data/iris.csv")
    st.dataframe(df.head())
    
    # # Method 1
    fig, ax = plt.subplots()
    ax.scatter(*np.random.random(size=(2,100)))

   # Method 2
    fig = plt.figure()
    df["species"].value_counts().plot(kind="bar")
    st.pyplot(fig)

    # Method 3
    # fig = plt.subplots()
    # df["species"].value_counts().plot(kind="bar")
    # st.pyplot(fig)
    
   

if __name__ == "__main__":
    main()