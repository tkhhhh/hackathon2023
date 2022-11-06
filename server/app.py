import json
import os

from flask import Flask
from flask import request
from flask.cli import load_dotenv

from server.function_area.transaction import Transaction
from server.text_format.format_text_to_function import TextFormat
from flask_sock import Sock

load_dotenv()  # take environment variables from .env.
authJWT = os.environ['AUTH_JWT']
app = Flask(__name__)
sock = Sock(app)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/api/transaction/recently", methods=["POST"])
def get_recent_transactions():
    content = request.json
    account_id = content["accountID"]
    day = content["day"]
    amount = content["amount"]
    trans = Transaction(account_id, authJWT)
    return json.dumps(trans.get_recent_transaction(day, amount))

@app.route("/api/robot", methods=["POST"])
def robot():
    content = request.json
    text = TextFormat(content)
    return json.dumps(text.analyse_purpose())

if __name__ == "__main__":
    app.run(debug=True)