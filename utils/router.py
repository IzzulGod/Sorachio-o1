from PIL import Image
import os
from models.sorachio_model import respond_text
from models.smolvlm_model import respond_image
from models.whisper_model import respond_audio

def detect_and_respond(input_data):
    if isinstance(input_data, str) and os.path.exists(input_data) and input_data.endswith(('.wav', '.mp3', '.m4a')):
        return respond_audio(input_data)
    elif isinstance(input_data, Image.Image):
        return respond_image(input_data)
    elif isinstance(input_data, str):
        return respond_text(input_data)
    else:
        return "Unknown input type."
