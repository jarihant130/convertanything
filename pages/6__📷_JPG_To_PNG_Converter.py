import streamlit as st
from PIL import Image
from io import BytesIO
import base64

def jpg2png():
    st.set_page_config(page_title="JPG to PNG Converter!!", page_icon=":camera:", layout="wide")
    st.title("JPG to PNG Converter :camera:")
    st.write("This Streamlit application allows you to convert your JPG image to PNG format. Upload your image and enter the desired output file name. The application will display the image and provide a download button to save the converted image as a PNG file. The application uses the PIL library to convert the uploaded image to PNG format and the io and base64 libraries to handle the file conversion and download.")
    
    # Upload the image
    uploaded_file = st.file_uploader("Choose an image", type=["jpg"])
    
    if uploaded_file is not None:
        output_file = st.text_input("Output file name", "output.png")
        # Convert the uploaded file to a PIL Image object
        image = Image.open(uploaded_file)
        
        # Add a "Download" button to allow the user to download the cropped image
        with BytesIO() as output:
            image.save(output, format='PNG')
            b64 = base64.b64encode(output.getvalue()).decode()
            href = f'<a href="data:application/octet-stream;base64,{b64}" download={output_file}>Download Image</a>'
            st.markdown(href, unsafe_allow_html=True)
    else:
        st.warning("Please upload an image file first!")

if __name__ == '__main__':
    jpg2png()
