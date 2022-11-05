import os
from flask import Flask
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.
authJWT = os.environ['AUTH_JWT']

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
