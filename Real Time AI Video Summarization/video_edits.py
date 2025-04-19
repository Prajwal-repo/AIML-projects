from moviepy import VideoFileClip
import os

def extract_audio(video_path, output_audio_path="output/audio.wav"):
    os.makedirs(os.path.dirname(output_audio_path), exist_ok=True)
    clip = VideoFileClip(video_path)
    clip.audio.write_audiofile(output_audio_path, codec='pcm_s16le')
    return output_audio_path

def extract_keyframes(video_path, output_dir="output/keyframes", interval=5):
    os.makedirs(output_dir, exist_ok=True)
    clip = VideoFileClip(video_path)
    for i, t in enumerate(range(0, int(clip.duration), interval)):
        frame = clip.get_frame(t)
        frame_path = os.path.join(output_dir, f"frame_{i}.jpg")
        clip.save_frame(frame_path, t)
    return output_dir
