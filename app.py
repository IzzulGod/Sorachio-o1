import os
from PIL import Image
from google.colab import files
from utils.router import multimodal_router as detect_and_respond

if __name__ == "__main__":

    print("Upload image file:")
    uploaded_image = files.upload()
    image_path = list(uploaded_image.keys())[0]  

    print("Upload audio file:")
    uploaded_audio = files.upload()
    audio_path = list(uploaded_audio.keys())[0]  

    # Test text input
    text_input = input("Enter text for Sorachio: ")  
    print("Text Response:", detect_and_respond("text", text_input))

    # Test image input
    try:
        image = Image.open(image_path)
        print("Image Response:", detect_and_respond("image", image))
    except FileNotFoundError:
        print(f"Image file '{image_path}' not found.")

    # Test audio input
    if os.path.exists(audio_path):
        print("Audio Response:", detect_and_respond("audio", audio_path))
    else:
        print(f"Audio file '{audio_path}' not found.")
