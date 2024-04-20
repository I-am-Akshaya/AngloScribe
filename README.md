
# AngloScribe

This is a console application that transcribes your audio files.


This simple Python application provides functionality for both recording and transcribing audio. It uses the `pyaudio` library for audio recording and `speech_recognition` for speech-to-text transcription. The user interface is built using the `tkinter` library.

## Features

- Record audio in real-time.
- Pause and resume recording.
- Upload existing audio files in `.wav` format for transcription.
- Automatic transcription using Google's Speech Recognition.

## Prerequisites

Before you run the application, make sure you have Python installed. You can download it [here](https://www.python.org/downloads/).

## Installation

1. Clone the repository:

```bash
git clone https://github.com/I-am-Akshaya/your-repo.git
Navigate to the project directory:
bash
Copy code
cd your-repo
Install the required dependencies:
bash
Copy code
pip install pyaudio SpeechRecognition
Usage
Run the application by executing the following command in your terminal:
bash
Copy code
python main.py
Use the GUI to perform the following actions:
Click on the Upload button to select an existing audio file in .wav format for transcription.
Click on the Record Audio button to start recording audio.
Click on the Pause button to pause the recording. Click Record Audio again to resume.
Click on the Stop button to stop the recording.
Once the audio is recorded or the file is uploaded, the transcription will appear in the text block below the buttons.

