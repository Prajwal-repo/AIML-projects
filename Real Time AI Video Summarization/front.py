import streamlit as st
import transformers
import Summarizer
import transcription
import ffmpeg
import os
import time
import torchaudio
import sentiment

st.title("🎬 Real-Time AI Video Summarizer")

video_file = st.file_uploader("Upload a short video", type=["mp4"])
mode = st.selectbox("Choose summarization mode:", ["abstractive", "extractive"])

asr_pipeline = transformers.pipeline("automatic-speech-recognition", model="openai/whisper-small")

def create_timelapse(input_path, output_path, speed=4):
    try:
        (
            ffmpeg
            .input(input_path)
            .output(
                output_path,
                vf=f"setpts=PTS/{speed}",
                af=f"atempo={min(speed, 2)}",  # atempo max = 2.0, stack if needed
                vcodec="libx264",
                acodec="aac"
            )
            .overwrite_output()
            .run(capture_stdout=True, capture_stderr=True)
        )
    except ffmpeg.Error as e:
        print("FFmpeg Timelapse error:", e.stderr.decode())
        raise e


def trim_video_ffmpeg(input_path, output_path, start_time, duration):
    try:
        (
            ffmpeg
            .input(input_path, ss=start_time, t=duration)
            .output(output_path, vcodec='libx264', acodec='aac')
            .overwrite_output()
            .run(capture_stdout=True, capture_stderr=True)
        )
    except ffmpeg.Error as e:
        print('stdout:', e.stdout.decode('utf8'))
        print("stderr:", e.stderr.decode('utf8'))
        raise e

def extract_audio_ffmpeg(video_path, audio_path):
    try:
        (
            ffmpeg
            .input(video_path)
            .output(audio_path, format='wav', acodec='pcm_s16le', ac=1, ar='16000')
            .overwrite_output()
            .run(capture_stdout=True, capture_stderr=True)
        )
    except ffmpeg.Error as e:
        print("Audio extract error:", e.stderr.decode())
        raise e

def stream_transcription_while_video_plays(video_path, mode):
    # Get video duration via ffmpeg
    probe = ffmpeg.probe(video_path)
    total_duration = int(float(probe['format']['duration']))
    chunk_duration = 30  # seconds

    os.makedirs("temp", exist_ok=True)
    full_transcript = ""
    summary_sections = []
    transcript_placeholder = st.empty()

    for start in range(0, total_duration, chunk_duration):
        end = min(start + chunk_duration, total_duration)

        video_chunk = f"temp/chunk_{start}_{end}.mp4"
        audio_chunk = f"temp/audio_{start}.wav"

        trim_video_ffmpeg(video_path, video_chunk, start, end - start)
        extract_audio_ffmpeg(video_chunk, audio_chunk)

        # Transcribe using transcription.py
        chunk_transcript = transcription.transcribe_in_chunks(audio_chunk)
        full_transcript += f"\n[⏱ {start}s - {end}s]:\n{chunk_transcript}\n"

        # Update transcript on screen
        transcript_placeholder.markdown(f"### 📜 Transcript (Live)\n```\n{full_transcript}\n```")

        # Summarize
        chunk_summary = Summarizer.summarize_text(chunk_transcript, mode)
        base_label, score = sentiment.analyze_sentiment(chunk_transcript)
        motiv_label, emoji = sentiment.map_to_label(base_label, score, chunk_transcript)

        summary_sections.append(
        f"[{start}s - {end}s]: {chunk_summary} (🧠 Sentiment: {motiv_label} {emoji}, score: {score})"
)

        with st.expander(f"📌 Summary for {start}s to {end}s"):
            st.write(chunk_summary)
            st.markdown(f"**🧠 Tone:** {emoji} `{motiv_label}` — confidence `{score}`")


        os.remove(video_chunk)
        os.remove(audio_chunk)
        time.sleep(0.5)

    return full_transcript, "\n\n".join(summary_sections)


if video_file:
    with open("temp_video.mp4", "wb") as f:
        f.write(video_file.read())

    start_btn = st.button("▶️ Start Real-Time Transcription")

    if start_btn:
        with st.spinner("Transcribing as the video plays..."):
            transcript, summary = stream_transcription_while_video_plays("temp_video.mp4", mode)
            timelapse_path = "temp/timelapse.mp4"
            create_timelapse("temp_video.mp4", timelapse_path, speed=4)

        st.subheader("🎞️ Timelapse Preview (4x Speed)")
        st.video(timelapse_path)

        st.subheader("🧾 Full Transcript")
        st.text_area("Transcript", transcript, height=300)

        st.subheader("📝 Full Summary")
        st.success(summary)

        st.download_button("Download Summary", summary, "summary.txt")
