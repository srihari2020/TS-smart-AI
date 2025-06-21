# respond.py
import os
import google.generativeai as genai

genai.configure(api_key="AIzaSyBgceWkydv8y7oVgOkOlPtxXucMKdAEMhQ")


def generate_response(text, lang):
    model = genai.GenerativeModel("gemini-1.5-flash")  # or "gemini-2.0-flash-001"
    prompt = f"(reply in {lang})\nUser: {text}"
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print("❌ Gemini error:", e)
        return "Sorry, I couldn't generate a response at the moment."
