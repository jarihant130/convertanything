import streamlit as st
from moviepy.video.io.VideoFileClip import VideoFileClip
import tempfile
import os

def trim_video():
    st.set_page_config(page_title="Video Trimmer!!", page_icon=":scissors:", layout="wide")
    # add a title to the app
    st.title("Video Trimmer App :scissors:")
    st.subheader("Welcome to Video Trimmer!")
    st.write("This is a simple application that trim the video with the help of Python.")

    # Upload a video file
    video_file = st.file_uploader("Upload a video", type=["mp4"])
    
    if video_file:
        video_bytes = video_file.read()

        # Save the video file to a temporary file
        with tempfile.NamedTemporaryFile(suffix=".mp4", delete=False) as f:
            f.write(video_bytes)
            file_path = f.name
        
        # Load the video file
        video = VideoFileClip(file_path)
        st.video(video_bytes, format = "video/mp4", start_time = 0)
            
        # Get the start and end times for the trim
        start_time = st.slider("Start time (in seconds)", 0, int(video.duration))
        end_time = st.slider("End time (in seconds)", start_time, int(video.duration))
        try:
            # Trim the video from start_time to end_time
            trimmed_video = video.subclip(start_time, end_time)
            
            # Output file name
            output_filename = st.text_input("Enter the desired output filename", value="trimmed.mp4")
            
            # Download the trimmed video as a file
            with st.spinner("Trimming video..."):
                # Create a temporary file to save the trimmed video
                with tempfile.NamedTemporaryFile(suffix=".mp4", delete=False) as f:
                    file_path = f.name
                    trimmed_video.write_videofile(file_path, codec="libx264", audio=True)

                # Display the trimmed video
                with open(file_path, "rb") as f:
                    video_bytes = f.read()
                    st.video(video_bytes, format="video/mp4", start_time=0)

            # Add a button to download the trimmed video
            st.download_button(
                label="Download trimmed video",
                data=video_bytes,
                file_name=output_filename,
                mime="video/mp4"
            )
            # Remove the temporary file
            os.unlink(file_path)
            st.write(file_path)
            
        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("Please upload the video file to trim!!")

if __name__ == '__main__':
    trim_video()
