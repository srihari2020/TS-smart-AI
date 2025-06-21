from flask import Flask, request, jsonify, render_template
import os
import uuid

from transcribe import transcribe_audio
from language_detect import detect_language
from respond import generate_response
from speak import speak_text
from transcribe import transcribe_audio

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')  # This line should be clean and end here.

@app.route('/process_audio', methods=['POST'])

def process_audio():
    audio_file = request.files['audio']
    file_path = os.path.join("input.wav")
    audio_file.save(file_path)

    try:
        text = transcribe_audio(file_path)
        print("✅ Transcribed Text:", text)

        lang = detect_language(text)
        print("🌐 Detected Language:", lang)

        reply = generate_response(text, lang)
        print("💬 Generated Reply:", reply)

        output_path = f"static/output_{uuid.uuid4().hex}.mp3"
        speak_text(reply, lang, output_path)

        return jsonify({
            "transcription": text,
            "reply": reply,
            "audio_url": "/" + output_path
        })
    except Exception as e:
        import traceback
        traceback.print_exc()  # 🔍 Logs full error to terminal

        return jsonify({
            "error": str(e),
            "transcription": "",
            "reply": "❌ Error processing audio."
        })
if __name__ == '__main__':
    app.run(debug=True)
