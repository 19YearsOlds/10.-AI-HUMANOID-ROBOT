import random
import time

def respond(command):
    responses = {
        "hello": "Hello! How can I assist you?",
        "how are you": "I am an AI, I don't have feelings, but I am ready to help!",
        "what is your name": "I am your AI-powered humanoid assistant!",
        "bye": "Goodbye! Have a great day!"
    }
    return responses.get(command.lower(), "I don't understand that command.")

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("AI: Goodbye!")
        break
    response = respond(user_input)
    print("AI:", response)
    time.sleep(1)