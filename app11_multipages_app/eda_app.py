import streamlit as st 
import pandas as pd
# Load EDA Pkgs

def run_eda_app():
	st.subheader("From Exploratory Data Analysis")
	df = pd.read_csv("iris.csv")
	st.dataframe(df)