import streamlit as st
import Summarizer
import transcription
import video_edits

st.title("🎬 Real-Time AI Video Summarizer")

video_file = st.file_uploader("Upload a short video", type=["mp4"])
mode = st.selectbox("Choose summarization mode:", ["abstractive", "extractive"])

if video_file:
    with open("temp_video.mp4", "wb") as f:
        f.write(video_file.read())

    st.video("temp_video.mp4")

    with st.spinner("Extracting audio and keyframes..."):
        audio_path = video_edits.extract_audio("temp_video.mp4")
        video_edits.extract_keyframes("temp_video.mp4")

    with st.spinner("Transcribing..."):
        transcript = transcription.transcribe_in_chunks(audio_path)

    with st.spinner("Summarizing..."):
        summary = Summarizer.summarize_text(transcript, mode)

    st.subheader("Transcript")
    st.text_area("Transcript", transcript, height=300)

    st.subheader("Summary")
    st.success(summary)

    st.download_button("Download Summary", summary, "summary.txt")
