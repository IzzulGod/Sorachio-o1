import os
from PIL import Image
from utils.router import multimodal_router

if __name__ == "__main__":
    # TEXT
    text_input = input("Enter text for Sorachio: ")
    print("Text Response:", multimodal_router("text", text_input))

    # IMAGE
    image_path = "sample.jpg"
    if os.path.exists(image_path):
        img = Image.open(image_path)
        print("Image Response:", multimodal_router("image", img))
    else:
        print(f"[!] {image_path} not found. Upload it to this folder.")

    # AUDIO
    audio_path = "sample.wav"
    if os.path.exists(audio_path):
        print("Audio Response:", multimodal_router("audio", audio_path))
    else:
        print(f"[!] {audio_path} not found. Upload it to this folder.")
