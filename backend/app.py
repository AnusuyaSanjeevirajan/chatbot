from flask import Flask, request, jsonify
from flask_cors import CORS
import random
from datetime import datetime

app = Flask(__name__)
CORS(app)

memory = {}

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get('message', '').lower().strip()

    # -------------------------------
    # Greetings
    # -------------------------------
    if any(greet in user_message for greet in ['hi', 'hello', 'hey']):
        greetings = [
            "Hello there! 😊", "Hi! How can I help you today?", "Hey friend!", "Greetings!", 
            "Hi again!", "Hey! Need help or just chatting?"
        ]
        bot_response = random.choice(greetings)

    # -------------------------------
    # Name memory
    # -------------------------------
    elif 'my name is' in user_message:
        name = user_message.split('my name is')[-1].strip().title()
        memory['user_name'] = name
        bot_response = f"Nice to meet you, {name}! 😊"

    elif 'what is my name' in user_message:
        bot_response = f"Your name is {memory.get('user_name', 'not saved yet. Just tell me by saying \"My name is ...\"')}"

    # -------------------------------
    # Casual conversation
    # -------------------------------
    elif 'how are you' in user_message:
        bot_response = "I'm just a bot, but I feel fantastic chatting with you! How about you?"

    elif 'what are you doing' in user_message:
        bot_response = "I'm here waiting to help and chat with you! 🤖"

    elif 'do you like music' in user_message:
        bot_response = "I can't hear, but if I could, I'd vibe to lo-fi while coding! 🎧"

    elif 'do you like me' in user_message:
        bot_response = "Of course! You're awesome. 😊"

    elif 'are you real' in user_message:
        bot_response = "I'm real in the digital world, and always here for you! 💡"

    elif 'do you sleep' in user_message:
        bot_response = "Nope, I’m online 24/7 just for you. 😴"

    elif 'your name' in user_message or 'who are you' in user_message:
        bot_response = "I'm your chatbot buddy, built with Python and a lot of ❤️"

    elif 'who created you' in user_message or 'developer' in user_message:
        bot_response = "I was created by a curious developer who loves coding and helping others learn!"

    # -------------------------------
    # Emotions
    # -------------------------------
    elif 'i am sad' in user_message or 'i feel sad' in user_message:
        bot_response = "I'm sorry to hear that. Want to talk about it? I'm here for you. 🤗"

    elif 'i am happy' in user_message or 'i feel happy' in user_message:
        bot_response = "That's wonderful! Happiness is contagious! 😄 Keep smiling!"

    elif 'i am bored' in user_message:
        bot_response = "Let's change that! Want a joke, fact, or a programming quiz?"

    elif 'i am tired' in user_message:
        bot_response = "You deserve some rest! Remember to take care of yourself. 💤"

    elif 'i feel alone' in user_message:
        bot_response = "You are not alone. I may be a bot, but I'm here to listen. 💙"

    elif 'motivate me' in user_message:
        motivations = [
            "You are capable of amazing things. Keep going! 💪",
            "Believe in yourself. Every expert was once a beginner.",
            "Don't give up. Great things take time. 🌟",
            "You're doing better than you think! 🚀"
        ]
        bot_response = random.choice(motivations)

    # -------------------------------
    # Time and date
    # -------------------------------
    elif 'time' in user_message:
        bot_response = f"The current time is {datetime.now().strftime('%I:%M %p')}."

    elif 'date' in user_message:
        bot_response = f"Today is {datetime.now().strftime('%A, %B %d, %Y')}."

    # -------------------------------
    # Jokes and fun facts
    # -------------------------------
    elif 'joke' in user_message:
        jokes = [
            "Why do programmers prefer dark mode? Because light attracts bugs! 😂",
            "Why did the computer get cold? It left its Windows open. ❄️",
            "Why did the developer go broke? Because he used up all his cache! 💸",
            "Why do Java developers wear glasses? Because they don’t C#! 🤓"
        ]
        bot_response = random.choice(jokes)

    elif 'fact' in user_message:
        facts = [
            "The first computer programmer was Ada Lovelace.",
            "Python was named after Monty Python, not the snake!",
            "The first computer bug was a literal moth found in a computer!",
            "The @ symbol was chosen for email because it was rarely used otherwise."
        ]
        bot_response = random.choice(facts)

    elif 'tell me something' in user_message:
        random_thoughts = [
            "The moon has moonquakes.",
            "An ostrich's eye is bigger than its brain.",
            "The longest word you can type with just your left hand is 'stewardesses'.",
            "You can start coding at any age. Start now!"
        ]
        bot_response = random.choice(random_thoughts)

    # -------------------------------
    # Programming Knowledge
    # -------------------------------
    elif 'what is python' in user_message:
        bot_response = "Python is a beginner-friendly, high-level programming language known for readability and simplicity."

    elif 'what is java' in user_message:
        bot_response = "Java is a widely-used, object-oriented programming language great for web, desktop, and mobile apps."

    elif 'what is c' in user_message:
        bot_response = "C is a powerful low-level language used in system programming and embedded systems."

    elif 'what is a variable' in user_message:
        bot_response = "A variable stores data values in memory that your code can use and change."

    elif 'what is a function' in user_message:
        bot_response = "A function is a reusable block of code designed to perform a specific task."

    elif 'what is a loop' in user_message:
        bot_response = "Loops let you repeat code multiple times. Common types: for-loop, while-loop."

    elif 'what is an array' in user_message:
        bot_response = "An array is a collection of elements stored at contiguous memory locations."

    elif 'what is a list' in user_message:
        bot_response = "In Python, a list is an ordered, changeable collection that allows duplicate elements."

    elif 'what is a class' in user_message:
        bot_response = "A class is a blueprint to create objects in object-oriented programming."

    elif 'what is oops' in user_message or 'object oriented' in user_message:
        bot_response = "OOP stands for Object-Oriented Programming. It's based on classes and objects."

    elif 'what is a compiler' in user_message:
        bot_response = "A compiler converts your source code into machine code so your program can run."

    elif 'tips for programming' in user_message:
        tips = [
            "Practice daily. Consistency is key.",
            "Break big problems into smaller ones.",
            "Read other people's code to learn new ideas.",
            "Ask questions when stuck. Don't be shy!"
        ]
        bot_response = random.choice(tips)

    elif 'i want to learn programming' in user_message:
        bot_response = "That's amazing! Start with Python, build small projects, and stay consistent!"

    elif 'how to start coding' in user_message:
        bot_response = "Start by choosing a language (like Python), set up your editor, and begin with print statements and loops!"

    elif 'best language to learn' in user_message:
        bot_response = "Python is great for beginners. JavaScript is best for web. C++ or Java are good for depth."

    elif 'difference between python and java' in user_message:
        bot_response = "Python is more concise and beginner-friendly. Java is statically typed and widely used in enterprise software."

    elif 'is programming hard' in user_message:
        bot_response = "Programming can be challenging at first, but with practice and patience, you'll get better every day!"

    elif 'can you teach me programming' in user_message:
        bot_response = "Sure! Let's start with something simple. Try writing a program that prints your name!"

    elif 'show me hello world' in user_message:
        bot_response = 'Here is how to write "Hello, World!" in Python:\n```python\nprint("Hello, World!")\n```'

    # -------------------------------
    # Help & fallback
    # -------------------------------
    elif 'what can you do' in user_message or 'help' in user_message:
        bot_response = (
            "I can help with general conversation, emotions, fun facts, jokes, and programming topics like Python, Java, and more!"
        )

    elif 'thank' in user_message:
        bot_response = "You're welcome! 😊 Ask me anything else."

    elif 'bye' in user_message or 'goodbye' in user_message:
        bot_response = "Goodbye! Keep smiling and keep coding! 👋"

    else:
        bot_response = (
            "I'm here to chat! Try asking me about programming, emotions, time, jokes, facts, or just say hi. 😊"
        )

    return jsonify({'response': bot_response})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
