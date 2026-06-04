from langdetect import detect
import tkinter as tk

def detect_language(text_to_analyze):
    # Try to detect the language from the input text
    try:
        language_code = detect(text_to_analyze)
        languages_dict = {
            "en": "English",
            "es": "Spanish",
            "fr": "French",
            "it": "Italian",
            "de": "German",
        }
    # Return the detected language code
        return languages_dict.get(language_code, language_code)
    except Exception:
        return "Unknown"
    
def handle_detection():
    user_text = entry.get()
    result_code = detect_language(user_text)
    result_label.config(text=f"Detected Language: {result_code}")

window = tk.Tk()
window.title('Language Detector')
window.geometry('400x300')

title_label = tk.Label(window, text='Language Detector')
title_label.pack(pady=10)

entry = tk.Entry(window, width=50)
entry.pack(pady=10)

button_label = tk.Button(window, text='Detect Language', command=handle_detection)
button_label.pack(pady=10)

result_label = tk.Label(window, text="Language: -")
result_label.pack(pady=10)
window.mainloop()