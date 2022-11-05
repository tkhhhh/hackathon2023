import os
from flask import Flask, request, jsonify
from function_area.transaction import Transaction
from dotenv import load_dotenv

load_dotenv()
 # take environment variables from .env.
authJWT = os.environ['AUTH_JWT']

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/transaction/recently", methods=["POST"])
def get_recent_transactions():
    content = request.json
    account_id = content["accountID"]
    day = content["day"]
    amount = content["amount"]
    trans = Transaction(authJWT, account_id)
    return jsonify(trans.get_recent_transaction(day, amount))
