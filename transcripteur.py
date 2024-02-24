
import whisper
file="ytmp3free.cc_history-of-venice-rise-to-glory-youtubemp3free.org.mp3"

model = whisper.load_model("tiny")
result = model.transcribe(file)
with open('transcription.txt', 'w') as f:
    f.write(result["text"])