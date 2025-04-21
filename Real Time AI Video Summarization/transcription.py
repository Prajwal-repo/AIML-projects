import torchaudio
import torch
from transformers import pipeline
import os

pipe = pipeline("automatic-speech-recognition", model="openai/whisper-small")

def chunk_audio_tensor(waveform, sample_rate, chunk_duration_ms):
    chunk_size = int(sample_rate * chunk_duration_ms / 1000)
    return [waveform[:, i:i+chunk_size] for i in range(0, waveform.size(1), chunk_size)]

def transcribe_in_chunks(audio_path, chunk_duration_ms=30000):
    torchaudio.set_audio_backend("soundfile")
    waveform, sample_rate = torchaudio.load(audio_path)
    chunks = chunk_audio_tensor(waveform, sample_rate, chunk_duration_ms)
    
    transcripts = []
    for i, chunk in enumerate(chunks):
        chunk_path = f"temp_chunk_{i}.wav"
        torchaudio.save(chunk_path, chunk, sample_rate)
        result = pipe(chunk_path)
        transcripts.append(result['text'])
        os.remove(chunk_path)
    
    return " ".join(transcripts)
