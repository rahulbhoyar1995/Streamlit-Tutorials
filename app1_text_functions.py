# Basic Text functions

# Core packages
import streamlit as st 

# Additional packages

#Functions
def main():
    """ All code goes"""
    
    # Text
    st.title("Streamlit App Info")
    st.header("India")
    st.subheader("Australia")
    st.markdown("New Zealand")
    
    st.text("This is Rahul Bhoyar's test page")
    country = "India"
    st.text(f"{country} is my favourite country.")
    
    # Colourful bootstrap
    st.success("This is success.")
    st.warning("This is the warning.")
    st.info("This is the information.")
    st.error("This is the error")
    st.exception("This is the exception.")
    
    # Superfunction
    st.write("This is the normal text line")
    st.write("## This is the HTML/Markdown code")
    st.write(60+20)
    st.write(dir(st))
    
    # Help Info
    st.help(range)
    
if __name__ == "__main__":
    main()