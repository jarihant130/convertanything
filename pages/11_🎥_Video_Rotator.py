import streamlit as st
from moviepy.video.io.VideoFileClip import VideoFileClip
import tempfile
import os
from moviepy.video.fx.all import rotate
def rotate_video():
    st.set_page_config(page_title="Video Rotator!!", page_icon=":arrows_counterclockwise:", layout="wide")
    # add a title to the app
    st.title("Video Rotator App :cyclone:")
    st.subheader("Welcome to Video Rotator!")
    st.write("""This code is a Streamlit application that rotates a user-uploaded video file. It first displays a title and a brief description of the application. The user is then prompted to upload a Video file. If a file is uploaded, the user is prompted to enter the desired output file name, which defaults to "rotated.mp4". The code then rotates the uploaded file to a mentioned angle by the user and saves it in MP4 format. Finally, it displays a "Download" button that allows the user to download the rotated video. If no file is uploaded, the application displays a warning message asking the user to upload a video file first.""")

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
        
        # Output file name
        output_filename = st.text_input("Enter the desired output filename", value="rotated.mp4")
        rotate_angle = st.slider("Rotation angle (in degrees)", -180, 180, 0)
        try:
            
            # Rotate the video clip by 0 degrees clockwise
            rotated_clip = rotate(video, rotate_angle)

            # st.video(rotated_clip, format = "video/mp4", start_time = 0)
            
            # Download the rotated video as a file
            with st.spinner("rotating video..."):
                # Create a temporary file to save the rotated video
                with tempfile.NamedTemporaryFile(suffix=".mp4", delete=False) as f:
                    file_path = f.name
                    # Write the rotated clip to a new video file
                    rotated_clip.write_videofile(file_path, codec="libx264", audio=True)

                # Display the rotated video
                with open(file_path, "rb") as f:
                    video_bytes = f.read()
                    st.video(video_bytes, format="video/mp4", start_time=0)

            # Add a button to download the rotated video
            st.download_button(
                label="Download rotated video",
                data=video_bytes,
                file_name=output_filename,
                mime="video/mp4"
            )
            # Remove the temporary file
            os.unlink(file_path)
            
        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("Please upload the video file to rotate!!")

if __name__ == '__main__':
    rotate_video()
