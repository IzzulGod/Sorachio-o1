import whisper

whisper_model = whisper.load_model("small")

def respond_audio(audio_path):
    result = whisper_model.transcribe(audio_path)
    return result["text"]
