from flask import Flask, request, redirect
import twilio.twiml
import os
import random
from chatterbot import ChatBot
from chatterbot.training.trainers import ChatterBotCorpusTrainer

app = Flask(__name__)

help_string = "Thank you for using LolChat! Here are some things you can text me:\n\"newfact\"+your_fact adds a new fact to the Cat Fact database!\n\"fact\" will send you a random cat fact!"

# helper functions
def choose_fact():
    lines = open('cat_facts.txt').read().splitlines()
    return random.choice(lines)

def add_fact(fact):
    with open('cat_facts.txt', 'a') as f:
        f.write(fact+"\n")
    return "Cat fact added!"

def last_fact():
    lines = open('cat_facts.txt').read().splitlines()
    return lines[-1]

def chat(text):
    return chatbot.get_response(text)

# ChatBot setup
chatbot = ChatBot("Ron Obvious")
chatbot.set_trainer(ChatterBotCorpusTrainer)
chatbot.train("chatterbot.corpus.english")

# Route Logic
@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
    """Respond to incoming calls with a simple text message."""

    user_message = request.values.get('Body', None).lower()
    response_message = twilio.twiml.Response()

    if user_message == "helpme":
        response_message.message(help_string)
    elif user_message == "fact":
        response_message.message("True fact: " + choose_fact())
    elif user_message[:7] == "newfact":
        response_message.message(add_fact(user_message[8:]))
    elif user_message == "last fact":
        response_message.message(last_fact())
    else:
        response_message.message(chat(user_message))

    return str(response_message)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
