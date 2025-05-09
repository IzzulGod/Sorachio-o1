import torch
from transformers import AutoProcessor, AutoModelForImageTextToText
from PIL import Image

vlm_model_id = "HuggingFaceTB/SmolVLM2-256M-Video-Instruct"
vlm_processor = AutoProcessor.from_pretrained(vlm_model_id)
vlm_model = AutoModelForImageTextToText.from_pretrained(
    vlm_model_id,
    torch_dtype=torch.bfloat16,
    _attn_implementation="flash_attention_2"
)
vlm_model = vlm_model.to("cuda")


def respond_image(image_path):
    image = Image.open(image_path)
    inputs = vlm_processor(images=image, text="Describe this image.", return_tensors="pt").to("cuda")
    with torch.no_grad():
        generated_ids = vlm_model.generate(**inputs, max_new_tokens=100)
        generated_text = vlm_processor.batch_decode(generated_ids, skip_special_tokens=True)[0]
    return generated_text
