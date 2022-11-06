import os, json
from flask import Flask, request
from flask.cli import load_dotenv
from api import accounts, sms

from server.function_area.transaction import Transaction
from server.text_format.format_text_to_function import TextFormat
from flask_sock import Sock


load_dotenv()  # take environment variables from .env.
authJWT = os.environ['AUTH_JWT']
twilio_phone_no = os.environ['TWILIO_PHONE_NO']
twilio_account_sid = os.environ['TWILIO_ACCOUNT_SID']
twilio_auth_token = os.environ['TWILIO_AUTH_TOKEN']

app = Flask(__name__)
sock = Sock(app)
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/test/accounts/create")
def create_account():
    account_data = accounts.create_account(authJWT)
    return f"{account_data}"

@app.route("/test/accounts/<account_id>")
def get_account(account_id):
    account_data = accounts.get_account_details(authJWT, account_id)
    return f"{account_data}"

@app.route("/test/sms/<phone_no>")
def send_sms(phone_no):
    sms.send_sms(twilio_account_sid, twilio_auth_token, twilio_phone_no, phone_no)

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
