import streamlit as st
import Summarizer
import transcription
import ffmpeg
import os
import time
from moviepy import VideoFileClip

st.title("🎬 Real-Time AI Video Summarizer")

video_file = st.file_uploader("Upload a short video", type=["mp4"])
mode = st.selectbox("Choose summarization mode:", ["abstractive", "extractive"])

def stream_transcription_while_video_plays(video_path, mode):
    chunk_duration = 30  # seconds
    clip = VideoFileClip(video_path)
    total_duration = int(clip.duration)

    transcript_placeholder = st.empty()
    full_transcript = ""
    summary_sections = []

    for start in range(0, total_duration, chunk_duration):
        end = min(start + chunk_duration, total_duration)
        output_filename = f"video_chunk_{start}_{end}.mp4"

        # ✅ Trim clip by setting start time and duration (avoid subclip)
        chunk_clip = clip.set_start(start).set_duration(end - start)
        chunk_clip.write_videofile(output_filename, codec="libx264", audio_codec="aac", logger=None)

        # Extract audio from chunk
        audio_path = f"temp_audio_{start}.wav"
        chunk_clip.audio.write_audiofile(audio_path, logger=None)

        # Transcribe and summarize
        chunk_transcript = transcription.transcribe_in_chunks(audio_path)
        full_transcript += f"\n[⏱ {start}s - {end}s]:\n{chunk_transcript}\n"
        transcript_placeholder.markdown(f"### 📜 Transcript (Live)\n```\n{full_transcript}\n```")

        chunk_summary = Summarizer.summarize_text(chunk_transcript, mode)
        summary_sections.append(f"[{start}s - {end}s]: {chunk_summary}")

        with st.expander(f"📌 Summary for {start}s to {end}s"):
            st.write(chunk_summary)

        # Clean up
        os.remove(output_filename)
        os.remove(audio_path)
        time.sleep(0.5)  # simulate live stream delay

    return full_transcript, "\n\n".join(summary_sections)


if video_file:
    with open("temp_video.mp4", "wb") as f:
        f.write(video_file.read())

    st.video("temp_video.mp4")

    start_btn = st.button("▶️ Start Real-Time Transcription")

    if start_btn:
        with st.spinner("Transcribing as the video plays..."):
            transcript, summary = stream_transcription_while_video_plays("temp_video.mp4", mode)

        st.subheader("🧾 Full Transcript")
        st.text_area("Transcript", transcript, height=300)

        st.subheader("📝 Full Summary")
        st.success(summary)

        st.download_button("Download Summary", summary, "summary.txt")
