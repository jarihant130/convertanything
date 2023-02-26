# import cv2
import streamlit as st
from PIL import Image
import numpy as np
import moviepy.editor as mp
from moviepy.video.io.VideoFileClip import VideoFileClip
import os
import io
import tempfile
from io import BytesIO
import base64
# import comtypes.client
from docx2pdf import convert
from pytube import YouTube
import PyPDF2
import docx
import img2pdf

# def converter(image, ksize, sigma):
#     # Convert to grayscale
#     gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#     # Invert the image
#     inverted_image = 255 - gray_image

#     # Apply a Gaussian blur to the inverted image
#     blurred_image = cv2.GaussianBlur(inverted_image, ksize, sigma)

#     # Blend the grayscale image with the blurred inverted image using the "color dodge" blend mode
#     sketch_image = cv2.divide(gray_image, 255 - blurred_image, scale=256)

#     return sketch_image

def rotate_image(image, angle):
    # Rotate the image
    rotated_image = image.rotate(angle, resample=Image.BICUBIC, expand=True)
    return rotated_image

def trim_video(video_file, start_time, end_time):
    # Load the video
#     clip = mp.VideoFileClip(video_file.name)
    clip = mp.VideoFileClip(r"F:\Video Songs\I See Love Ft. Joe Jonas.mp4")

    # Trim the video
    trimmed_clip = clip.subclip(start_time, end_time)

    # Save the trimmed video
    trimmed_clip.write_videofile("trimmed.mp4")

    return trimmed_clip

def crop_image():
    st.subheader("Welcome to Image Cropper!")
    st.write("This is a simple application that crops an image.")
    # Allow the user to upload an image
    uploaded_file = st.file_uploader("Choose an image file", type=["jpg", "jpeg", "png"])
    
    # If the user has uploaded a file, display it and allow them to crop it
    if uploaded_file is not None:
        try:
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
        except Exception as e:
            st.error(f"Error: {e}")

def image_resizer():
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
                img.save(output_filename)

                # Display the resized image
                st.image(img, caption="Resized Image", use_column_width=True)

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

def youtube_download():
    st.title("YouTube Video Downloader")
    st.subheader("Welcome to YouTube Video Downloader!")
    st.write("This is a simple application that download YouTube videos for you using PyTube.")
    # Ask user for YouTube video URL
    url = st.text_input("Enter the YouTube video URL:")
    try:
        # Create a YouTube object and get the available resolutions
        if url:
            yt = YouTube(url)
            streams = yt.streams.filter(progressive=True)

            # Display available resolutions to user
            res_options = [stream.resolution for stream in streams]
            res_choice = st.selectbox("Select resolution:", res_options)

            # Find video stream with selected resolution
            video = None
            for stream in streams:
                if stream.resolution == res_choice:
                    video = stream

            # Download video when user clicks button
            if video and st.button("Download"):
                video.download()
                st.success("Video downloaded successfully!")
    except Exception as e:
        st.error(f"Error: {e}")


def image_to_pdf():
    """Convert an image file to a PDF file."""
    st.title("Convert Image To PDF")
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



def video2audio():
    st.title("Convert Video To Audio")
    st.subheader("Welcome to Video To Audio Converter!")
    st.write("This is a simple application that converts a Video To Audio.")

    try:
        # File uploader
        uploaded_file = st.file_uploader("Upload a video file", type=["mp4", "mkv", "mov", "avi"])

        if uploaded_file is not None:
            if st.button("Convert to Audio"):
                if uploaded_file is None:
                    st.warning("Please upload a video file first!")
                else:
                    file_name = uploaded_file.name
                    if file_name.endswith(".mp4") or file_name.endswith(".mkv") or file_name.endswith(".mov") or file_name.endswith(".avi"):
                        with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as tmp_file:
                            # Convert video to audio and save to temporary file
                            video = mp.VideoFileClip(uploaded_file.name)
                            audio = video.audio
                            audio.write_audiofile(tmp_file.name)
                            
                            # Download the converted audio file when the user clicks the download button
                            if st.button("Download Audio"):
                                with open(tmp_file.name, 'rb') as f:
                                    bytes_data = f.read()
                                    st.download_button(
                                        label="Download Audio",
                                        data=bytes_data,
                                        file_name=f"{file_name.split('.')[0]}.mp3"
                                    )
                            st.success("Your Audio file has been created successfully!")
                    else:
                        st.warning("Please upload a valid video file with .mp4, .mkv, .mov or .avi extension.")

    except Exception as e:
        st.error(f"Error: {e}")




        
