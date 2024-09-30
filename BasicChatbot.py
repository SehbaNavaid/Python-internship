import nltk
import random
import string

# Download NLTK's punkt tokenizer and wordnet corpus (for lemmatization)
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')

from nltk.chat.util import Chat, reflections
from nltk.corpus import wordnet as wn
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

# Lemmatizer and stopwords
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))

# Sample responses for the chatbot
greetings = ["hello", "hi", "hey", "howdy", "what's up"]
greeting_responses = ["Hello! How can I assist you today?", "Hi! What can I help you with?", "Hey! What's up?"]

basic_questions = {
    "what is your name": "I'm ChatBot, your virtual assistant!",
    "how are you": "I'm just a bunch of code, but thanks for asking!",
    "what do you do": "I am here to chat with you and help you with basic tasks!",
    "who created you": "I was created by a Python programmer!",
    "bye": "Goodbye! Have a nice day!",
}

# Tokenize and preprocess user input
def preprocess_input(user_input):
    tokens = nltk.word_tokenize(user_input.lower())
    tokens = [lemmatizer.lemmatize(word) for word in tokens if word not in stop_words and word not in string.punctuation]
    return tokens

# Check for greetings
def check_greeting(user_input):
    for word in user_input.split():
        if word.lower() in greetings:
            return random.choice(greeting_responses)
    return None

# Generate chatbot response
def chatbot_response(user_input):
    # Check if user input is a greeting
    greeting = check_greeting(user_input)
    if greeting:
        return greeting

    # Check for basic questions
    preprocessed_input = ' '.join(preprocess_input(user_input))
    for question, answer in basic_questions.items():
        if question in preprocessed_input:
            return answer

    # Default response if no matching pattern
    return "I'm sorry, I didn't understand that. Can you rephrase?"

# Main chatbot loop
def chatbot():
    print("ChatBot: Hello! I am a chatbot. Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if 'bye' in user_input.lower():
            print("ChatBot: Goodbye! Have a nice day!")
            break
        response = chatbot_response(user_input)
        print(f"ChatBot: {response}")

if __name__ == "__main__":
    chatbot()
