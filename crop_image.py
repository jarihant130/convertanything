import streamlit as st
from PIL import Image
import io
from io import BytesIO
import base64

def crop_image():
    st.subheader("Welcome to Image Cropper!")
    st.write("This is a simple application that crops an image.")
    # Allow the user to upload an image
    uploaded_file = st.file_uploader("Choose an image file", type=["jpg", "jpeg", "png"])
    
    # If the user has uploaded a file, display it and allow them to crop it
    try:
        if uploaded_file is not None:
            # Load the image using PIL
            image = Image.open(uploaded_file)

            # Get the dimensions of the image
            width, height = image.size

            # Get the user's input for the crop dimensions
            crop_left = st.slider("Left edge of crop", 0, width, 0)
            crop_top = st.slider("Top edge of crop", 0, height, 0)
            crop_right = st.slider("Right edge of crop", 0, width, width)
            crop_bottom = st.slider("Bottom edge of crop", 0, height, height)

            # Get the user's input for the rotation angle
            rotate_degrees = st.slider("Rotation (degrees)", -180, 180, 0, step = 90)

            # Rotate the image using PIL
            rotated_image = image.rotate(rotate_degrees, expand=True)

            # Crop the image using PIL
            cropped_image = rotated_image.crop((crop_left, crop_top, crop_right, crop_bottom))

            # Display the cropped image to the user
            st.image(cropped_image)

            # Add a "Download" button to allow the user to download the cropped image
            with io.BytesIO() as output:
                cropped_image.save(output, format='JPEG')
                b64 = base64.b64encode(output.getvalue()).decode()
                href = f'<a href="data:application/octet-stream;base64,{b64}" download="cropped_image.jpeg">Download Image</a>'
                st.markdown(href, unsafe_allow_html=True)
        
        else:
            st.warning("Please upload an image file first!")
    except Exception as e:
            st.error(f"Error: {e}")