# Widgets

# Core packages
import streamlit as st 

# Additional packages
# Buttons / Radio / Checkbox / Select
#Functions
def main():
    # Text
    st.title("Streamlit Widgets")
    
    # Buttons
    name = "Rahul is practising Streamlit."
    
    if st.button("Submit"):
        st.write(f"Name: {name}")
        
    if st.button("Submit", key="new02"):
        st.write(f"First Name: {name.lower()}")
        
    # Radio Buttons
    status = st.radio("What is your status ?",("Active","Inactive"))
    if status == "Active":
        st.success("User is active.") 
    elif status == "Inactive":
        st.warning("User is Inactive.") 
    
    # Checkboxes
    if st.checkbox("Show/Hide"):
        st.text("Show me something with this")
        for i in dir(st):
             st.text(i)
            
        
    # Working with  Expander
    with st.expander("See explanation"):
        st.write("""
            The chart above shows some numbers I picked for you.
            I rolled actual dice for these, so they're *guaranteed* to
            be random.
        """)
        st.image("https://static.streamlit.io/examples/dice.jpg")
        
        
    # Select or Multiple Select
    my_languages = ["Python","Golang","Java","C++"]
    choice = st.selectbox("Language", my_languages)
    st.write("You selected {}".format(choice))
    
    #Multiple Select
    spoken_languages = ["English","Spanish","French","Hindi"]
    my_spoken_lang = st.multiselect("Spoken Languages :",spoken_languages, default="English")
    
    # Slider
    # Numbers (Int/Float/Dates)
    age = st.slider("Age", 1, 100)
    
    # Select Slider
    colour = st.select_slider("Choose your favourite colour",options = ["Yellow","Red","Green","Blue","Black","White"], value=("Yellow","Red"))
    
if __name__ == "__main__":
    main()