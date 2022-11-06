
# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client

def send_sms(twilio_account_sid, twilio_auth_token, sender, recipient):
    # Find your Account SID and Auth Token at twilio.com/console
    # and set the environment variables. See http://twil.io/secure
    client = Client(twilio_account_sid, twilio_auth_token)
    message = client.messages.create(
        body="Join Earth's mightiest heroes. Like Kevin Bacon.",
        from_=sender,
        to=recipient
    )
    return message.sid
