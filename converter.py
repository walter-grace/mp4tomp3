# Import required libraries
import streamlit as st
from moviepy.editor import *
import os

# Function to handle the conversion
def convert_mp4_to_mp3(mp4_file_path, mp3_file_path):
    # Load the mp4 file
    video = VideoFileClip(mp4_file_path)
    
    # Extract audio from video
    video.audio.write_audiofile(mp3_file_path)

# Main Streamlit app
def main():
    st.title("MP4 to MP3 Converter")

    # Upload the MP4 file
    uploaded_file = st.file_uploader("Choose an MP4 file", type=['mp4'])

    if uploaded_file is not None:
        # Create temporary files
        mp4_file_path = "uploaded_video.mp4"
        mp3_file_path = "converted_audio.mp3"

        # Write the uploaded file to a temporary file
        with open(mp4_file_path, "wb") as f:
            f.write(uploaded_file.read())

        # Call the conversion function
        convert_mp4_to_mp3(mp4_file_path, mp3_file_path)

        # Remove the temporary mp4 file
        os.remove(mp4_file_path)

        # Provide the MP3 download link
        st.write("Conversion complete!")
        
        # Read the MP3 file for download
        with open(mp3_file_path, "rb") as f:
            mp3_bytes = f.read()
        
        # Streamlit download button to download MP3 file
        st.download_button(
            label="Download MP3",
            data=mp3_bytes,
            file_name="converted_audio.mp3",
            mime="audio/mpeg"
        )

        # Remove the temporary mp3 file
        os.remove(mp3_file_path)

if __name__ == "__main__":
    main()
