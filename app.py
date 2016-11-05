from flask import Flask, request, redirect
import twilio.twiml
import os

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
  """Respond to incoming calls with a simple text message."""

    mess = request.values.get('Body', None)

    resp = twilio.twiml.Response()
    resp.message(mess)

    return str(resp)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
