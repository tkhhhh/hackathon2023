import datetime

import requests
import json

class LoadApi(object):

    def __init__(self):
        authJWT = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJuYmYiOjE2NjI0MjI0MDAsImFwaV9zdWIiOiJjNzgzNTAzODJlNDc3YTMyNmYwMjQ5Mzg1M2NhMmI5NzNiYjA0OGZjYTFkZmJjMWZlMDg0NTNkNTg2NWVmNjcwMTY3NTEyMzIwMDAwMCIsInBsYyI6IjVkY2VjNzRhZTk3NzAxMGUwM2FkNjQ5NSIsImV4cCI6MTY3NTEyMzIwMCwiZGV2ZWxvcGVyX2lkIjoiYzc4MzUwMzgyZTQ3N2EzMjZmMDI0OTM4NTNjYTJiOTczYmIwNDhmY2ExZGZiYzFmZTA4NDUzZDU4NjVlZjY3MCJ9.ZqiS7hmgZ6yfCp4PNdt9vpnq4NqgyOX6MT9ZMNOsezr1-s9Enz9hugQewlEcSxBpoAfeSEupTU96_NLhlWcHGxI1_TNcTwlnwHOk9gpjju7pKlc2JyUhJg9wE2nve1Tr5SYJVCKtGChxrkZLcoEqHqSLirqvByetcAVDjbIWWDb-E-5ETvMZDzicN0gDxyA6bDwEFtBALbFAKJe1hEinCcc6N_2BYLDYKWO0KXPPlXylsMvoESg_IOkZwiIH8_gniqUXiSlHwdZGgsAbhMPKPKTh4EKXwpLqcmekB1oyyWRYHpFiWtmrSk_wK_UDt1eQ-KFbEhLEbP4Mz69ZxTwKAQ"
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
        json_response = json.loads(response)
        print(json_response)

    def get_user_all_transaction(self, account_id):
        response = requests.get(
            f"https://sandbox.capitalone.co.uk/developer-services-platform-pr/api/data/transactions/accounts/{account_id}/transactions",
            headers=self.headers, params={}).text
        json_response = json.loads(response)
        return json_response


if __name__ == '__main__':
    load = LoadApi()
    load.get_user_all_transaction("73680920")