import os
from PIL import Image
from utils.router import multimodal_router

def chat_with_sorachio():
    text_input = input("Enter text for Sorachio: ")
    print("Text Response:", multimodal_router("text", text_input))

def process_image():
    image_path = input("Enter image file path: ")
    if os.path.exists(image_path):
        img = Image.open(image_path)
        print("Image Response:", multimodal_router("image", img))
    else:
        print(f"[!] {image_path} not found.")

def process_audio():
    audio_path = input("Enter audio file path: ")
    if os.path.exists(audio_path):
        print("Audio Response:", multimodal_router("audio", audio_path))
    else:
        print(f"[!] {audio_path} not found.")

if __name__ == "__main__":
    chat_with_sorachio()
    process_image()
    process_audio()
