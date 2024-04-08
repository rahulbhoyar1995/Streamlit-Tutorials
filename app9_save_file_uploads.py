# Filename : app_save_file_upload.py

# Saving Uploaded file into a Directory in Streamlit
import streamlit as st

# File Processing Pkgs
from PIL import Image
import pandas as pd 
import docx2txt
# import textract
from PyPDF2 import PdfReader
import pdfplumber
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

def read_pdf(pdf_path):
    text = ""
    pdf_reader = PdfReader(pdf_path)
    num_pages = len(pdf_reader.pages)
    for page_num in range(num_pages):
        page = pdf_reader.pages[page_num]
        text += page.extract_text()
    return text

# Function to save the uploaded file
def save_uploaded_file(uploadedFile):
    file_path = Path("data_saved") / uploadedFile.name
    with open(file_path, "wb") as f:
        f.write(uploadedFile.read())
    st.success("File Saved.")
    

def main():
    st.title("File Upload and Saved File to Directory Tutorial using Streamlit")
    menu = ["Image Files", "Dataset", "DocumentFiles", "About"]
    choice = st.sidebar.selectbox("Menu", menu)
    create_directory()
    
    if choice == "Image Files":
        st.subheader("Image Files")
        image_file = st.file_uploader("Upload Images", type=["png", "jpg", "jpeg"])
        if image_file is not None:
            # To see details
            st.write(type(image_file))
            file_details = {
                "filename": image_file.name,
                "filetype": image_file.type,
                "filesize": image_file.size
            }
            st.write(file_details)
            st.image(load_image(image_file), caption=image_file.name, width=250)
            save_uploaded_file(image_file)

    elif choice == "Dataset":
        st.subheader("Dataset")
        data_file = st.file_uploader("Upload CSV", type=["csv"])
        if data_file is not None:
            st.write(type(data_file))
            file_details = {
                "filename": data_file.name,
                "filetype": data_file.type,
                "filesize": data_file.size
            }
            st.write(file_details)
            df = pd.read_csv(data_file)
            st.dataframe(df)
            save_uploaded_file(data_file)
            
    elif choice == "DocumentFiles":
        st.subheader("DocumentFiles")
        docx_file = st.file_uploader("Upload Document", type=["pdf", "docx", "txt"])
        if st.button("Process"):
            if docx_file is not None:
                file_details = {
                    "filename": docx_file.name,
                    "filetype": docx_file.type,
                    "filesize": docx_file.size
                }
                st.write(file_details)
                if docx_file.type == "text/plain":
                    # Read as bytes
                    # raw_text = docx_file.read()
                    # st.write(raw_text) # works but in bytes
                    # st.text(raw_text) # does work as expected

                    # Read as string (decode bytes to string)
                    raw_text = str(docx_file.read(), "utf-8")
                    # st.write(raw_text) # Works
                    st.text(raw_text)  # Work
                    save_uploaded_file(docx_file)
                elif docx_file.type == "application/pdf":
                    # try:
                    #     with pdfplumber.open(docx_file) as pdf:
                    #         pages = pdf.pages[0]
                    #         st.write(pages.extract_text())
                    # except:
                    #     st.write("None")

                    # using PyPDF
                    raw_text = read_pdf(docx_file)
                    st.write(raw_text)
                    save_uploaded_file(docx_file)

                else:
                    raw_text = docx2txt.process(docx_file)
                    st.write(raw_text)  # works
                    # st.text(raw_text)# works
                    save_uploaded_file(docx_file)

    else:
        st.subheader("About")
        
if __name__ == '__main__':
	main()