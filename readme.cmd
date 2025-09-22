# Multi-Mode AI Translator

A versatile and modern translation tool designed to bridge communication gaps. This application provides seamless language translation powered by Google's Gemini AI, alongside robust Morse code encoding and decoding functionalities. The user-friendly interface supports multiple input methods, including text and voice, ensuring a smooth and intuitive experience.

---

## ✨ Features

* **🌐 Language Translation**: Translate text between numerous languages, including English, Spanish, French, Hindi, and more, leveraging the power of the Google Gemini API.
* **🔠 Morse Code Encoder**: Instantly convert English text into its corresponding Morse code representation.
* **🔡 Morse Code Decoder**: Translate Morse code back into English. The interface supports both direct typing and an interactive tap pad for inputting dots, dashes, and spaces.
* **🎤 Voice Input**: Utilizes the browser's Web Speech API for accurate speech-to-text, allowing you to speak directly into the translator for both language and Morse code inputs.
* **🌓 Dual Theme UI**: A sleek, responsive interface featuring both light and dark modes to suit your preference.
* **📋 Translation History**: Access a history of your past language translations in a convenient modal window.
* **🚀 Welcome Portal**: A stylish, animated landing page to welcome users and guide them to the different translation modes.

---

## 💻 Tech Stack

| Category      | Technology                                                                                                  |
| ------------- | ----------------------------------------------------------------------------------------------------------- |
| **Frontend** | HTML5, CSS3, Tailwind CSS, JavaScript                                                                       |
| **Backend** | Python, Flask                                                                                               |
| **APIs** | Google Gemini API, Web Speech API                                                                           |
| **Libraries** | Lucide Icons                                                                                                |

---

## 🚀 Getting Started

Follow these instructions to set up and run the project on your local machine.

### Prerequisites

* Python 3.7+
* `pip` package manager
* A web browser that supports the Web Speech API (e.g., Chrome, Edge)

### Installation & Setup

1.  **Clone the Repository**
    ```bash
    git clone <your-repository-url>
    cd morsecode
    ```

2.  **Backend Setup**
    * Navigate to the backend directory:
        ```bash
        cd backend
        ```
    * Create and activate a Python virtual environment:
        ```bash
        # For macOS/Linux
        python3 -m venv venv
        source venv/bin/activate

        # For Windows
        python -m venv venv
        .\venv\Scripts\activate
        ```
    * Install the required Python packages from `requirements.txt`:
        ```bash
        pip install -r requirements.txt
        ```
    * Create a `.env` file in the `backend` directory. This file will store your API key.
    * Add your Google Gemini API key to the `.env` file. You can obtain a key from [Google AI Studio](https://aistudio.google.com/).
        ```env
        GEMINI_API_KEY="YOUR_GEMINI_API_KEY_HERE"
        ```
    * Run the Flask application:
        ```bash
        flask run
        ```
    The backend server will now be running at `http://127.0.0.1:5000`.

3.  **Frontend Setup**
    * No special setup is required for the frontend. Simply open the `welcome.html` or `index.html` file in your web browser.
        ```bash
        # (From the root 'morsecode' directory)
        open welcome.html
        ```

---

##  usage

Once the backend is running and you have opened the frontend in your browser:

1.  From the **Welcome Portal**, select the translation mode you wish to use:
    * Translate Languages
    * Encode Morse
    * Decode Morse
2.  This will take you to the main translator interface (`index.html`). You can switch between modes at any time using the tabs at the top.
3.  **Language Translation**: Select source and target languages, type or speak your text, and see the translation appear.
4.  **Morse Encoding/Decoding**: Use the dedicated tabs to convert between English and Morse code. For decoding, you can type the code directly or use the interactive tap pad.
5.  **Toggle Theme**: Use the sun/moon icon at the top-right to switch between light and dark modes.
6.  **View History**: Click the history icon to see a list of your previous language translations.

---

## 👥 Credits

This project was created by **Rohit, Leno & Rahul (RLR)**.
