import os
import uuid
import datetime
import logging
import google.generativeai as genai
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv

# This is a new utility import, make sure you have this file
# from utils.json_handler import save_result, read_results

# Load environment variables from a .env file
load_dotenv()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("ai-translator-backend")

app = Flask(__name__)
CORS(app)  # This enables Cross-Origin Resource Sharing

# --- Morse Code Logic ---
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
    ',': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-', ' ': '/'
}
MORSE_TO_ENG_DICT = {v: k for k, v in MORSE_CODE_DICT.items()}

# --- API Endpoints ---
@app.route('/translate', methods=['POST'])
def translate():
    try:
        data = request.json
        text_to_translate = data.get('text')
        source_lang_name = data.get('source_lang')
        target_lang_name = data.get('target_lang')

        if not all([text_to_translate, source_lang_name, target_lang_name]):
            return jsonify({"error": "Missing required fields"}), 400

        genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        prompt = f"Translate the following text from {source_lang_name} to {target_lang_name}. Provide only the direct translation, without any additional explanations or context:\n\n\"{text_to_translate}\""
        
        response = model.generate_content(prompt)
        translated_text = response.text.strip()
        
        # Prepare data in a simple format for saving to history
        result_to_save = {
            "id": uuid.uuid4().hex,
            "timestamp": datetime.datetime.utcnow().isoformat() + "Z",
            "source_lang": source_lang_name,
            "target_lang": target_lang_name,
            "original_text": text_to_translate,
            "translated_text": translated_text
        }
        # save_result(result_to_save)
        
        return jsonify({"translated_text": translated_text})

    except Exception as e:
        logger.exception(f"An error occurred during translation: {e}")
        return jsonify({"error": "An internal error occurred during translation."}), 500

@app.route('/results/', methods=['GET'])
def get_results():
    # return jsonify({"status": "success", "data": read_results()})
    return jsonify({"status": "success", "data": []})

@app.route('/eng-to-morse', methods=['POST'])
def eng_to_morse():
    data = request.json
    text = data.get('text', '').upper()
    morse_code = ' '.join(MORSE_CODE_DICT.get(char, '') for char in text)
    return jsonify({"morse_code": morse_code.replace('  ', ' / ').strip()})

@app.route('/morse-to-eng', methods=['POST'])
def morse_to_eng():
    data = request.json
    morse_code = data.get('morse_code', '').strip()
    words = morse_code.split(' / ')
    english_text = ' '.join(
        ''.join(MORSE_TO_ENG_DICT.get(code, '') for code in word.split(' '))
        for word in words
    )
    return jsonify({"english_text": english_text})


if __name__ == '__main__':
    app.run(port=5000, debug=True)