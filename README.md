# Sorachio Multimodal Assistant

This project combines:
- Sorachio-360M-Chat for text
- SmolVLM2-256M-Video-Instruct for image/video
- Whisper small for audio (ASR)
- Coqui TTS for text-to-speech (optional)

## Setup

1. Clone this repository:

git clone https://github.com/IzzulGod/Sorachio-o1.git cd Sorachio-o1

2. Install dependencies:

pip install -r requirements.txt

3. Run the app:

python app.py

Make sure you provide sample image (sample.jpg) and sample audio (sample.wav) in the root folder for testing.

---

## Folder Structure

- *models/* → contains model loading + response functions
- *utils/* → contains the input routing logic
- *app.py* → main script to test everything
-
