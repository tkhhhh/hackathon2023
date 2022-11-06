class TextFormat(object):

    def __init__(self, data):
        self.accountID = data["accountID"]
        self.purpose = data["purpose"]
        self.purposes = [{
            "purpose_url": "/api/report/transactions",
            "purpose": "transactions report",
            "param": {
                "accountID": self.accountID
            }
        },
            {
                "purpose_url": "/api/report/pie",
                "purpose": "transactions report pie",
                "param": {
                    "accountID": self.accountID
                }
            }
                         ]

    def analyse_purpose(self):
        distance = 999999
        result = {}
        for purpose in self.purposes:
            if abs(self.lv_number(purpose["purpose"], self.purpose)) < distance:
                distance = abs(self.lv_number(purpose["purpose"], self.purpose))
                result = purpose
        return result

    def lv_number(self, a, b):
        string1 = a
        string2 = b
        distance = 0
        n1 = len(string1)
        n2 = len(string2)
        if n1 >= n2:
            for i in range(n1):
                if i < n2:
                    if string1[i] != string2[i]:
                        distance += 1
                else:
                    distance += 1
        else:
            for i in range(n2):
                if i < n1:
                    if string2[i] != string1[i]:
                        distance -= 1
                else:
                    distance -= 1
        return distance
