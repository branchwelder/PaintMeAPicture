import os

os.environ["CLOUDINARY_URL"] = "cloudinary://883825118655646:VlZmyyexT5904-9WIUNTnQXb7ew@djj2spuau"
os.environ["cloud_name"]="djj2spuau"
os.environ["api_key"]="883825118655646"
os.environ["api_secret"]="VlZmyyexT5904-9WIUNTnQXb7ew"


from flask import Flask, request, redirect
import twilio.twiml
import random
from chatterbot import ChatBot
from retrieve_images import get_images_from_sentence
from Collagerator.collagerator import collagerator

app = Flask(__name__)

help_string = "Thank you for using LolChat! Here are some things you can text me:\n\"collage\"+ your collage idea makes you a beautiful collage!\n\"newfact\"+your_fact adds a new fact to the Cat Fact database!\n\"fact\" will send you a random cat fact!\n\"word cloud\" will send you a word cloud!\nAnything else will start a conversation with Ron Obvious!"

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
    return str(chatbot.get_response(text))

def make_collage(text):
    img = get_images_from_sentence(text)
    url = collagerator(img)
    return str(url[0])



# ChatBot setup
chatbot = ChatBot('Ron Obvious', trainer='chatterbot.trainers.ChatterBotCorpusTrainer')

# Train based on the english corpus
chatbot.train("chatterbot.corpus.english")

# Route Logic
@app.route("/", methods=['GET', 'POST'])
def index():
    """Respond to incoming messages with a simple text message."""

    user_message = request.values.get('Body', None).lower().strip()
    response_message = twilio.twiml.Response()

    if user_message == "helpme":
        response_message.message(help_string)
    elif user_message == "fact":
        response_message.message("True fact: " + choose_fact())
    elif user_message[:7] == "newfact":
        response_message.message(add_fact(user_message[8:]))
    elif user_message[:7] == "collage":
        response_message.message(make_collage(user_message[8:]))
    elif user_message == "last fact":
        response_message.message(last_fact())
    elif user_message == "word cloud":
        response_message.message("cloud")
    elif user_message == "dog":
        response_message.message("HISSSSSSSSSSSSSSSSSSSSSSSS")
    else:
        response_message.message(chat(user_message))

    return str(response_message)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
