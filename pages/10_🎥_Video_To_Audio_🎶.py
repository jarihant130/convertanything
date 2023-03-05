import streamlit as st
import tempfile
import os
from moviepy.video.io.VideoFileClip import VideoFileClip
from pydub import AudioSegment

def video2audio():
    try:
        st.set_page_config(page_title="Video To Audio Converter!!", page_icon=":movie_camera:", layout="wide")
        # add a title to the app
        st.title("Convert Video To Audio :movie_camera:")
        st.subheader("Welcome to Video To Audio Converter!")
        st.write("""
        This code is for a web application that converts a video file into an audio file. The user can upload a video file with the extensions .mp4, .mkv, .mov, or .avi, and the app converts it to an MP3 audio file.

The app uses Streamlit, tempfile, os, moviepy, and pydub libraries.

The app interface includes a title, subheader, and description. The user can upload a video file, and the app converts the video file to an audio file. The converted audio file can be played using the st.audio() method, and the user can also download the file.

The app deletes the temporary file after the user downloads the audio file.
""")
        video_file = st.file_uploader("Upload a video", type=["mp4", "mkv", "mov", "avi"])
        if video_file is not None:
            with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
                tmp_file.write(video_file.read())
                video_clip = VideoFileClip(tmp_file.name)
                audio_clip = video_clip.audio
                audio_file = os.path.abspath("{tmp_file.name[:-4]}.mp3")
                audio_clip.write_audiofile(audio_file)
                file_path = open(audio_file, "rb")
                audio_bytes = file_path.read()
                st.success(f"Your Audio file has been created successfully! Please download your audio file by clicking on '\u22EE'")
                st.audio(audio_bytes, format="audio/mp3")
                
                # check if user downloaded the file
                if st.session_state.get("audio_downloaded", False):
                    os.remove(audio_file)  # delete temporary file
        else:
            st.warning("Please upload a valid video file with .mp4, .mkv, .mov or .avi extension.")
    except Exception as e:
        st.error(f"Error: {e}")

if __name__ == "__main__":
    video2audio()
