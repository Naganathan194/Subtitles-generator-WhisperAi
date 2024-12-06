import os
import streamlit as st
import whisper
import subprocess
from pydub import AudioSegment

# Set ffmpeg path (ensure it's correctly set for your system)
os.environ["FFMPEG_BINARY"] = r"C:\ffmpeg\ffmpeg-2024-12-04-git-2f95bc3cb3-full_build\bin\ffmpeg.exe"

# Function to extract audio from video using subprocess and FFmpeg (if ffmpeg is available)
def extract_audio_ffmpeg(video_path, output_audio_path):
    try:
        # Call FFmpeg using subprocess
        command = [
            os.environ["FFMPEG_BINARY"],
            "-i", video_path,
            "-vn",  # Disable video
            "-acodec", "pcm_s16le",  # Set audio codec
            "-ar", "16000",  # Set audio sample rate
            "-ac", "1",  # Mono audio
            output_audio_path
        ]
        subprocess.run(command, check=True)
        return output_audio_path
    except Exception as e:
        st.error(f"Error extracting audio using FFmpeg: {e}")
        return None

# Function to extract audio using pydub (alternative method in case FFmpeg doesn't work)
def extract_audio_pydub(video_path, output_audio_path):
    try:
        # Load audio from the video file using pydub (requires ffmpeg installed)
        audio = AudioSegment.from_file(video_path)
        audio = audio.set_channels(1)  # Mono audio
        audio = audio.set_frame_rate(16000)  # Sample rate 16000 Hz
        audio.export(output_audio_path, format="wav")
        return output_audio_path
    except Exception as e:
        st.error(f"Error extracting audio using pydub: {e}")
        return None

# Function to transcribe audio using Whisper (OpenAI Whisper package)
def transcribe_audio(audio_path, model_name="base"):
    try:
        model = whisper.load_model(model_name)  # Load the Whisper model
        result = model.transcribe(audio_path)   # Perform transcription
        return result
    except Exception as e:
        st.error(f"Error in transcription: {e}")
        return None

# Function to generate SRT subtitles
def generate_srt(transcription_result, output_srt_path):
    def format_time(seconds):
        millis = int((seconds - int(seconds)) * 1000)
        seconds = int(seconds)
        minutes, seconds = divmod(seconds, 60)
        hours, minutes = divmod(minutes, 60)
        return f"{hours:02}:{minutes:02}:{seconds:02},{millis:03}"

    try:
        with open(output_srt_path, "w", encoding="utf-8") as srt_file:
            for i, segment in enumerate(transcription_result["segments"]):
                start = segment["start"]
                end = segment["end"]
                text = segment["text"]
                srt_file.write(f"{i+1}\n")
                srt_file.write(f"{format_time(start)} --> {format_time(end)}\n")
                srt_file.write(f"{text}\n\n")
        return output_srt_path
    except Exception as e:
        st.error(f"Error generating SRT: {e}")
        return None

# Streamlit UI
st.title("Video Transcription and Subtitle Generator")
st.markdown("Upload a video to generate subtitles automatically using OpenAI Whisper.")
uploaded_video = st.file_uploader("Upload a video file", type=["mp4", "mkv", "avi", "mov"])

if uploaded_video:
    st.info("Processing the uploaded video...")
    # Save uploaded video to a temporary file
    temp_video_path = f"temp/{uploaded_video.name}"
    os.makedirs("temp", exist_ok=True)
    with open(temp_video_path, "wb") as f:
        f.write(uploaded_video.read())
    
    st.success("Video uploaded successfully!")

    # Try extracting audio with FFmpeg first
    st.info("Extracting audio from the video...")
    temp_audio_path = "temp/audio.wav"
    audio_path = extract_audio_ffmpeg(temp_video_path, temp_audio_path)
    
    # If FFmpeg extraction fails, use pydub as a fallback
    if not audio_path:
        st.warning("FFmpeg extraction failed, trying pydub...")
        audio_path = extract_audio_pydub(temp_video_path, temp_audio_path)
    
    if audio_path:
        st.success("Audio extracted successfully!")

        # Transcribe the audio using Whisper
        st.info("Transcribing audio...")
        transcription = transcribe_audio(audio_path)
        
        if transcription:
            st.success("Transcription completed!")
            st.subheader("Transcription")
            st.write(transcription["text"])

            # Generate subtitles
            st.info("Generating subtitles...")
            output_srt_path = "temp/subtitles.srt"
            srt_path = generate_srt(transcription, output_srt_path)
            
            if srt_path:
                st.success("Subtitles generated!")
                # Provide a download link for the subtitles
                with open(srt_path, "rb") as srt_file:
                    st.download_button(
                        label="Download Subtitles (.srt)",
                        data=srt_file,
                        file_name="subtitles.srt",
                        mime="text/srt"
                    )

# Clean up temporary files after processing
if st.button("Clear Temporary Files"):
    if os.path.exists("temp"):
        for file in os.listdir("temp"):
            os.remove(os.path.join("temp", file))
        st.success("Temporary files cleared!")
