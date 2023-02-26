import streamlit as st
from docx2pdf import convert
import PyPDF2
import docx


# Function to convert pdf to docx        
def pdf2word():
    st.title("Convert PDF to WORD")
    st.subheader("Welcome to PDF TO Word Document Converter!")
    st.write("This is a simple application that convert PDF to word document.")

    try:
        # File uploader
        uploaded_file = st.file_uploader("Upload a PDF File", type=["pdf"])

        if uploaded_file is not None:
            # Ask user for output file name
            output_file_name = st.text_input("Output file name", "output.docx")

            if st.button("Convert to Word"):
                if uploaded_file is None:
                    st.warning("Please upload a PDF file first!")
                else:
                    # Open the PDF file
                    pdf_file = uploaded_file
                    pdf_reader = PyPDF2.PdfReader(pdf_file)

                    # Create a Word document
                    doc = docx.Document()

                    # Loop through each page of the PDF file
                    for page_num in range(len(pdf_reader.pages)):
                        page = pdf_reader.pages[page_num]
                        text = page.extract_text()

                        # Add the text to the Word document
                        doc.add_paragraph(text)

                    # Save the Word document
                    doc.save(output_file_name)

                    # Show success message
                    st.success("Conversion successful!")

                    # Create a download button for the converted file
                    with open(output_file_name, 'rb') as f:
                        bytes_data = f.read()
                    st.download_button(
                        label="Download Converted File",
                        data=bytes_data,
                        file_name=output_file_name,
                        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                    )
    except Exception as e:
        st.error(f"Error: {e}")


