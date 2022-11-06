import datetime
from api_service.load_api import LoadApi

class Account(object):

    def __init__(self, account_id, authJWT):
        self.load_api = LoadApi(authJWT)
        self.account_id = account_id

    def get_account_details(self, day, amount):
        json_response = self.load_api.get_account_details(self.account_id)
        return json_response["Accounts"][0]

