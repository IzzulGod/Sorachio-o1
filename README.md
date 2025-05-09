# Sorachio-o1 Multimodal

This project combines:
- Sorachio-360M-Chat for text
- SmolVLM2-256M-Video-Instruct for image/video
- Whisper (small) for audio

## Setup

1. Clone the repo:
```bash
git clone https://github.com/IzzulGod/Sorachio-o1.git
cd Sorachio-o1
```

2. Install requirements:
```
pip install -r requirements.txt
```


3. Run the app:
```
python app.py
```


Usage

-Input type: text, image, or audio
-Input data: For text, type your prompt; for image/audio, provide the file path.


Example:
```
Input type (text/image/audio or 'quit'): text
Input data (prompt or file path): Who are you?
Response: I am Sorachio, your AI assistant!
```
