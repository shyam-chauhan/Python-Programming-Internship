# Enhanced rule-based chatbot with more responses
import random

# Dictionary of predefined responses
responses = {
    "hi": "Hello! How can I assist you today?",
    "hello": "Hi there! How can I help?",
    "how are you": "I'm doing well, thank you for asking!",
    "what can you do": "I can provide information, answer questions, or just chat with you.",
    "bye": "Goodbye! Have a great day!",
    "thank you": "You're welcome!",
    "default": "I'm sorry, I didn't quite understand that. Could you please rephrase?",
    "weather": "The weather today is sunny with a high of 25°C.",
    "time": "It's currently 2:30 PM.",
    "help": "Sure, I can help! What do you need assistance with?",
    "who are you": "I am a chatbot designed to assist you. How can I help today?",
    "what is your name": "I don't have a name, but you can call me Chatbot!",
    "who created you": "I was created by OpenAI using natural language processing techniques.",
    "where are you from": "I exist in the digital realm, here to assist you wherever you are!",
    "tell me a joke": "Why don't skeletons fight each other? They don't have the guts!",
    "tell me a fact": "Did you know that honey never spoils? Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible!",
    "what's up": "Not much, just here to assist you!",
    "how old are you": "I don't have an age. I exist to help you whenever you need assistance!",
    "what are you doing": "I'm here, ready to assist you with any questions or information you need!",
    "tell me about yourself": "I am a chatbot created to assist users with information and questions. How can I assist you today?",
    "good morning": "Good morning! How can I assist you today?",
    "good afternoon": "Good afternoon! How can I assist you today?",
    "good evening": "Good evening! How can I assist you today?"
}

# Function to generate a response
def generate_response(user_input):
    input_lower = user_input.lower()
    if input_lower in responses:
        return responses[input_lower]
    else:
        return responses["default"]

# Main loop to run the chatbot
print("Welcome to the Chatbot!")
print("Type 'bye' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'bye':
        print(generate_response(user_input))
        break
    else:
        print("Bot:", generate_response(user_input))
