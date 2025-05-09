from models.sorachio_model import respond_text
from models.smolvlm_model import respond_image
from models.whisper_model import respond_audio

def multimodal_router(input_type, input_data):
    if input_type == "text":
        return respond_text(input_data)
    elif input_type == "image":
        return respond_image(input_data)
    elif input_type == "audio":
        return respond_audio(input_data)
    else:
        return "Unsupported input type. Use 'text', 'image', or 'audio'."
