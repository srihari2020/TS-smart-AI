import whisper

model = whisper.load_model("medium")  # Use 'medium' or 'large' for better multilingual support

def transcribe_audio(audio_path):
    try:
        print("🔍 Transcribing...")
        result = model.transcribe(audio_path, fp16=False)  # No forced language
        return result["text"].strip()
    except Exception as e:
        print(f"❌ Error in transcription: {e}")
        return ""
