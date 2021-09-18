import utility as util
import requests
import json


class VendorBankAccount():
    urlCreate = "/api/v2/Crud/Create/VendorBankAccount.json"

    def __init__(self,
                 vendorId,
                 accountNumber,
                 routingNumber,
                 usersId,
                 entity="VendorBankAccount",
                 isSavings=False,
                 isPersonalAcct=True,
                 isActive="1"
                 ):
        self.vendorId = vendorId
        self.accountNumber = accountNumber
        self.routingNumber = routingNumber
        self.usersId = usersId
        self.entity = entity
        self.isSavings = isSavings
        self.isPersonalAcct = isPersonalAcct
        self.isActive = isActive
        self.id = ""

    def toJSON(self):
        return json.dumps({"obj": self.__dict__})

    def create(self):
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        query = {"devKey": util.DEVKEY, "sessionId": util.SESSION_ID, "data": self.toJSON()}
        response = requests.post(util.URL + self.urlCreate, data=query, headers=headers)
        data = response.json()
        id = data['response_data']['id']
        # print(data)
