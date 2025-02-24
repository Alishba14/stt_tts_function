 Speech-to-Text and Text-to-Speech Project

 Overview
This project enables users to convert speech to text and text to speech using HTML, CSS, JavaScript, and Python. It utilizes Python libraries like `gTTS` for text-to-speech conversion and `speech_recognition` for speech-to-text functionality. The web interface allows users to interact with the application seamlessly.

 Features
- Speech-to-Text: Converts spoken words into text using Google's Speech Recognition API.
- Text-to-Speech: Converts written text into spoken words using Google Text-to-Speech (gTTS).
- User-Friendly Interface: Simple and responsive design for easy interaction.
 Technologies Used
- Frontend:
  - HTML: Structure of the web application.
  - CSS: Styling for a clean and responsive design.
  - JavaScript: Handles user interactions and communicates with the backend.
- Backend:
  - Python: Processes speech and text conversion.
  - Libraries:
    - `logging`: For debugging and tracking the application flow.
    - `gTTS`: Converts text to speech.
    - `speech_recognition`: Recognizes speech from audio input.

 Installation
1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd speech-to-text-text-to-speech
   ```

2. Install dependencies:
   ```bash
   pip install gtts SpeechRecognition
   ```

3. Run the application:
   ```bash
   python app.py
   ```

Usage
- Open the web application in your browser.
- Click the **Record** button to speak and see the text output.
- Enter text in the input box and click **Convert to Speech** to hear it spoken aloud.
 File Structure
```
├── app.py               # Python backend for processing requests
├── templates/
│   └── index.html       # Web interface
├── static/
│   ├── css/
│   │   └── styles.css   # Styling
│   └── js/
│       └── script.js    # Frontend logic
└── README.md            # Project documentation
```
 Code Overview
 Python (app.py)
- Sets up a Flask server to handle frontend requests.
- Converts text to speech using `gTTS` and returns an audio file.
- Processes audio input for speech-to-text conversion using `speech_recognition`.

 HTML (index.html)
- Provides buttons for recording speech and converting text to speech.
- Displays recognized text on the page.

 CSS (styles.css)
- Styles buttons and layout for responsiveness and usability.

 JavaScript (script.js)
- Captures user actions and sends requests to the backend.
- Plays generated audio and displays recognized text.

 Contributing
Contributions are welcome! Please fork the repository and create a pull request.

 License
This project is open-source under the MIT License.

