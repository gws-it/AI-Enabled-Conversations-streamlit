# Streamlit Audio Transcription and Chat Application

This project is a web application that allows users to upload audio files for transcription and interact with an AI chat model. It utilizes a Flask backend for audio processing and a Streamlit frontend for user interaction.

## Project Structure

```
streamlit-app
├── audio_server.py      # Flask application for audio transcription and chat
├── streamlit_app.py     # Streamlit application for user interface
├── requirements.txt      # List of dependencies
└── README.md             # Project documentation
```

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd streamlit-app
   ```

2. **Create a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   Create a `.env` file in the root directory and add your OpenAI API key:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

## Usage

1. **Run the Flask audio server:**
   ```bash
   python audio_server.py
   ```

2. **Run the Streamlit application:**
   In a new terminal window, run:
   ```bash
   streamlit run streamlit_app.py
   ```

3. **Access the application:**
   Open your web browser and go to `http://localhost:8501` to access the Streamlit interface.

## Features

- Upload audio files for transcription using the Whisper model.
- Interact with an AI chat model powered by OpenAI.
- View transcriptions and chat responses in real-time.

## Dependencies

- Flask
- Streamlit
- Whisper
- OpenAI
- python-dotenv
- soundfile
- numpy
- cryptography

## License

This project is licensed under the MIT License. See the LICENSE file for more details.