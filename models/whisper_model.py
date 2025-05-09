import whisper

audio_model = whisper.load_model("small")

def respond_audio(audio_path):
    result = audio_model.transcribe(audio_path)
    return result['text']

