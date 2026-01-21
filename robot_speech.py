import speech_recognition as sr
import pyttsx3

recognizer = sr.Recognizer()
speaker = pyttsx3.init()

def speak(text):
    speaker.say(text)
    speaker.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            return recognizer.recognize_google(audio)
        except:
            return "I didn't understand"

while True:
    command = listen()
    print("You said:", command)

    if "hello" in command:
        speak("Hello! How can I help you?")
    elif "exit" in command:
        speak("Goodbye!")
        break