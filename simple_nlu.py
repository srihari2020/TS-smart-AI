def generate_response(text):
    if "పేరు" in text:
        return "నా పేరు తెలుగుబోట్."
    elif "సమయం" in text or "టైమ్" in text:
        return "ఇప్పుడు సాయంత్రం అయింది."
    elif "వాతావరణం" in text:
        return "ఈ రోజు వాతావరణం చల్లగా ఉంది."
    else:
        return "క్షమించండి, నాకు అర్థం కాలేదు."