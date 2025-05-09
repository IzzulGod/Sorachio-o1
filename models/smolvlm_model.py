from PIL import Image
from transformers import AutoProcessor, AutoModelForVision2Seq
import torch

# Load processor and model once at the top (so they don't reload every call)
processor = AutoProcessor.from_pretrained('SmolVLM/SmolVLM-2-256M-Video-Instruct')
model = AutoModelForVision2Seq.from_pretrained('SmolVLM/SmolVLM-2-256M-Video-Instruct').to('cuda' if torch.cuda.is_available() else 'cpu')

def respond_image(image_path):
    try:
        # Open the image
        image = Image.open(image_path)

        # Define the prompt
        prompt = "<|image|> Describe this image."

        # Process the input
        inputs = processor(prompt, images=[image], return_tensors="pt").to(model.device)

        # Generate the output
        outputs = model.generate(**inputs)

        # Decode the response
        response = processor.decode(outputs[0], skip_special_tokens=True)

        return response
    except Exception as e:
        return f"[Image Error] {str(e)}"
