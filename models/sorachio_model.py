import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

text_model_id = "IzzulGod/Sorachio-360M-Chat"
tokenizer = AutoTokenizer.from_pretrained(text_model_id)
text_model = AutoModelForCausalLM.from_pretrained(text_model_id).to("cuda")

def build_chat_prompt(user_message):
    
    system_prompt = "<|im_start|>system\nYou are a helpful AI assistant<|im_end|>\n"
    user_prompt = f"<|im_start|>user\n{user_message}<|im_end|>\n"
    assistant_prompt = "<|im_start|>assistant\n"
    return system_prompt + user_prompt + assistant_prompt

def respond_text(prompt):

    chat_prompt = build_chat_prompt(prompt)
    inputs = tokenizer(chat_prompt, return_tensors="pt").to("cuda")

    # Generate respons
    outputs = text_model.generate(
        **inputs,
        max_new_tokens=200,
        do_sample=True,
        temperature=0.7,
        top_p=0.9,
        pad_token_id=tokenizer.eos_token_id
    )

    # Decode respons
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)

    if "<|im_start|>assistant\n" in response:
        response = response.split("<|im_start|>assistant\n")[-1]
    else:
        response = response.replace(prompt, "")

    return response.strip()
