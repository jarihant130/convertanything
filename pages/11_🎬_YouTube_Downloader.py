import streamlit as st
import os
import io
import tempfile
from io import BytesIO
import base64
from pytube import YouTube
from pydub import AudioSegment

def youtube_download():
    st.set_page_config(page_title="YouTube Video Downloader!!", page_icon=":clapper:", layout="wide")
    # add a title to the app
    st.title("YouTube Video Downloader 🎬")
    st.subheader("Welcome to YouTube Video Downloader!")
    st.write("This is a simple application that download YouTube videos for you using PyTube.")
    
    # Ask user for YouTube video URL
    url = st.text_input("Enter the YouTube video URL:")
    
    try:
        # Create a YouTube object and get the available resolutions
        if url:
            yt = YouTube(url)
            streams = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc()

            # Display available resolutions to user
            options = []
            for stream in streams:
                if stream.includes_audio_track:
                    label = f"{stream.resolution} ({stream.mime_type.split('/')[1]})"
                    options.append(label)
                else:
                    mute_icon = Image.open("mute.png")
                    label = f"{stream.resolution} ({stream.mime_type.split('/')[1]}) [MUTED]"
                    options.append((label, mute_icon))
            
            res_choice = st.selectbox("Select video quality:", options)

            # Find video stream with selected resolution
            video = None
            audio = None
            for stream in streams:
                if f"{stream.resolution} ({stream.mime_type.split('/')[1]})" in res_choice:
                    if stream.includes_audio_track:
                        video = stream
                        audio = stream
                    else:
                        st.warning("Selected stream does not include audio. Please choose a different stream.")
                        return
            
            # Download video with audio when user clicks button
            if st.button("Download Video"):
                if video and audio:
                    # Get video title and create output filename
                    title = yt.title.replace("|", "-").replace(":", "-")
                    filename = f"{title}_{res_choice.split()[0]}.mp4"
                    
                    # Download video to a temporary file
                    with st.spinner(f"Downloading '{filename}'..."):
                        video_path = video.download()
                        audio_path = audio.download()
                        os.system(f"ffmpeg -i \"{video_path}\" -i \"{audio_path}\" -c:v copy -c:a copy \"{filename}\"")
                    
                    # Prompt user to save the downloaded file
                    with open(video_path, "rb") as f:
                        bytes_data = f.read()
                    st.write(f"Do you want to download {title}.mp4?")
                    st.download_button(
                        label="Download Video",
                        data=bytes_data,
                        file_name=filename,
                        mime="video/mp4"
                    )

                    # Delete the temporary files
                    os.remove(video_path)
                    os.remove(audio_path)
                    
                    st.success("Video downloaded successfully!")
                else:
                    st.warning("Please select a video quality that includes audio!")
    except Exception as e:
        pass

if __name__ == '__main__':
    youtube_download()  