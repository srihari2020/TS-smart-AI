from gtts import gTTS
from playsound import playsound
import tempfile
import os

def speak_text(text, lang='en',output_path='static/output.mp3'):
    try:
        tts = gTTS(text=text, lang=lang)
        with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as fp:
            temp_path = fp.name
        tts.save(temp_path)
        playsound(temp_path)
        os.remove(temp_path)
    except Exception as e:
        print(f"❌ Error in speaking: {e}")
