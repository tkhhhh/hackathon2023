import os
from flask import Flask
from dotenv import load_dotenv
from api import accounts, sms

load_dotenv()  # take environment variables from .env.
authJWT = os.environ['AUTH_JWT']
twilio_phone_no = os.environ['TWILIO_PHONE_NO']
twilio_account_sid = os.environ['TWILIO_ACCOUNT_SID']
twilio_auth_token = os.environ['TWILIO_AUTH_TOKEN']

app = Flask(__name__)
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
    return "Message sent"
