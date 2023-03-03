import cv2
import streamlit as st
from PIL import Image
import numpy as np
from io import BytesIO
import base64

def converter(image, ksize, sigma):
    # Convert to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Invert the image
    inverted_image = 255 - gray_image

    # Apply a Gaussian blur to the inverted image
    blurred_image = cv2.GaussianBlur(inverted_image, ksize, sigma)

    # Blend the grayscale image with the blurred inverted image using the "color dodge" blend mode
    sketch_image = cv2.divide(gray_image, 255 - blurred_image, scale=256)

    return sketch_image

def image2sketch():
    st.set_page_config(page_title="Image to Sketch Converter!!", page_icon=":camera:", layout="wide")
    # add a title to the app
    st.title('Convert Image to Sketch :camera:')
    st.subheader("Welcome to Image to Sketch Converter!")
    st.write("This is a simple application that converts an image to a pencil sketch using OpenCV.")

    # Upload the image
    uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])

    # Display the image as a button
    if uploaded_file is not None:
        # Code to convert image to sketch goes here
        image = Image.open(uploaded_file)
        st.image(image, caption="Original Image", use_column_width=True)

        # Convert the PIL image to a NumPy array for OpenCV processing
        img_np = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

        # Get the kernel size and sigma from the user
        ksize = st.slider("Kernel size", 1, 551, 251, step=21)
        sigma = st.slider("Sigma", 1, 1001, 0)

        # Convert the image to a sketch
        sketch_image = converter(img_np, (ksize, ksize), sigma)

        # Convert the sketch image back to a PIL image for display
        sketch_image_pil = Image.fromarray(sketch_image)

        # Show the sketch image
        st.image(sketch_image_pil, caption="Sketch Image", use_column_width=True)
        output_file = st.text_input("Output file name", "output.png")

        # Save the sketch image as a PNG file
        
        # Add a "Download" button to allow the user to download the cropped image
        with BytesIO() as output:
            sketch_image_pil.save(output, format='PNG')
            b64 = base64.b64encode(output.getvalue()).decode()
            href = f'<a href="data:application/octet-stream;base64,{b64}" download={output_file}>Download Image</a>'
            st.markdown(href, unsafe_allow_html=True)

    else:
        st.warning("Please click the image to convert it to a sketch.")
if __name__ == '__main__':
    image2sketch()            