from api_service.load_api import LoadApi
import matplotlib.pyplot as plt
from dotenv import load_dotenv
from matplotlib.backends.backend_pdf import PdfPages

from server.api_service.load_api import LoadApi
import os
import pandas as pd

from matplotlib import rcParams, pyplot as plt

rcParams['axes.spines.top'] = False
rcParams['axes.spines.right'] = False

def create_pie_chart_data(auth_JWT, account_id):
    api = LoadApi(auth_JWT)
    transactions = api.get_user_all_transaction(account_id)["Transactions"]
    # total = 0
    categories = {

    }
    for t in transactions:
        category = t["merchant"]["category"]
        if (category in categories.keys()):
            categories[category] += t["amount"]
        else:
            categories[category] = t["amount"]
        ##total += 1

    # for (k,v) in categories.entries:
    #    categories[k] = v/total

    return categories

def generate_sales_data(auth_JWT, account_id):
    api = LoadApi(auth_JWT)
    transactions = api.get_user_all_transaction(account_id)["Transactions"]

    result = {}
    for transaction in transactions:
        for item in transaction.keys():
            if item not in result.keys():
                result[item] = []
            if item == "merchant":
                result[item].append(transaction[item]['name'])
            else:
                result[item].append(transaction[item])

    df = pd.DataFrame(result)

    fig, ax = plt.subplots(figsize=(12, 4))
    ax.axis('tight')
    ax.axis('off')
    the_table = ax.table(cellText=df.values, colLabels=df.columns, loc='center')
    # the_table.auto_set_font_size(False)
    # the_table.set_fontsize(2)

    pp = PdfPages("foo.pdf")
    pp.savefig(fig, bbox_inches='tight')
    pp.close()

    # {
    #         "transactionUUID": "0673bca4-fbb2-46bd-aa76-36243305ceed",
    #         "accountUUID": "72965642",
    #         "merchant": {
    #           "name": "Capital Two",
    #           "category": "Bills & Utilities",
    #           "description": "Credit Card Company",
    #           "pointOfSale": [
    #             "Online"
    #           ]
    #         },
    #         "amount": 843.92,
    #         "creditDebitIndicator": "Debit",
    #         "currency": "GBP",
    #         "timestamp": "2019-05-20 10:51:33",
    #         "emoji": "🤑",
    #         "latitude": -4.38849,
    #         "longitude": 52.33594,
    #         "status": "Successful",
    #         "message": "Weekly groceries shopping",
    #         "pointOfSale": "Online"
    #     },

load_dotenv()  # take environment variables from .env.
authJWT = os.environ['AUTH_JWT']
generate_sales_data(authJWT, "73680920")