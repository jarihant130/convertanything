import streamlit as st
from PIL import Image
import os
from io import BytesIO
import base64

def image_resizer():
    st.set_page_config(page_title="Image Resizer!!", page_icon=":camera:", layout="wide")
    # add a title to the app
    st.title('Image Resizer!:camera:')
    # Set page header
    st.subheader("Welcome to Image Resizer!")
    st.write("This is a simple application that resize an image.")
    try:
        # Allow user to upload an image file
        uploaded_file = st.file_uploader("Choose an image file", type=["jpg", "jpeg", "png"])

        # If the user has uploaded a file and provided resizing options, process it
        if uploaded_file is not None:
            img = Image.open(uploaded_file)
            width, height = img.size

            # Get user input for the desired output size and filename
            width_input = st.number_input("Enter the desired width in pixels", value=width)
            height_input = st.number_input("Enter the desired height in pixels", value=height)
            output_filename = st.text_input("Enter the desired output filename", value="resized_image")

            if width_input and height_input and output_filename:
                # Open the image and resize it
                img = img.resize((int(width_input), int(height_input)))

                # Convert to RGB mode if necessary
                if img.mode not in ('L', 'RGB'):
                    img = img.convert('RGB')

                # Save the resized image with the user-specified filename and extension
                filename, extension = os.path.splitext(uploaded_file.name)
                output_filename = output_filename + extension
#                 img.save(output_filename)

                # Display the resized image
                st.image(img, caption="Resized Image", use_column_width=True)
                # Add a "Download" button to allow the user to download the cropped image
                with BytesIO() as output:
                    img.save(output, format=extension[1:])
                    b64 = base64.b64encode(output.getvalue()).decode()
                    href = f'<a href="data:application/octet-stream;base64,{b64}" download={output_filename}>Download Image</a>'
                    st.markdown(href, unsafe_allow_html=True)

            else:
                st.warning("Please upload the image to resize it.")

            # Create a download button for the resized image file
            if os.path.isfile(output_filename):
                with open(output_filename, 'rb') as f:
                    bytes_data = f.read()
                st.download_button(
                    label="Download Resized Image",
                    data=bytes_data,
                    file_name=output_filename,
                    mime="image/jpeg"
                )

        else:
            st.warning("Please upload the image to resize it.")

    except Exception as e:
        st.error(f"Error: {e}")
if __name__ == '__main__':
    image_resizer()  