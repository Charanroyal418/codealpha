import spacy
from datetime import datetime

# Load the spaCy model
nlp = spacy.load('en_core_web_sm')

# Predefined questions and answers
qa_pairs = {
    "what is your name?": "I am a chatbot created by you.",
    "how are you?": "I'm doing well, thank you! How can I assist you today?",
    "what can you do?": "I can help answer your questions and chat with you.",
    "where are you from?": "I'm from the digital world, created to assist you.",
}

# Function to get the intent of the user's input
def get_intent(text):
    doc = nlp(text)
    tokens = [token.text.lower() for token in doc]
    if "hello" in tokens or "hi" in tokens:
        return "greeting"
    elif "bye" in tokens or "goodbye" in tokens:
        return "farewell"
    elif any(token in tokens for token in ["date", "time"]):
        return "datetime"
    elif any(token.isdigit() for token in tokens) and any(op in tokens for op in ["+", "-", "*", "/"]):
        return "math"
    else:
        return "question"

# Function to generate a response based on the intent
def generate_response(intent, text):
    if intent == "greeting":
        return "Hello! How can I help you today?"
    elif intent == "farewell":
        return "Goodbye! Have a great day!"
    elif intent == "datetime":
        now = datetime.now()
        return f"The current date and time is {now.strftime('%Y-%m-%d %H:%M:%S')}."
    elif intent == "math":
        try:
            result = eval(text)
            return f"The answer is {result}."
        except Exception as e:
            return "I couldn't understand the math problem. Please try again."
    elif intent == "question":
        for question, answer in qa_pairs.items():
            if question in text.lower():
                return answer
        return "I'm not sure I understand. Could you please rephrase?"
    else:
        return "I'm not sure I understand. Could you please rephrase?"

# Function to run the chatbot
def chatbot():
    print("Chatbot: Hi! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("Chatbot: Goodbye! Have a great day!")
            break

        intent = get_intent(user_input)
        response = generate_response(intent, user_input)
        print("Chatbot:", response)

# Start the chatbot
chatbot()