def main():
    st.set_page_config(page_title="Convert Anything!!", page_icon=":pencil2:")

    # Create a sidebar with a menu
    menu = ["Home", 
#             "Image to Sketch", 
            "Image To PDF" , "Rotate Image", "Trim Video", "Crop Image", "Image Resizer", 
#             "Word To PDF", 
            "PDF To Word", "Youtube Video Downloader", "Video To Audio"]
    choice = st.sidebar.selectbox("Select an option", menu)

    # Show the appropriate page based on the user's menu choice
    if choice == "Home":
        st.subheader("Convert Anything From Here!!")
        st.write("Please select available options from the menu to get started.")
#     elif choice == "Image to Sketch":
#         st.subheader("Welcome to Image to Sketch Converter!")
#         st.write("This is a simple application that converts an image to a pencil sketch using OpenCV.")

#         # Upload the image
#         uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])

#         # Display the image as a button
#         if uploaded_file is not None:
#             # Code to convert image to sketch goes here
#             image = Image.open(uploaded_file)
#             st.image(image, caption="Original Image", use_column_width=True)

#             # Convert the PIL image to a NumPy array for OpenCV processing
#             img_np = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

#             # Get the kernel size and sigma from the user
#             ksize = st.slider("Kernel size", 1, 551, 251, step=21)
#             sigma = st.slider("Sigma", 1, 1001, 0)

#             # Convert the image to a sketch
#             sketch_image = converter(img_np, (ksize, ksize), sigma)

#             # Convert the sketch image back to a PIL image for display
#             sketch_image_pil = Image.fromarray(sketch_image)

#             # Show the sketch image
#             st.image(sketch_image_pil, caption="Sketch Image", use_column_width=True)

#             # Save the sketch image as a PNG file
#             sketch_image_pil.save("sketch.png")

#             # Add a button to download the sketch image
#             st.download_button(
#                 label="Download Sketch Image",
#                 data=open("sketch.png", "rb").read(),
#                 file_name="sketch.png",
#                 mime="image/png")
#         else:
#             st.warning("Please click the image to convert it to a sketch.")
    elif choice == "Image To PDF":
        image_to_pdf()
        
    elif choice == "Rotate Image":
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
            rotated_image = rotate_image(image, angle)

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
    elif choice == "Crop Image":
        crop_image()
        
    elif choice == "Image Resizer":
        image_resizer()
    
    elif choice == "Trim Video":
        st.subheader("Welcome to Video Trimmer!")
        st.write("This is a simple application that trim the video.")

        # Upload the video
        uploaded_file = st.file_uploader("Choose a video file", type=["mp4", "avi", "mov"])
        # Display the uploaded video
        st.video(uploaded_file)
        
        if uploaded_file is not None and uploaded_file.name.endswith('.mp4'):
            # Save the uploaded file to a temporary file
            with tempfile.NamedTemporaryFile(delete=False) as temp_file:
                temp_file.write(uploaded_file.read())
                temp_file.flush()

            # Read the video file
            video = VideoFileClip(temp_file.name)

            # Get the length of the video in seconds
            video_length = int(video.duration)

            # Get the start and end times from the user
            start_time = st.slider("Start time (in seconds)", 0, video_length, 0)
            end_time = st.slider("End time (in seconds)", start_time, video_length, video_length)

            # Trim the video
            trimmed_video = video.subclip(start_time, end_time)

            # Convert the trimmed video to a VideoFileClip object
            trimmed_video = trimmed_video.to_videofile("trimmed_video.mp4", fps=video.fps or 30)
            st.write(trimmed_video)

            # Display the trimmed video
            st.video(trimmed_video)

            # Save the trimmed video to a file
            with tempfile.NamedTemporaryFile(delete=False) as temp_file:
                trimmed_video.write_videofile("Trimmed.mp4")

                # Download the trimmed video
                with open(temp_file.name, 'rb') as f:
                    video_bytes = BytesIO(f.read()).getvalue()
                st.download_button("Download trimmed video", data=video_bytes, file_name="trimmed_video.mp4")
        else:
            st.warning("Please upload a video file")
    elif choice == "Word To PDF":
        word2pdf()
    elif choice == "PDF To Word":
        pdf2word()
    elif choice == "Youtube Video Downloader":
        youtube_download()
    elif choice == "Video To Audio":
        video2audio()


if __name__ == "__main__":
    main()
