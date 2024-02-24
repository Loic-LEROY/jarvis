from vosk import Model, KaldiRecognizer
import os
import wave

# Load a model
model = Model("path_to_model_directory")

# Create a recognizer
rec = KaldiRecognizer(model, 16000)

# Open a wave file
wf = wave.open("path_to_audio_file.wav", "rb")

# Check if the file is opened
if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getcomptype() != "NONE":
    print ("Audio file must be WAV format mono PCM.")
    exit(1)

# Use the recognizer to transcribe the audio
while True:
    data = wf.readframes(4000)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        print(rec.Result())
    else:
        print(rec.PartialResult())

print(rec.FinalResult())