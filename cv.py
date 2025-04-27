import streamlit as st
import cv2
import numpy as np
from PIL import Image
st.title("Image Resizer")
uploaded_file = st.file_uploader("Choose an image...", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    image = np.array(image)
    st.image(image, caption="Uploaded Image", use_container_width=True)
   
    width = st.number_input("Enter width:", min_value=1, value=image.shape[1])
    height = st.number_input("Enter height:", min_value=1, value=image.shape[0])
    resized_image = cv2.resize(image, (width, height))
    st.image(resized_image, caption="Resized Image", use_container_width=True)
    result_image = Image.fromarray(resized_image)
    with open("resized_image.jpg", "rb") as file:
        st.download_button("Download Resized Image", file, "resized_image.jpg")
