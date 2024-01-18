from pydub import AudioSegment
from pydub.playback import play
import numpy as np
import sounddevice as sd
import librosa.display
import matplotlib.pyplot as plt
import speech_recognition as sr

# Load audio file
# audio = AudioSegment.from_file("audio.mp4", format="mp4")

# Play audio
# play(audio)
# Load audio file
sine_frequency = 440  # Frequency in Hertz (Hz)
sine_duration = 3 
sample_rate = 44100

t = np.linspace(0, sine_duration, int(sample_rate * sine_duration), endpoint=False)
sine_wave = 0.5 * np.sin(2 * np.pi * sine_frequency * t)
# Play the sine wave
sd.play(sine_wave, samplerate=sample_rate)
sd.wait()

# Specify the parameters for the sine wave

y, sr = librosa.load("audio.mp4")

# # Display waveform
# plt.figure(figsize=(14, 5))
# librosa.display.waveshow(y, sr=sr)
# plt.title('Waveform')
# plt.show()
# import librosa

# Load audio file
# y, sr = librosa.load("example.wav")

# Extract features (e.g., chroma feature)
# chroma = librosa.feature.chroma_stft(y=y, sr=sr)

recognizer = sr.Recognizer()

# Record audio from the microphone
with sr.Microphone() as source:
    print("Say something:")
    audio = recognizer.listen(source)

try:
    # Recognize speech using Google Speech Recognition
    text = recognizer.recognize_google(audio)
    print("You said: {}".format(text))
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand the audio.")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))

# Print the chroma feature matrix
# print(chroma)

