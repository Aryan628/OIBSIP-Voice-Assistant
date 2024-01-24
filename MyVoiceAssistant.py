import os
import random
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import time as t

# Initialize the speech recognition system
listener = sr.Recognizer()

# Initialize the text-to-speech engine
machine = pyttsx3.init()

# Function to speak the provided text
def talk(text):
    machine.say(text)
    machine.runAndWait()

# Function to capture user's voice input
def input_instruction():
    global instruction
    try:
        with sr.Microphone() as source:
            print("Listening.....")
            speech = listener.listen(source)
            os.system("cls")
            print("Processing User's Command ", end='', flush=True)
            for _ in range(10):
                t.sleep(0.1)  # Simulating some processing time
                print(".", end='', flush=True)
            print()
            instruction = listener.recognize_google(speech)
            instruction = instruction.lower()
            # Remove the word 'bro' from the instruction if present
            if "bro" in instruction:
                instruction = instruction.replace('bro','')
            

    except sr.UnknownValueError:
        print("Sorry, I couldn't understand the audio.")

    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")

    except Exception as e:
        print(f"An error occurred: {e}")
    return instruction


# Main execution block
try:
    instruction = input_instruction()
    print(instruction)

    # Process the user's instruction
    if 'play' in instruction or 'sing' in instruction:
        song = instruction.replace('play',"")
        # Play the requested song on YouTube
        talk("Playing "+ song)
        pywhatkit.playonyt(song)

    elif 'time' in instruction:
        # Get the current time and speak it
        time = datetime.datetime.now().strftime("%I:%M %p")
        talk("The current time is "+ time)

    elif 'date' in instruction:
        # Get the current date and speak it
        date = datetime.datetime.now().strftime("%B %d,%Y")
        talk("Today's Date is "+ date)

    elif 'how are you' in instruction:
        # Respond with a random emotion
        emotion = random.choice(["I am good.", "I am doing well."])
        talk(emotion)

    elif 'what is your name' in instruction:
        # Introduce the assistant
        talk("Hi, My name is Bro. I am your personal AI developed by Aryan")

    elif 'who is' in instruction or 'what is' in instruction:
        # Search and speak a summary from Wikipedia
        human = instruction.replace('who is','')
        info = wikipedia.summary(human, 1)
        print(info)
        talk(info)

    elif 'hello' in instruction or 'hi' in instruction:
        # Respond with a random greeting
        greetings = ["Hello there!", "Hey! How can I help you?"]
        talk(random.choice(greetings))

    elif 'stop' in instruction or 'exit' in instruction:
        # Thank the user for using the assistant
        talk('Thank You for using me')

    else:
        # Handle unrecognized instructions
        talk("Sorry, I couldn't understand the audio.")

# Handle unexpected errors
except Exception as e:
        print(f"An unexpected error occurred: {e}")