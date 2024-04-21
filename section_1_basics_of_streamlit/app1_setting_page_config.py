# First thing is to setup the app config

import streamlit as st 
from PIL import Image

#img = Image.open("someimage.png")

# First way --------------------------------
# st.set_page_config(page_title = "homepage",
#                    page_icon = ":smiley:",
#                    # For image :  page_icon = img 
#                    layout = "wide",
#                    initial_sidebar_state = "auto" #"collapsed"
#                    )

# Second Way  --------------------------------
PAGE_CONFIG = {
    "page_title": "homepage_second_way",
    "page_icon": ":smiley:",
    "layout": "centered"
}
st.set_page_config(**PAGE_CONFIG)

def main():
    st.title("Streamlit : Setting up the app configuration")
    st.sidebar.success("Menu")
    
    
if __name__ == "__main__":
    main()