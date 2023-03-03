import img2pdf
import streamlit as st

# Function to convert image to pdf 
def image_to_pdf():

    """Convert an image file to a PDF file."""
    st.set_page_config(page_title="Convert Image To PDF!!", page_icon=":camera:", layout="wide")
    st.title("Convert Image To PDF:camera:")
    st.subheader("Welcome to Image To PDF Converter!")
    st.write("This is a simple application that converts an image file to PDF.")

    try:
        # File uploader
        uploaded_file = st.file_uploader("Upload an Image", type=["jpg", "jpeg", "png"])

        if uploaded_file is not None:
            # Ask user for output file name
            output_file_name = st.text_input("Output file name", "output.pdf")

            if st.button("Convert to PDF"):
                with open(output_file_name, 'wb') as out:
                    out.write(img2pdf.convert(uploaded_file))
                st.success("Your PDF file has been created successfully!")
                
                try:
                    with open(output_file_name, 'rb') as f:
                        bytes_data = f.read()
                        st.download_button(
                            label="Download PDF",
                            data=bytes_data,
                            file_name=output_file_name
                        )
                except FileNotFoundError:
                    st.warning("PDF file not found. Please convert your image to PDF first.")
                          
        else:
            st.warning("Please upload an image file first!")
                          
    except Exception as e:
        st.error(f"Error: {e}")
        
if __name__ == '__main__':
    image_to_pdf()