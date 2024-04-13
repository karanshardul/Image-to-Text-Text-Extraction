#Image to Text


import streamlit as st
from pytesseract import pytesseract 
from PIL import Image
import os


filename = st.file_uploader('Upload a image')
if filename is not None:   


    if filename.endswith(".jpeg") or filename.endswith(".png"):  # Check for image extensions
        
            # Open the image
            raw_image = filename

            text = pytesseract.image_to_string(raw_image)

            st.write(text)

 


