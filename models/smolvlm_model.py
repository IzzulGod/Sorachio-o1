from transformers import AutoProcessor, AutoModelForVision2Seq

vlm_id = "HuggingFaceTB/SmolVLM2-256M-Video-Instruct"

vlm_processor = AutoProcessor.from_pretrained(vlm_id)
vlm_model = AutoModelForVision2Seq.from_pretrained(vlm_id, device_map="auto")

def respond_image(image):
    inputs = vlm_processor(images=image, text="Describe this image.", return_tensors="pt").to(vlm_model.device)
    outputs = vlm_model.generate(**inputs, max_new_tokens=100)
    response = vlm_processor.decode(outputs[0], skip_special_tokens=True)
    return response
