import streamlit as st
from PIL import Image

def rotate_image():
    # Rotate the image
#     rotated_image = image.rotate(angle, resample=Image.BICUBIC, expand=True)
    st.subheader("Welcome to Image Rotator!")
    st.write("This is a simple application that rotates an image by the specified angle.")

    # Upload the image
    uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])
    angle = st.slider("Angle", -180, 180, 90, step=10)
        
    # Display the image as a button
    if uploaded_file is not None:
        # Convert the uploaded file to a PIL Image object
        image = Image.open(uploaded_file)

        # Rotate the image
        rotated_image = image.rotate(angle, resample=Image.BICUBIC, expand=True)

        # Show the rotated image
        st.image(rotated_image, caption="Rotated Image", use_column_width=True)

        # Add a button to download the rotated image
        st.download_button(
            label="Download Rotated Image",
            data=rotated_image.tobytes(),
            file_name="rotated.png",
            mime="image/png")
    else:
        st.warning("Please click the image to rotate it.")