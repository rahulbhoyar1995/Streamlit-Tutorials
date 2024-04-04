# Loading the media files

import streamlit as st
from PIL import Image

def main():
    st.title("Streamlit : Working with the media files")
    # Loading image from local directory
    img = Image.open("data/sample_image.jpg")
    st.image(img,use_column_width=True)

    # Loading tmage from URL
    st.image("some_url")

    # Loading video files
    video_file = open("data/sample_video.mp4","rb").read()
    st.video(video_file,start_time = 3)

    # Display the audio files
    audio_file = open("data/song_audio.mp3","rb").read()
    st.audio(audio_file, format="audio/mp3")
    
if __name__ == "__main__":
    main()