
import sounddevice as sd
import numpy as np
import socket

def audio_receiver(ip, port):
    # Set up the socket
    receiver_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    receiver_socket.bind((ip, port))

    # Set up the audio stream
    fs = 44100  # Sample rate
    duration = 10  # Duration in seconds

    try:
        print("Waiting for audio...")
        audio_bytes, addr = receiver_socket.recvfrom(fs * duration * 2)  # 2 channels, 2 bytes per sample
        audio_data = np.frombuffer(audio_bytes, dtype=np.int16)

        # Play the received audio
        sd.play(audio_data, samplerate=fs)
        sd.wait()

        print("Audio received and played successfully!")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        receiver_socket.close()

if __name__ == "__main__":
    ip_address = "127.0.0.1"
    port_number = 65535
    audio_receiver(ip_address, port_number)