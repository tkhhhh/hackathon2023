from server.api_service.load_api import LoadApi
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

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

def generate_pie_chart(auth_JWT, account_id):
    categories = create_pie_chart_data(auth_JWT, account_id)
    pp = PdfPages('long.pdf')
    fig = plt.figure(3, figsize=(4, 4))
    ax = plt.axes([0.1, 0.1, 0.8, 0.8])
    for x in categories.keys():
        ax.cla()
        labels = x
        fracs = categories[x]
        p = plt.pie(fracs, labels=labels)
        fig.savefig(pp, format='pdf')
    pp.close()
    return {}
    
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
