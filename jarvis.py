#!/usr/bin/env python3
 
import argparse
import os
import queue
import sounddevice as sd
import vosk
import sys
import ollama
import pyttsx4

engine = pyttsx4.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)
 
q = queue.Queue()
 
 
def int_or_str(text):
    """Helper function for argument parsing."""
    try:
        return int(text)
    except ValueError:
        return text
 
def callback(indata, frames, time, status):
    """This is called (from a separate thread) for each audio block."""
    if status:
        print(status, file=sys.stderr)
    q.put(bytes(indata))
 
parser = argparse.ArgumentParser(add_help=False)
parser.add_argument(
    '-l', '--list-devices', action='store_true',
    help='show list of audio devices and exit')
args, remaining = parser.parse_known_args()
if args.list_devices:
    print(sd.query_devices())
    parser.exit(0)
parser = argparse.ArgumentParser(
    description=__doc__,
    formatter_class=argparse.RawDescriptionHelpFormatter,
    parents=[parser])
parser.add_argument(
    '-f', '--filename', type=str, metavar='FILENAME',
    help='text file to store transcriptions')
parser.add_argument(
    '-m', '--model', type=str, metavar='MODEL_PATH',
    help='Path to the model')
parser.add_argument(
    '-d', '--device', type=int_or_str,
    help='input device (numeric ID or substring)')
parser.add_argument(
    '-r', '--samplerate', type=int, help='sampling rate')
args = parser.parse_args(remaining)
 
try:
    if args.model is None:
        args.model = "model"
    if not os.path.exists(args.model):
        print ("Please download a model for your language from https://alphacephei.com/vosk/models")
        print ("and unpack as 'model' in the current folder.")
        parser.exit(0)
    if args.samplerate is None:
        device_info = sd.query_devices(args.device, 'input')
        # soundfile expects an int, sounddevice provides a float:
        args.samplerate = int(device_info['default_samplerate'])
 
    model = vosk.Model(args.model)
 
    if args.filename:
        dump_fn = open(args.filename, "a")
    else:
        dump_fn = None
 
    with sd.RawInputStream(samplerate=args.samplerate, blocksize = 1024, device=args.device, dtype='int16',
                            channels=1, latency='high', callback=callback):
            print('-' * 80)
            print('Press Ctrl+C to stop the recording')
            print('-' * 80)
 
            rec = vosk.KaldiRecognizer(model, args.samplerate)
            while True:
                t = ""
                data = q.get()
                if rec.AcceptWaveform(data):
                    r = eval(rec.Result())
                    t = r["text"]
                    if t and "jarvis" in t:
                        print('\033[92m' + t + '\033[0m\n')
                        if dump_fn is not None and len(t) > 5:
                            dump_fn.write(t+'\n')
                        ollama_response = ollama.chat(model='mistral', messages=[
                            {
                            'role': 'system',
                            'content': 'You are Jarvis, assistant of Loïc the Tony Stark son. You only answer in english but you do not tell it. Do not ask me if you can help me.',
                            },
                            {
                            'role': 'user',
                            'content': t.replace("jarvis", ""),
                            },
                        ])
                        # Printing out of the generated response
                        try:
                            print(ollama_response['message']['content']+ '\n')
                            engine.say(ollama_response['message']['content'])
                            engine.runAndWait()
                        except:
                            a=1
 
except KeyboardInterrupt:
    print('\nDone')
    parser.exit(0)
except Exception as e:
    parser.exit(type(e).__name__ + ': ' + str(e))