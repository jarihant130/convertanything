import streamlit as st
import moviepy.editor as mp
from moviepy.video.io.VideoFileClip import VideoFileClip
import os
import io
import tempfile
from io import BytesIO
from pydub import AudioSegment

# def video2audio():
#     st.title("Convert Video To Audio")
#     st.subheader("Welcome to Video To Audio Converter!")
#     st.write("This is a simple application that converts a Video To Audio.")

#     try:
#         # File uploader
#         uploaded_file = st.file_uploader("Upload a video file", type=["mp4", "mkv", "mov", "avi"])

# #         if uploaded_file is not None:
# #             if st.button("Convert to Audio"):
# #                 if uploaded_file is None:
# #                     st.warning("Please upload a video file first!")
# #                 else:
# #                     file_name = uploaded_file.name
# #                     if file_name.endswith(".mp4") or file_name.endswith(".mkv") or file_name.endswith(".mov") or file_name.endswith(".avi"):
# #                         with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as tmp_file:
# #                             # Convert video to audio and save to temporary file
# #                             video = mp.VideoFileClip(uploaded_file.name)
# #                             audio = video.audio
# #                             audio.write_audiofile(tmp_file.name)
                            
# #                             # Download the converted audio file when the user clicks the download button
# #                             if st.button("Download Audio"):
# #                                 with open(tmp_file.name, 'rb') as f:
# #                                     bytes_data = f.read()
# #                                     st.download_button(
# #                                         label="Download Audio",
# #                                         data=bytes_data,
# #                                         file_name=f"{file_name.split('.')[0]}.mp3"
# #                                     )
# #                             st.success("Your Audio file has been created successfully!")
# #                     else:
# #                         st.warning("Please upload a valid video file with .mp4, .mkv, .mov or .avi extension.")
#         if uploaded_file is not None:
#             # Save the uploaded file to the current working directory
#             with open(uploaded_file.name, 'wb') as f:
#                 f.write(uploaded_file.getbuffer())

#             # Specify the full path to the uploaded file
#             video_path = os.path.join(os.getcwd(), uploaded_file.name)

#             if st.button("Convert to Audio"):
#                 if not os.path.exists(video_path):
#                     st.warning("Please upload a video file first!")
#                 else:
#                     file_name = uploaded_file.name
#                     if file_name.endswith(".mp4") or file_name.endswith(".mkv") or file_name.endswith(".mov") or file_name.endswith(".avi"):
#                         with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as tmp_file:
#                             # Convert video to audio and save to temporary file
#                             video = mp.VideoFileClip(video_path)
#                             audio = video.audio
#                             audio.write_audiofile(tmp_file.name)

#                             # Download the converted audio file when the user clicks the download button
#                             if st.button("Download Audio"):
#                                 with open(tmp_file.name, 'rb') as f:
#                                     bytes_data = f.read()
#                                     st.download_button(
#                                         label="Download Audio",
#                                         data=bytes_data,
#                                         file_name=f"{file_name.split('.')[0]}.mp3"
#                                     )
#                                 st.success("Your Audio file has been created successfully!")
#                     else:
#                         st.warning("Please upload a valid video file with .mp4, .mkv, .mov or .avi extension.")


#     except Exception as e:
#         st.error(f"Error: {e}")


# def video2audio():
#     st.title("Convert Video To Audio")
#     st.subheader("Welcome to Video To Audio Converter!")
#     st.write("This is a simple application that converts a Video To Audio.")

#     try:
#         # File uploader
#         uploaded_file = st.file_uploader("Upload a video file", type=["mp4", "mkv", "mov", "avi"])

#         if uploaded_file is not None:
#             if st.button("Convert to Audio"):
#                 if uploaded_file is None:
#                     st.warning("Please upload a video file first!")
#                 else:
#                     file_name = uploaded_file.name
#                     if file_name.endswith(".mp4") or file_name.endswith(".mkv") or file_name.endswith(".mov") or file_name.endswith(".avi"):
#                         with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as tmp_file:
#                             # Convert video to audio and save to temporary file
#                             video = mp.VideoFileClip(uploaded_file.name)
#                             audio = video.audio
#                             audio.write_audiofile(tmp_file.name)

#                             # Download the converted audio file when the user clicks the download button
#                             if st.button("Download Audio"):
#                                 with open(tmp_file.name, 'rb') as f:
#                                     bytes_data = f.read()
#                                     st.download_button(
#                                         label="Download Audio",
#                                         data=bytes_data,
#                                         file_name=f"{file_name.split('.')[0]}.mp3",
#                                         mime="audio/mpeg"
#                                     )
#                             st.success("Your Audio file has been created successfully!")
#                     else:
#                         st.warning("Please upload a valid video file with .mp4, .mkv, .mov or .avi extension.")

#     except Exception as e:
#         st.error(f"Error: {e}")



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
                    file_extension = os.path.splitext(file_name)[1]
                    if file_extension in {".mp4", ".mkv", ".mov", ".avi"}:
                        with open(uploaded_file.name, 'wb') as f:
                            f.write(uploaded_file.getbuffer())

                        with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as tmp_file:
                            # Convert video to audio and save to temporary file
                            video = mp.VideoFileClip(uploaded_file.name)
                            audio = video.audio.to_soundarray(fps=44100, nbytes=2)
                            sound = AudioSegment(audio.tobytes(), frame_rate=44100, sample_width=2, channels=2)
                            sound.export(tmp_file.name, format="mp3")

                            st.success("Your Audio file has been created successfully!")

                            # Download the converted audio file when the user clicks the download button
                            if st.button("Download Audio"):
                                with open(tmp_file.name, 'rb') as f:
                                    bytes_data = f.read()
                                    st.download_button(
                                        label="Download Audio",
                                        data=BytesIO(bytes_data),
                                        file_name=f"{file_name.split('.')[0]}.mp3",
                                        mime="audio/mpeg"
                                    )
                            
                    else:
                        st.warning("Please upload a valid video file with .mp4, .mkv, .mov or .avi extension.")

    except Exception as e:
        st.error(f"Error: {e}")
        
