from record import record_audio
from transcribe import transcribe_audio
from language_detect import detect_language
from respond import generate_response
from speak import speak_text

def run_assistant():
    try:
        print("🎙️ Speak now...")
        audio_file = "input.wav"
        record_audio(audio_file, duration=5)

        text = transcribe_audio(audio_file)
        print(f"📝 మీరు చెప్పారు:  {text}")
        if not text:
            print("⚠️ Could not detect speech.")
            return

        lang = detect_language(text)
        print(f"🌐 Detected Language: {lang}")

        reply = generate_response(text, lang)
        print(f"🤖 Response: {reply}")

        speak_text(reply, lang)

    except Exception as e:
        print("❌ Error:", e)
