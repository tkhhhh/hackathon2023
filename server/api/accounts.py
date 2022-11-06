import json
import requests

def create_account(authJWT):
    headers = {
        'Authorization': f'Bearer {authJWT}',
        'Content-Type': 'application/json',
        'version': '1.0'
    }
    quantity = 1
    numTransactions = 0
    liveBalance = True
    payload = json.dumps({"quantity": quantity, "numTransactions": numTransactions, "liveBalance": liveBalance})

    response = requests.post("https://sandbox.capitalone.co.uk/developer-services-platform-pr/api/data/accounts/create", headers=headers, data=payload).text
    json_response = json.loads(response)
    return json_response

def get_account_details(authJWT, account_id):
    headers = {
        'Authorization': f'Bearer {authJWT}',
        'Content-Type': 'application/json',
        'version': '1.0'
    }

    response = requests.get(f"https://sandbox.capitalone.co.uk/developer-services-platform-pr/api/data/accounts/{account_id}", headers=headers).text
    json_response = json.loads(response)
    return json_response
