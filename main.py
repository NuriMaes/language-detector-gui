from langdetect import detect

def detect_language(text_to_analyze):
    # Try to detect the language from the input text
    try:
        language_code = detect(text_to_analyze)
        return language_code
    # Return the detected language code
    except Exception:
        return "Unknown"

# Test the function with a sample text
print(detect_language("Hello world"))