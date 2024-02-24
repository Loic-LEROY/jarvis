import whisper
from pocketsphinx import LiveSpeech, get_model_path
import os
import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav

model_path = get_model_path()

speech = LiveSpeech(
    verbose=False,
    sampling_rate=16000,
    buffer_size=2048,
    no_search=False,
    full_utt=False,
    hmm=os.path.join(model_path, 'en-us'),
    lm=os.path.join(model_path, 'en-us.lm.bin'),
    dic=os.path.join(model_path, 'cmudict-en-us.dict')
)

def start_recording():
    print("Started recording...")
    fs=44100
    duration = 5  # seconds
    myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=2)
    sd.wait()

# Save as WAV file
wav.write('output.wav', fs, myrecording)

for phrase in speech:
    print(phrase)
    if "jarvis" in str(phrase):
        start_recording()


file="output.wav"

model = whisper.load_model("tiny")
result = model.transcribe(file)

curl http://localhost:11434/api/generate -d '{
  "model": "mistral",
  "prompt": result["text"]
}'
