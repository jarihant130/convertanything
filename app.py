import streamlit as st
from linux_cmd import alphabet_selector
from rotate_image import rotate_image
from crop_image import crop_image
from image_to_pdf import image_to_pdf
from image_resizer import image_resizer
from video2audio import video2audio
# from word2pdf import word2pdf
from youtube_download import youtube_download
# from pdf2word import pdf2word
from trim_video import trim_video
from home import home
from onlinePyCompiler import compiler_app
from password_generator import password_generator
from video2gif import video2gif
from image2sketch import image2sketch
def main():
    st.set_page_config(page_title="Convert Anything!!", page_icon=":pencil2:", layout="wide")
    # Create a sidebar with a menu
    menu = ["Home", #home.py
            "Image to Sketch", #image2sketch.py
            "Image To PDF" , #image_to_pdf.py
            "Rotate Image", #rotate_image.py
#             "Trim Video", #trim_video.py
            "Crop Image", #crop_image.py
            "Image Resizer", #image_resizer.py
#             "Word To PDF", #word2pdf.py
#             "PDF To Word", #pdf2word.py
            "Youtube Video Downloader", #youtube_download.py
            "Video To Audio", #video2audio.py
           "Linux Commands", #linux_cmd.py
            "Online Python Compiler", #onlinePyCompiler.py
            "Password Generator", #password_generator.py
            "Video To GIF", #video2gif.py
           ]
    choice = st.sidebar.selectbox("Select an option", menu)
    st.sidebar.markdown('''
        ---
        Made with ❤️ by Arihant Jain ([Study Material](https://www.youtube.com/channel/UCeC088dyJsXK_L1bCHZDcjA))
        ''')
    
    # Show the appropriate page based on the user's menu choice
    if choice == "Home":
        home()
        
    elif choice == "Image to Sketch":
        image2sketch()

    elif choice == "Image To PDF":
        image_to_pdf()
        
    elif choice == "Rotate Image":
        rotate_image()

    elif choice == "Crop Image":
        crop_image()
        
    elif choice == "Image Resizer":
        image_resizer()
    
#     elif choice == "Trim Video":
#         trim_video()
        
#     elif choice == "Word To PDF":
#         word2pdf()
        
#     elif choice == "PDF To Word":
#         pdf2word()
        
    elif choice == "Youtube Video Downloader":
        youtube_download()
        
    elif choice == "Video To Audio":
        video2audio()
        
    elif choice == "Linux Commands":
        alphabet_selector()
    elif choice == "Online Python Compiler":
        compiler_app()
    elif choice == "Password Generator":
        password_generator()
    elif choice == "Video To GIF":
        video2gif()
if __name__ == "__main__":
    main()
