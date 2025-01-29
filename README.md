# 🎬 SUBTITLE-GENERATOR USING WHISPERAI 🎤  

A **Streamlit-based app** for **transcribing video files** and **generating subtitles** using **OpenAI Whisper**. This tool **extracts audio**, **transcribes speech**, and **creates `.srt` subtitle files** with accurate timestamps. It supports large video files (up to **3GB** 📁) and ensures your **data remains private** 🔐 without relying on external APIs.  

---

## ✨ Features  
✅ **Extract audio** from video files using **FFmpeg** or **PyDub** as a fallback.  
✅ **Transcribe** audio into text using **OpenAI Whisper** 🎙️.  
✅ **Generate `.srt` subtitle files** with precise timestamps ⏳.  
✅ **Upload large video files** up to **3GB** 📂.  
✅ **Download subtitles** directly from the app ⬇️.  
✅ **User-friendly Streamlit UI** with error handling & progress updates 🎨.  

---

## 🛠️ Technology Stack  
🖥️ **Frontend**: Streamlit  
🐍 **Backend**: Python  
🎛️ **Audio Processing**: FFmpeg, PyDub  
🗣️ **Speech Recognition**: OpenAI Whisper  
📝 **Subtitle Formatting**: Python  

---

## ⚙️ Installation  

### 🔹 Prerequisites  
🔹 **Python 3.8 or later** 🐍  
🔹 **FFmpeg installed** and added to your PATH. 👉 [Download FFmpeg](https://ffmpeg.org/download.html) 🎥  
🔹 **PyTorch installed** for running Whisper. 👉 [Get PyTorch](https://pytorch.org/get-started/locally/) 🏋️‍♂️  

---

### 🚀 Setup Steps  
1️⃣ **Clone the repository** 📂:  
   ```bash
   git clone https://github.com/Naganathan194/Subtitles-generator-WhisperAi
   ```
2️⃣ **Navigate to the project folder** 📁:  
   ```bash
   cd Subtitles-generator-WhisperAi
   ```
3️⃣ **Create a virtual environment & activate it** 🔄:  
   ```bash
   python -m venv venv  
   source venv/bin/activate  # On Windows: venv\Scripts\activate  
   ```
4️⃣ **Install dependencies** 📦:  
   ```bash
   pip install -r requirements.txt  
   ```
5️⃣ **Run the Streamlit app** 🎬:  
   ```bash
   streamlit run app.py  
   ```
6️⃣ **Access the app** in your browser via the displayed local URL 🌍.  

---

## 🎯 Impact  
🚀 **Revolutionizes** subtitle generation with AI-powered transcription.  
🎶 **Enhances accessibility** by providing subtitles for videos.  
🔊 **Supports content creators** with efficient subtitle generation.  
🌍 **No external APIs**, ensuring **privacy & security**.  

---

💡 **Easily transcribe videos, generate accurate subtitles, and enhance accessibility with AI!** 🔥🎬🎤  

Let me know if you'd like any further tweaks! 🚀😃
