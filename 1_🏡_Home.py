import streamlit as st
from PIL import Image
def home():
    try:
        st.subheader("Convert Anything From Here!!")
        st.write("Please select available options from the menu to get started.")

        # Load image from file
        image = Image.open("convert_anything.jpg")

        # Display image on Streamlit app
        st.image(image, caption="Convert Anything")
    except Exception as e:
        st.error(f"Error: {e}")
