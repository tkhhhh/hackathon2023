class TextFormat(object):

    def __init__(self, data):
        self.accountID = data["accountID"]
        self.purpose = data["purpose"]
        self.purposes = ["report during month", "report during week", "balance", "predicted costing"]

    def analyse_purpose(self):
        for purpose in self.purposes:
            if purpose in self.purpose.contain:
                return 1
        return -1

