from flask import Flask, request, redirect
import twilio.twiml
import os
import random

app = Flask(__name__)

def choose_fact():
    lines = open('cat_facts.txt').read().splitlines()
    return random.choice(lines)


@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
    """Respond to incoming calls with a simple text message."""

    user_message = request.values.get('Body', None).lower()
    response_message = twilio.twiml.Response()

    if user_message == "fact":
        response_message.message("True fact: " + choose_fact())
    else:
        response_message.message("I'm going to assume you wanted a cat fact! True fact: " + choose_fact())

    return str(response_message)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
