import os
from google.colab import files
from utils.router import multimodal_router

# TEXT
text_input = input("Enter text for Sorachio: ")
print("Text Response:", multimodal_router("text", text_input))

# IMAGE
print("Upload image file:")
uploaded_image = files.upload()
for image_name in uploaded_image.keys():
    if os.path.exists(image_name):
        print("Image Response:", multimodal_router("image", image_name))  # Kirim PATH saja
    else:
        print(f"[!] {image_name} not found.")

# AUDIO
print("Upload audio file:")
uploaded_audio = files.upload()
for audio_name in uploaded_audio.keys():
    if os.path.exists(audio_name):
        print("Audio Response:", multimodal_router("audio", audio_name))  # Kirim PATH saja
    else:
        print(f"[!] {audio_name} not found.")
