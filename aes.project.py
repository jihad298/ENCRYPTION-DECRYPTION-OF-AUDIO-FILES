import wave
import numpy as np
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import tkinter as tk
from tkinter import filedialog
import os

# Function to select a WAV file from the user's device
def select_audio_file():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(title="Select a WAV audio file", filetypes=[("WAV files", "*.wav")])
    return file_path

# AES Encryption function
def aes_encrypt(audio_data, aes_key):
    cipher = AES.new(aes_key, AES.MODE_CBC)
    iv = cipher.iv
    ciphertext = cipher.encrypt(pad(audio_data, AES.block_size))
    return iv + ciphertext  # Prepend IV to ciphertext

# AES Decryption function
def aes_decrypt(encrypted_data, aes_key):
    iv = encrypted_data[:16]  # Extract IV (first 16 bytes)
    ciphertext = encrypted_data[16:]  # Rest is the actual ciphertext
    cipher = AES.new(aes_key, AES.MODE_CBC, iv)
    return unpad(cipher.decrypt(ciphertext), AES.block_size)

# Function to encrypt audio
def encrypt_audio(input_file, key):
    aes_key = key.ljust(32, '\0').encode('utf-8')[:32]

    # Open the input WAV file
    with wave.open(input_file, 'rb') as wav_in:
        params = wav_in.getparams()
        audio_data = wav_in.readframes(params.nframes)

    # Encrypt the audio data using AES
    encrypted_data = aes_encrypt(audio_data, aes_key)

    # Save the encrypted audio in a new WAV file
    output_file = input_file.replace(".wav", "_encrypted.wav")
    with wave.open(output_file, 'wb') as wav_out:
        wav_out.setparams(params)
        wav_out.writeframes(encrypted_data)

    print(f"Encrypted audio saved to {output_file}")

# Function to decrypt audio
def decrypt_audio(input_file, key):
    aes_key = key.ljust(32, '\0').encode('utf-8')[:32]

    # Open the encrypted WAV file
    with wave.open(input_file, 'rb') as wav_in:
        params = wav_in.getparams()
        encrypted_audio_data = wav_in.readframes(params.nframes)

    # Decrypt the audio data using AES
    decrypted_data = aes_decrypt(encrypted_audio_data, aes_key)

    # Save the decrypted audio to a new WAV file
    output_file = input_file.replace("_encrypted.wav", "_decrypted.wav")
    with wave.open(output_file, 'wb') as wav_out:
        wav_out.setparams(params)
        wav_out.writeframes(decrypted_data)

    print(f"Decrypted audio saved to {output_file}")

# Main function to run the AES encryption and decryption
def main():
    action = input("Do you want to (E)ncrypt or (D)ecrypt? ").strip().lower()

    # Select an audio file
    input_file = select_audio_file()
    if not input_file:
        print("No file selected. Exiting.")
        return
    
    # Ask for a key
    key = input("Enter the AES key: ")

    if action == 'e':
        encrypt_audio(input_file, key)
    
    elif action == 'd':
        decrypt_audio(input_file, key)
    
    else:
        print("Invalid option. Please enter 'E' for encryption or 'D' for decryption.")

if __name__ == "__main__":
    main()
