import streamlit as st
from PIL import Image
from io import BytesIO
import base64

def rotate_image():
    st.set_page_config(page_title="Image Rotator!!", page_icon=":camera:", layout="wide")
    # Rotate the image
    # add a title to the app
    st.title('Image Rotator:camera:')
    st.subheader("Welcome to Image Rotator!")
    st.write("This is a simple application that rotates an image by the specified angle.")

    # Upload the image
    uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])
    angle = st.slider("Angle", -180, 180, 0, step=10)
        
    # Display the image as a button
    if uploaded_file is not None:
        # Convert the uploaded file to a PIL Image object
        image = Image.open(uploaded_file)

        # Rotate the image
        rotated_image = image.rotate(angle, resample=Image.BICUBIC, expand=True)

        # Show the rotated image
        st.image(rotated_image, caption="Rotated Image", use_column_width=True)
        output_file_name = "rotated_" + uploaded_file.name + ".png"

        # Add a "Download" button to allow the user to download the cropped image
        with BytesIO() as output:
            rotated_image.save(output, format='PNG')
            b64 = base64.b64encode(output.getvalue()).decode()
            href = f'<a href="data:application/octet-stream;base64,{b64}" download="rotated_image.png">Download Image</a>'
            st.markdown(href, unsafe_allow_html=True)
    
    else:
        st.warning("Please upload an image file first!")
if __name__ == '__main__':
    rotate_image()