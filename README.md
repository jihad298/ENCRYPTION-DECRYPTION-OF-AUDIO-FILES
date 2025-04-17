## ENCRYPTION & DECRYPTION OF AUDIO FILES USING AES
In this project, an audio encryption system is developed as a real-time software application. 
Basically, the audio is taken as an input and is encoded to be decoded by authenticated users only. 
The algorithm used to perform this cryptography is Advanced Encryption Standards (AES) algorithm in Python.

### Workflow:
Prompts the user to select an action: encryption (E) or decryption (D).
Guides the user to choose an audio file through select_audio_file() (functionality assumed to be implemented elsewhere).
Validates the presence of a selected file before proceeding.
Requests the user to provide an AES key.
Based on the chosen action:
Encrypts the selected file using encrypt_audio().
Decrypts the selected file using decrypt_audio().
 
 ### Validation:
 Ensures a valid input for the action.
 Exits gracefully if no file is selected or if an invalid option is provided
