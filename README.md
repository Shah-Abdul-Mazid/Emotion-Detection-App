# oaqjp-final-project-emb-ai

A premium, responsive Python Flask web application that detects emotions in user-provided text using Watson NLP's advanced Natural Language Processing services. This application classifies text into five emotional spectrums: **anger**, **disgust**, **fear**, **joy**, and **sadness**, and identifies the **dominant emotion**.

---

## 🌟 Key Features
- **Watson NLP Integration**: Connects to the robust Watson NLP EmotionPredict API.
- **Dynamic, Modern UI**: Built with a stunning radial background, custom Outfit typography, glassmorphic glass card, and clean responsive CSS.
- **Robust Error Handling**: Gracefully intercepts invalid/blank text inputs and reports status 400 issues appropriately.
- **10/10 PEP-8 Quality**: Backend files scored a perfect `10.00/10` in pylint code quality analysis.
- **Complete Test Coverage**: Unit-tested suite via `unittest` covering all baseline emotional dimensions.

---

## 📁 Project Directory Structure
```text
Emotion Detection App/
├── .venv/                         # Python Virtual Environment
├── EmotionDetection/              # Packaged Core Module
│   ├── __init__.py                # Module initialization and exports
│   └── emotion_detection.py       # Core Watson API connection logic
├── static/                        # Static assets (images, stylesheets, scripts)
│   └── mywebscript.js             # Client-side AJAX handler script
├── templates/                     # Jinja2 template files
│   └── index.html                 # Main interface HTML page
├── tests/                         # Test directory
│   └── test_emotion_detection.py  # Unit test assertions
├── server.py                      # Flask web server routing entrypoint
└── README.md                      # Project documentation (this file)
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- Flask framework
- Requests library

### Installation & Run
1. Clone this repository to your system:
   ```bash
   git clone <your-repository-url>
   cd "Emotion Detection App"
   ```
2. Activate your virtual environment and install dependencies:
   ```bash
   .venv\Scripts\activate
   pip install flask requests pylint
   ```
3. Start the Flask server:
   ```bash
   python server.py
   ```
4. Access the web application by opening your browser and navigating to:
   ```text
   http://localhost:5000
   ```

---

## 🧪 Running Unit Tests
Execute the unit tests using Python's standard `unittest` library:
```bash
python -m unittest tests/test_emotion_detection.py
```

---

## 🛡️ Static Code Quality Score
Run pylint static analysis to confirm perfect compliance with coding guidelines:
```bash
pylint server.py
```
**Current Score**: `10.00/10` ⭐
