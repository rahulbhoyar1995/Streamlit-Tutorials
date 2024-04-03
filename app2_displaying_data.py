
# Core packages
import streamlit as st 

# Additional packages
import pandas as pd

#Functions
def main():
    # Text
    st.title("Tabular Data")
    df = pd.read_csv("data/foods.csv").head(50)
    
    # Dataframe
    st.subheader("Pandas Dataframe :")
    #st.dataframe(df) #Default
    st.dataframe(df, 2000, 1000)    # height = 200, width = 100
    
    # Normal Static Table
    st.subheader("Static Table :")
    st.table(df)
    
    # Dataframe with addded feature
    st.subheader("Pandas Dataframe added feature highlighted the maximum values :")
    #st.dataframe(df) #Default
    st.dataframe(df.style.highlight_max(axis = 0)) 
    
    # With write method
    st.subheader("Table with write method :")
    st.write(df)
    
    # Display JSON 
    st.subheader("Displaying the JSON data :")
    json_dict = {"data": "some_name"}
    st.json(json_dict)
    
    # Display Code
    st.subheader("Displaying the code :")
    my_code = """
    def my_function(text):
        return text 
    """
    st.code(my_code, language = "python")
    
if __name__ == "__main__":
    main()