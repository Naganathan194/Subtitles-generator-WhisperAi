# SUBTITLE-GENERATOR USING WHISPERAI

A **Streamlit-based app** for transcribing video files and generating subtitles using **OpenAI Whisper**. This tool processes video files locally, extracts audio, performs transcription, and generates `.srt` subtitle files with precise timestamps. It supports large video files (up to **3GB**) and ensures your data stays private without relying on external APIs.

---

## Features
- Extract audio from video files using **FFmpeg** or **PyDub** as fallback.
- Transcribe audio into text using **OpenAI Whisper** (local installation).
- Generate `.srt` subtitle files with accurate timestamps.
- Supports large video uploads up to **3GB**.
- Download subtitles directly from the app.
- Friendly **Streamlit UI** with error handling and progress updates.

---

## Technology Stack
- **Frontend**: Streamlit
- **Backend**: Python
- **Audio Processing**: FFmpeg, PyDub
- **Speech Recognition**: OpenAI Whisper
- **Subtitle Formatting**: Python

---

## Installation

### Prerequisites
1. **Python 3.8 or later**.
2. **FFmpeg installed** and added to your PATH. [Download FFmpeg](https://ffmpeg.org/download.html).
3. **PyTorch** installed for running Whisper. Install it from the [PyTorch website](https://pytorch.org/get-started/locally/).

### Setup Steps
1. Clone this repository:
   ```bash
   git clone https://github.com/Naganathan194/Subtitles-generator-WhisperAi
