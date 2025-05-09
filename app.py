from PIL import Image
from utils.router import multimodal_router as detect_and_respond

if __name__ == "__main__":
    # Test text input
    text_input = "Hello Sorachio!"
    print("Text Response:", detect_and_respond(text_input))

    # Test image input
    image_path = "sample.jpg"
    try:
        image = Image.open(image_path)
        print("Image Response:", detect_and_respond(image))
    except FileNotFoundError:
        print(f"Image file '{image_path}' not found.")

    # Test audio input
    audio_path = "sample.wav"
    if os.path.exists(audio_path):
        print("Audio Response:", detect_and_respond(audio_path))
    else:
        print(f"Audio file '{audio_path}' not found.")
