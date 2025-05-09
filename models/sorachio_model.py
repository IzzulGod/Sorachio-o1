import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

text_model_id = "IzzulGod/Sorachio-360M-Chat"
tokenizer = AutoTokenizer.from_pretrained(text_model_id)
text_model = AutoModelForCausalLM.from_pretrained(text_model_id).to("cuda")

def respond_text(prompt):
    inputs = tokenizer(prompt, return_tensors="pt").to("cuda")
    outputs = text_model.generate(**inputs, max_new_tokens=200)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)
