import streamlit as st
import os
import comtypes.client

# Function to convert docx to pdf
def convert_to_pdf(docx_file_path, pdf_file_path):
    try:
        # Initialize COM library
        comtypes.CoInitialize()

        # Open an instance of Word
        word = comtypes.client.CreateObject('Word.Application')
        word.Visible = False  # Hide the Word window

        # Open the docx file
        docx_file = os.path.abspath(docx_file_path)
        doc = word.Documents.Open(docx_file)

        # Save the file as pdf
        pdf_file = os.path.abspath(pdf_file_path)
        doc.SaveAs(pdf_file, FileFormat=17)  # FileFormat=17 for PDF format

        # Close the docx file and the Word instance
        doc.Close()
        word.Quit()

        # Uninitialize COM library
        comtypes.CoUninitialize()
    except Exception as e:
        st.error(f"Error: {e}")

# Function to convert docx to pdf
def word2pdf():
    st.title("Convert Word to PDF")
    st.subheader("Welcome to Word Document to PDF Converter!")
    st.write("This is a simple application that convert word document to PDF.")
    try:
        # File uploader
        uploaded_file = st.file_uploader("Upload a Word document", type=["docx"])

        if uploaded_file is not None:
            # Ask user for output file name
            output_file_name = st.text_input("Output file name", "output.pdf")

            if st.button("Convert to PDF"):
                # Convert Word to PDF
                convert_to_pdf(uploaded_file.name, output_file_name)

                # Show success message
                st.success("Conversion successful!")

                if st.button("Download PDF"):
                    # Download link for the PDF file
                    with open(output_file_name, "rb") as f:
                        bytes = f.read()
                        st.download_button(label="Download PDF", data=bytes, file_name=output_file_name)
                # Show download success message
                st.success("Your PDF file has been downloaded successful!")

        else:
            st.warning("Please upload a word document file")            
    except Exception as e:
        st.error(f"Error: {e}")
