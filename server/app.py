from flask import Flask
from flask import request, jsonify
from server.function_area.transaction import Transaction

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
    trans = Transaction(account_id)
    return jsonify(trans.get_recent_transaction(day, amount))

