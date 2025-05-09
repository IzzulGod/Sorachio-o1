import whisper

audio_model = whisper.load_model("small").to('cuda')  # Pastikan model di-load ke GPU

def respond_audio(audio_path):
    result = audio_model.transcribe(audio_path)
    return result['text']
