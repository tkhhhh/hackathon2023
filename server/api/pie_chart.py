def create_pie_chart_data(transactions):
    total = 0
    categories = {

    }
    for t in transactions:
        category = t["merchant"]["category"]
        if (category in categories.keys):
            categories[category] += 1
        else:
            categories[category] = 1
        total += 1

    for (k,v) in categories.entries:
        categories[k] = v/total

    return categories

    
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