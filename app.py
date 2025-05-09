import os
from PIL import Image
from google.colab import files
from utils.router import multimodal_router

# Fungsi untuk input dan respons chat teks
def chat_with_sorachio():
    # Teks
    text_input = input("Enter text for Sorachio: ")
    print("Text Response:", multimodal_router("text", text_input))
    
# Fungsi untuk upload gambar dan respons
def upload_and_process_image():
    print("Upload image file:")
    uploaded_image = files.upload()  # Upload file gambar
    
    for image_name in uploaded_image.keys():
        if os.path.exists(image_name):
            img = Image.open(image_name)
            print("Image Response:", multimodal_router("image", image_name))
        else:
            print(f"[!] {image_name} not found. Please upload it.")
    
# Fungsi untuk upload audio dan respons
def upload_and_process_audio():
    print("Upload audio file:")
    uploaded_audio = files.upload()  # Upload file audio
    
    for audio_name in uploaded_audio.keys():
        if os.path.exists(audio_name):
            print("Audio Response:", multimodal_router("audio", audio_name))
        else:
            print(f"[!] {audio_name} not found. Please upload it.")
            

# Main program
if __name__ == "__main__":
    chat_with_sorachio()

    upload_and_process_image()

    upload_and_process_audio()
