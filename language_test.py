from langdetect import detect

text_samples = [
    "మీ సేవా స్థితిని తెలుసుకోవాలి",  # Telugu
    "मुझे अपनी सेवा की स्थिति जाननी है",  # Hindi
    "I want to check my service status"    # English
]

for text in text_samples:
    lang = detect(text)
    print(f"Detected language: {lang} → Text: {text}")
