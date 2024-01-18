# from pydub import AudioSegment
# import numpy as np
# import math

# def generate_sine_wave(duration, frequency, amplitude=0.5, sample_rate=44100):
#     t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
#     y = amplitude * np.sin(2 * np.pi * frequency * t)
#     return y

# def add_sine_wave(input_path, output_path, sine_frequency=440, sine_amplitude=0.1):
#     # Load the original audio file
#     audio = AudioSegment.from_file("audio.mp4", format="mp4")

#     # Generate a sine wave with the same duration as the audio
#     duration = len(audio) / 1000  # Convert milliseconds to seconds
#     sine_wave = generate_sine_wave(duration, sine_frequency, sine_amplitude)

#     # Convert the sine wave to the same format as the original audio
#     sine_wave_audio = AudioSegment(
#         np.int16(sine_wave * 32767),  # Convert to 16-bit PCM
#         frame_rate=audio.frame_rate,
#         channels=1,  # Mono
#     )

#     # Add the sine wave to the original audio
#     audio_with_sine = audio.overlay(sine_wave_audio)

#     # Export the result to a new audio file
#     audio_with_sine.export(output_path, format="mp4")

# if __name__ == "__main__":
#     input_audio_path = "audio.mp4"
#     output_audio_path = "audio_with_sine.mp4"
    
#     # Add a sine wave with a frequency of 500 Hz and amplitude of 0.1
#     add_sine_wave(input_audio_path, output_audio_path, sine_frequency=500, sine_amplitude=0.1)

#     print(f"Sine wave added and saved to {output_audio_path}")
import numpy as np
from scipy.io import wavfile

def add_sine_wave(input_file, output_file, frequency=440.0, duration=5.0, amplitude=0.5):
    # Read the original audio file
    sample_rate, original_data = wavfile.read(input_file)

    # Create a time array for the sine wave
    time = np.arange(0, duration, 1/sample_rate)

    # Generate the sine wave
    sine_wave = amplitude * np.sin(2 * np.pi * frequency * time)

    # Ensure the sine wave has the same length as the original audio
    sine_wave = sine_wave[:len(original_data)]

    # Add the sine wave to the original audio
    augmented_data = original_data + sine_wave.astype(np.int16)

    # Save the augmented audio to a new file
    wavfile.write(output_file, sample_rate, augmented_data)

# Specify the input audio file and output file
input_audio_file = "audio.mp4"
output_audio_file = "audio_with_sine.mp4"

# Add a sine wave to the audio file
add_sine_wave(input_audio_file, output_audio_file, frequency=440.0, duration=5.0, amplitude=0.1)
