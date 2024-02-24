import os
import sounddevice as sd
import scipy.io.wavfile as wav
import ollama
import speech_recognition as sr

#------------------------- Recording -------------------------#
def record_audio():
    # Set the duration of the recording (in seconds)
    duration = 5

    # Set the sample rate and number of channels for the recording
    sample_rate = 44100
    channels = 1

    # Start recording audio
    audio = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=channels)

    # Wait for the keyword "Jarvis" to be detected
    keyword = "Jarvis"
    detected = False
    while not detected:
        # Check if the keyword is present in the recorded audio
        if keyword in audio:
            detected = True

    # Stop recording audio
    sd.wait()

    # Save the recorded audio to a file
    audio_file = "output.wav"
    wav.write(audio_file, sample_rate, audio)

record_audio()

#------------------------- Speech Recognition -------------------------#
def speech_to_text():
    # Load the recorded audio file
    audio_file = "output.wav"

    # Initialize the recognizer
    r = sr.Recognizer()

    # Open the audio file
    with sr.AudioFile(audio_file) as source:
        # Read the audio data from the file
        audio_data = r.record(source)

        # Convert speech to text
        text = r.recognize_google(audio_data)

    return text

# Call the speech_to_text function
text = speech_to_text()
print("Speech to text:", text)

#------------------------- Ollama -------------------------#
# Setting up the model, enabling streaming responses, and defining the input messages
ollama_response = ollama.chat(model='mistral', messages=[
     {
     'role': 'system',
     'content': 'You are a helpful assistant.',
     },
     {
     'role': 'user',
     'content': audio,
     },
])
# Printing out of the generated response
print(ollama_response['message']['content'])
