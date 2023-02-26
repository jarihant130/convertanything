import streamlit as st
import moviepy.editor as mp
from moviepy.video.io.VideoFileClip import VideoFileClip
import tempfile
from io import BytesIO

def trim_video():
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
