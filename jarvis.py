import speech_recognition as sr
from mistral import NaturalLanguageProcessor
from text_to_speech import TextToSpeech

# Initialize the voice recognition module
r = sr.Recognizer()

# Initialize the natural language processing module
nlp = NaturalLanguageProcessor()

# Initialize the text-to-speech module
tts = TextToSpeech()

# Function to process user commands
def process_command(command):
    # Perform natural language processing on the command
    nlp_result = nlp.process(command)
    
    # Extract the intent and entities from the NLP result
    intent = nlp_result.intent
    entities = nlp_result.entities
    
    # Perform actions based on the intent and entities
    if intent == "greet":
        tts.speak("Hello! How can I assist you?")
    elif intent == "search":
        if "query" in entities:
            query = entities["query"]
            tts.speak(f"Searching for {query}")
            # Perform search operation here
        else:
            tts.speak("What would you like me to search for?")
    else:
        tts.speak("I'm sorry, I didn't understand that command.")

# Function to listen for user commands
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        
        try:
            # Use voice recognition to convert speech to text
            command = r.recognize_google(audio)
            print(f"Command: {command}")
            
            # Process the user command
            process_command(command)
        except sr.UnknownValueError:
            print("Sorry, I could not understand what you said.")
        except sr.RequestError as e:
            print(f"Sorry, an error occurred: {e}")

# Main loop to continuously listen for commands
while True:
    listen()
