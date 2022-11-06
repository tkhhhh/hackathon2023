import datetime

import requests
import json

class LoadApi(object):

    def __init__(self, authJWT):
        self.headers = {
            'Authorization': f'Bearer {authJWT}',
            'Content-Type': 'application/json',
            'version': '1.0'
        }

    def create_random_account(self, quantity, numTransactions, liveBalance):
        payload = json.dumps({"quantity": quantity, "numTransactions": numTransactions, "liveBalance": liveBalance})
        response = requests.post(
            "https://sandbox.capitalone.co.uk/developer-services-platform-pr/api/data/accounts/create",
            headers=self.headers,
            data=payload).text
        print(response)
        json_response = json.loads(response)
        return json_response

    def get_account_details(self, account_id):
        response = requests.get(
            f"https://sandbox.capitalone.co.uk/developer-services-platform-pr/api/data/accounts/{account_id}",
            headers=self.headers).text
        json_response = json.loads(response)
        return json_response

    def get_user_all_transaction(self, account_id):
        response = requests.get(
            f"https://sandbox.capitalone.co.uk/developer-services-platform-pr/api/data/transactions/accounts/{account_id}/transactions",
            headers=self.headers, params={}).text
        json_response = json.loads(response)
        return json_response


if __name__ == '__main__':
    load = LoadApi()
    load.get_user_all_transaction("73680920")