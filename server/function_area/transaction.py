import datetime
from api_service.load_api import LoadApi

class Transaction(object):

    def __init__(self, authJWT, account_id):
        self.load_api = LoadApi(authJWT)
        self.account_id = account_id

    def get_recent_transaction(self, day, amount):
        json_response = self.load_api.get_user_all_transaction(self.account_id)
        result = {}
        Transactions = []
        for transaction in json_response["Transactions"]:
            # 2022-10-26 02:34:18
            timestamp = datetime.datetime.strptime(transaction["timestamp"], "%Y-%M-%D %HH:%mm:%ss")
            now_timestamp = datetime.datetime.now()
            if (now_timestamp - timestamp).days < day and len(Transactions) < amount:
                Transactions.append(transaction)
        result["Transactions"] = Transactions
        return result
