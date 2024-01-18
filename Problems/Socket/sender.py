import sounddevice as sd
import numpy as np
import socket

def audio_sender(ip, port):
    # Set up the socket
    sender_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Set up the audio stream
    # fs = 44100  # Sample rate
    # duration = 10  # Duration in seconds
    fs = 2100  # Sample rate
    duration = 5  # Duration in seconds

    # Specify the number of channels (2 for stereo)
    channels = 2

    # Record audio in shorter segments
    segments = []
    segment_duration = 1  # Adjust the segment duration as needed

    
    try:
        # print("Recording audio...")
        # audio_data = sd.rec(int(fs * duration), samplerate=fs, channels=2, dtype=np.int16)
        # sd.wait()
        # for _ in range(int(duration / segment_duration)):
        #     audio_data = sd.rec(int(fs * segment_duration), samplerate=fs, channels=channels, dtype=np.int16)
        #     sd.wait()  # Wait for recording to finish
        #     segments.append(audio_data)

        # Concatenate recorded segments
        # full_audio_data = np.concatenate(segments, axis=0)
        with open("audio.mp4", 'rb') as audio_file:
            audio_bytes = audio_file.read(1024)

        # Convert audio data to bytes
        # audio_bytes = audio_data.tobytes()

        # Send the audio data
        sender_socket.sendto(audio_bytes, (ip, port))
        print("Audio sent successfully!")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        sender_socket.close()

if __name__ == "__main__":
    ip_address = "127.0.0.1"
    port_number = 65535
    audio_sender(ip_address, port_number)


