import sounddevice as sd
import soundfile as sf

def record_audio(filename, duration=5, samplerate=16000):
    print("🎙️ Recording...")
    audio = sd.rec(int(samplerate * duration), samplerate=samplerate, channels=1)
    sd.wait()
    sf.write(filename, audio, samplerate)
    print(f"✅ Saved recording to {filename}")
