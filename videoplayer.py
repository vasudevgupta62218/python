import streamlit as st

st.header('Video Player App')
st.subheader('Enjoy Your Videos')
video=st.file_uploader('Upload Your File- ',type=['mp4','mkv'])
if video is not None:
    st.video(video)
    st.write('ENJOY!')