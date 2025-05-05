
# Real-Time AI Video Summarizer

## ✅ Project Overview

**Real-Time AI Video Summarizer** is a Streamlit-based web application that enables users to upload a short video and receive:

- 📜 Real-time transcription (chunk-wise)
- 📝 Abstractive or extractive summarization
- 🧠 Sentiment analysis per chunk
- 🎞️ Timelapse generation (4x speed)
- 📸 Keyframe extraction
- 🔊 Audio extraction

---

## 🗂️ Project Structure

```
├── front.py             # Streamlit UI + Real-time logic
├── transcription.py     # Whisper-based audio-to-text transcription
├── Summarizer.py        # Summarization + keyword extraction
├── sentiment.py         # Sentiment classification + label mapping
├── video_edits.py       # Audio extraction, frame grabbing, chunking
├── README.md            # Project documentation
└── output/              # Stores intermediate files (audio, frames)
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/video-summarizer.git
cd video-summarizer
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

<details>
<summary><strong>🧾 requirements.txt (suggested)</strong></summary>

```txt
streamlit
transformers
torch
torchaudio
moviepy
ffmpeg-python
keybert
scikit-learn
```
</details>

### 3. Run the App

```bash
streamlit run front.py
```

---

## 📌 Features

### 1. 🔄 Real-Time Transcription
- Uses OpenAI Whisper to transcribe video chunks.
- Processes 30-second intervals with Whisper and displays live updates.

### 2. ✍️ Summarization
- Select between:
  - `abstractive` (via T5-small)
  - `extractive` (via BART-large-CNN)

### 3. 🎭 Sentiment Analysis
- Uses `cardiffnlp/twitter-roberta-base-sentiment`.
- Maps base sentiment into motivational/emotional tones using emojis.

### 4. 🔧 Video Processing Tools (from `video_edits.py`)
- `extract_audio`: Extracts audio (WAV format)
- `extract_keyframes`: Captures keyframes at intervals (default: 5 sec)
- `split_video_chunks`: Splits video into N-second chunks

### 5. 🎬 Timelapse Generation
- 4x faster preview using FFmpeg.

---

## 🧪 Example Output

```
[0s - 30s]: The speaker discusses the importance of mindset. (🧠 Sentiment: 💪 Empowering, score: 0.97)
[30s - 60s]: They emphasize learning from failure. (🧠 Sentiment: 💡 Insightful, score: 0.93)
...
```

---

## 📁 Output Downloads

- Summary (`.txt`)
- Transcript (`.txt`)
- Timelapse Video (`.mp4`)

---
