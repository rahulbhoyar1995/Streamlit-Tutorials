# filename : Multiple files uploads 

import streamlit as st 
from PIL import Image
from pathlib import Path


def create_directory():
    data_saved_folder = Path("data_saved")
    if not data_saved_folder.exists():
        data_saved_folder.mkdir()

# Load Images
@st.cache_data
def load_image(image_file):
	img = Image.open(image_file)
	return img

def save_uploaded_file(uploadedFile):
    create_directory()
    file_path = Path("data_saved") / uploadedFile.name
    with open(file_path, "wb") as f:
        f.write(uploadedFile.read())
    st.success(f"File Saved.")
    
    
import streamlit as st

def main():
    st.title("Multiple File Upload Tutorial using Streamlit")
    menu = ["Image Files", "About"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Image Files":
        st.subheader("Upload the multiple files")
        uploaded_files = st.file_uploader("Upload Image Files", type=["png", "jpg", "jpeg"], accept_multiple_files = True)
        if uploaded_files is not None:
            for image_file in uploaded_files:
                # To see details
                file_details = {
                    "filename": image_file.name,
                    "filetype": image_file.type,
                    "filesize": image_file.size
                }
                st.write(file_details)
                st.image(load_image(image_file), caption=image_file.name, width=250)
                save_uploaded_file(image_file)
                # save_uploaded_file(image_file) # Function definition not provided
                # You may define a function to save the uploaded files
    else:
         st.subheader("This is the about section.")
if __name__ == '__main__':
	main()
    

