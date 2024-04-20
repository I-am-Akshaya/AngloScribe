import tkinter as tk
from tkinter import filedialog
import threading
import pyaudio
import wave
import speech_recognition as sr


class AudioRecorder:
    def __init__(self):
        self.is_recording = False
        self.audio = None
        self.frames = []

    def start_recording(self):
        self.is_recording = True
        self.frames = []
        CHUNK = 1024
        FORMAT = pyaudio.paInt16
        CHANNELS = 2
        RATE = 44100
        p = pyaudio.PyAudio()

        stream = p.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK)

        print("Recording audio...")
        while self.is_recording:
            data = stream.read(CHUNK)
            self.frames.append(data)

        stream.stop_stream()
        stream.close()
        p.terminate()

        self.audio = b''.join(self.frames)
        self.save_audio()

        try:
            transcription_label.config(text="Your Audio says... \n " + self.recognize_audio())
        except:
            transcription_label.config(text="Transcription: Not Available")
            print("Transcription: Not Available")

    def recognize_audio(self):
        r = sr.Recognizer()
        with sr.WavFile("audio.wav") as source:
            audio = r.record(source)
            return r.recognize_google(audio)

    def save_audio(self):
        wf = wave.open("audio.wav", 'wb')
        wf.setnchannels(2)
        wf.setsampwidth(pyaudio.PyAudio().get_sample_size(pyaudio.paInt16))
        wf.setframerate(44100)
        wf.writeframes(self.audio)
        wf.close()

    def stop_recording(self):
        self.is_recording = False

    def pause_recording(self):
        self.is_recording = False

    def resume_recording(self):
        self.is_recording = True
        self.start_recording()

    def record_audio(self):
        threading.Thread(target=self.start_recording).start()


def transcribe_audio(file_path):
    r = sr.Recognizer()
    # with sr.WavFile(file_path) as source:
    with sr.AudioFile(file_path) as source:
    
        audio = r.record(source)    # extract audio data from the file

    try:
        transcription_label.config(text="Your Audio says... \n " + r.recognize_google(audio))
    except:
        transcription_label.config(text="Transcription: Not Available")
        print("Transcription: Not Available")


def upload_file():

    file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.wav")])
    # file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.wav;*.mp3;*.flac;*.ogg;*.wma")])

    if file_path:
        transcribe_audio(file_path)


def record_audio():
    recorder.record_audio()
    record_button.config(state=tk.DISABLED)
    pause_button.grid(row=0, column=2, padx=5, pady=5)
    stop_button.grid(row=0, column=3, padx=5, pady=5)


def pause_audio():
    recorder.pause_recording()
    record_button.config(state=tk.NORMAL)
    pause_button.grid_forget()
    stop_button.grid_forget()


def stop_audio():
    recorder.stop_recording()
    record_button.config(state=tk.NORMAL)
    pause_button.grid_forget()
    stop_button.grid_forget()


# Create Tkinter window
root = tk.Tk()
root.title("Speech Transcription")

# Create an instance of AudioRecorder
recorder = AudioRecorder()

# Styling
bg_color = "#f0f0f0"
button_bg = "#4CAF50"
button_fg = "white"
font_style = ("Arial", 10)
label_bg = "#e0e0e0"
label_border_color = "#BDBDBD"

# Create Upload button
upload_button = tk.Button(root, text="Upload", command=upload_file, width=15, bg=button_bg, fg=button_fg,
                          font=font_style)
upload_button.grid(row=0, column=0, padx=5, pady=5)

# Create Record audio button
record_button = tk.Button(root, text="Record Audio", command=record_audio, width=15, bg=button_bg, fg=button_fg,
                          font=font_style)
record_button.grid(row=0, column=1, padx=5, pady=5)

# Create Pause button
pause_button = tk.Button(root, text="Pause", command=pause_audio, width=15, bg=button_bg, fg=button_fg,
                         font=font_style)

# Create Stop button
stop_button = tk.Button(root, text="Stop", command=stop_audio, width=15, bg=button_bg, fg=button_fg, font=font_style)

# Create a block to display the transcription
transcription_label = tk.Label(root, text="Your Transcription appears here... ", wraplength=300, justify=tk.LEFT,
                               bg=label_bg, font=font_style, bd=1, relief=tk.SOLID, padx=5, pady=5)
transcription_label.grid(row=1, column=0, columnspan=4, padx=5, pady=5, sticky="ew")

# Set column weights
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)

# Set row weights
root.rowconfigure(0, weight=0)
root.rowconfigure(1, weight=1)

# Center the window
window_width = 450
window_height = 200
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_cordinate = int((screen_width / 2) - (window_width / 2))
y_cordinate = int((screen_height / 2) - (window_height / 2))
root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

# Run the Tkinter event loop
root.mainloop()
