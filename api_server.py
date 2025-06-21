from flask import Flask, request, jsonify, send_file
import tempfile
import os
from transcribe import transcribe_audio
from language_detect import detect_language
from respond import generate_response
from speak import speak_text
import traceback

app = Flask(__name__)

@app.route('/process', methods=['POST'])
def process():
    if 'audio' not in request.files:
        return jsonify({'error': 'No audio file provided'}), 400
    audio_file = request.files['audio']
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix='.wav') as temp_audio:
            audio_path = temp_audio.name
            audio_file.save(audio_path)
    except Exception as e:
        app.logger.error(f"Audio save error: {e}\n{traceback.format_exc()}")
        return jsonify({'error': f'Audio save error: {e}'}), 500
    try:
        transcript = transcribe_audio(audio_path)
    except Exception as e:
        app.logger.error(f"Transcription error: {e}\n{traceback.format_exc()}")
        os.remove(audio_path)
        return jsonify({'error': f'Transcription error: {e}'}), 500
    try:
        language = detect_language(transcript)
    except Exception as e:
        app.logger.error(f"Language detection error: {e}\n{traceback.format_exc()}")
        os.remove(audio_path)
        return jsonify({'error': f'Language detection error: {e}'}), 500
    try:
        response_text = generate_response(transcript, language)
    except Exception as e:
        app.logger.error(f"Response generation error: {e}\n{traceback.format_exc()}")
        os.remove(audio_path)
        return jsonify({'error': f'Response generation error: {e}'}), 500
    try:
        from gtts import gTTS
        lang_map = {'en': 'en', 'hi': 'hi', 'te': 'te'}
        lang_code = lang_map.get(language, 'en')
        tts = gTTS(text=response_text, lang=lang_code)
        fd, tts_path = tempfile.mkstemp(suffix='.mp3')
        os.close(fd)
        tts.save(tts_path)
    except Exception as e:
        app.logger.error(f"TTS error: {e}\n{traceback.format_exc()}")
        os.remove(audio_path)
        return jsonify({'error': f'TTS error: {e}'}), 500

    def cleanup():
        os.remove(audio_path)
        if os.path.exists(tts_path):
            os.remove(tts_path)
    
    try:
        response = send_file(tts_path, mimetype='audio/mpeg')
        response.headers['Transcript'] = transcript
        response.headers['Response-Text'] = response_text
        response.call_on_close(cleanup)
        return response
    except Exception as e:
        app.logger.error(f"Send file error: {e}\n{traceback.format_exc()}")
        cleanup()
        return jsonify({'error': f'Send file error: {e}'}), 500

if __name__ == '__main__':
    app.run(port=5001, debug=True) 