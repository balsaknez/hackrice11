import utility as util
import json
import requests
import jsonpickle
import twilio



class BillLineItem:
    

    def __init__(self,
                 amount,
                 entity="BillLineItem",
                 chartOfAccountId="",
                 departmentId="",
                 locationId="",
                 jobId="",
                 customerId="",
                 jobBillable=True,
                 description="",
                 itemId="",
                 quantity=1,
                 unitPrice=0,
                 employeeId="",
                 actgClassId=""
                 ):
        self.actgClassId = actgClassId
        self.employeeId = employeeId
        self.unitPrice = unitPrice
        self.quantity = quantity
        self.itemId = itemId
        self.description = description
        self.jobBillable = jobBillable
        self.customerId = customerId
        self.jobId = jobId
        self.locationId = locationId
        self.departmentId = departmentId
        self.chartOfAccountId = chartOfAccountId
        self.entity = entity
        self.amount = amount


class PayBills:

    urlCreate = "/api/v2/PayBills.json"

    def __init__(self,
                 vendorId,
                 bankAccountId="",
                 processDate="",
                 billPays=[],
                 billCredits=[]):
        # self.billCredits = billCredits
        self.billPays = billPays
        self.processDate = processDate
        self.bankAccountId = bankAccountId
        self.vendorId = vendorId

    def toJSON(self):
        return jsonpickle.encode( self.__dict__)
        # return json.dumps({"obj": self.__dict__})

    def create(self):
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        query = {"devKey": util.DEVKEY, "sessionId": util.SESSION_ID, "data": self.toJSON()}
        response = requests.post(util.URL + self.urlCreate, data=query, headers=headers)
        print(query)
        data = response.json()
        print(data)


class Bill:
    billMap = {}
    urlCreate = "/api/v2/Crud/Create/Bill.json"

    def __init__(self,
                 ourUserId,
                 vendorId,
                 invoiceNumber,
                 invoiceDate,
                 dueDate,
                 entity="Bill",
                 isSavings=False,
                 isPersonalAcct=True,
                 isActive="1",
                 glPostingDate="",
                 description="",
                 billLineItems=[]
                 ):
        self.ourUserId = ourUserId
        self.billLineItems = billLineItems
        self.description = description
        self.glPostingDate = glPostingDate
        self.isActive = isActive
        self.isPersonalAcct = isPersonalAcct
        self.isSavings = isSavings
        self.entity = entity
        self.dueDate = dueDate
        self.invoiceDate = invoiceDate
        self.invoiceNumber = invoiceNumber
        self.vendorId = vendorId
        self.id = ""
        self.amount = 0

    def toJSON(self):
        return jsonpickle.encode({"obj": self.__dict__})
        # return json.dumps({"obj": self.__dict__})

    def create(self):
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        query = {"devKey": util.DEVKEY, "sessionId": util.SESSION_ID, "data": self.toJSON()}
        response = requests.post(util.URL + self.urlCreate, data=query, headers=headers)
        data = response.json()
        print(data)
        self.id = data['response_data']['id']
        self.amount = data['response_data']['amount']
        Bill.billMap[self.id] = self.ourUserId

    def setBillApprover(self, approverId):

        urlSetApprovers = "/api/v2/SetApprovers.json"

        dict = {"objectId" : self.id,
                "entity" : "Bill",
                "approvers" : [approverId]}

        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        query = {"devKey": util.DEVKEY, "sessionId": util.SESSION_ID, "data": jsonpickle.encode(dict)}
        response = requests.post(util.URL + urlSetApprovers, data=query, headers=headers)
        data = response.json()
        print(data)

    def setBillApproverPolicy(self, amountThreshold = 4000, minNumApprovers = 1):
        urlSetApprovers = "/api/v2/Crud/Create/ApprovalPolicy.json"

        dict = {
                    "obj" :
                        {
                            "objectId": self.id,
                            "entity": "ApprovalPolicy",
                            "type": "0",
                            "amountThreshold" : amountThreshold,
                            "minNumApprovers" : minNumApprovers,
                            "isActive" : "1"
                        }
                }

        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        query = {"devKey": util.DEVKEY, "sessionId": util.SESSION_ID, "data": jsonpickle.encode(dict)}
        response = requests.post(util.URL + urlSetApprovers, data=query, headers=headers)
        data = response.json()
        print(data)

    def getBillsForUser(userId, vendId):
        urlList = "/api/v2/List/Bill.json"
        dict = {"start" : 0,
                "max" : 999}

        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        query = {"devKey": util.DEVKEY, "sessionId": util.SESSION_ID, "data": jsonpickle.encode(dict)}
        response = requests.post(util.URL + urlList, data=query, headers=headers)
        data = response.json()['response_data']

        billsForUser = []

        for i in data:
            try:
                if userId == Bill.billMap[i["id"]] and vendId == i["vendorId"]:
                    sum = 0
                    for item in i["billLineItems"]:
                        sum += float(item["amount"])
                    billsForUser.append({"billId" : i["id"] , "amount" : sum})
            except Exception:
                continue

        return billsForUser



class RecurringBillItem:
    def __init__(self,
                 amount,
                 entity = "RecurringBillLineItem",
                 chartOfAccountId = "",
                 departmentId = "",
                 locationId = "",
                 description = ""):
        self.description = description
        self.locationId = locationId
        self.departmentId = departmentId
        self.chartOfAccountId = chartOfAccountId
        self.entity = entity
        self.amount = amount

class RecurringBill:
    urlCreate = "/api/v2/Crud/Create/RecurringBill.json"

    def __init__(self,
                 vendorId,
                 timePeriod,
                 frequencyPerTimePeriod,
                 nextDueDate,
                 daysInAdvance,
                 recurringBillLineItems,
                 entity = "RecurringBill",
                 isActive = "1",
                 endDate = "",
                 description = "",
                 recurringBillItems = []
                 ):
        self.recurringBillItems = recurringBillItems
        self.description = description
        self.endDate = endDate
        self.isActive = isActive
        self.entity = entity
        self.recurringBillLineItems = recurringBillLineItems
        self.daysInAdvance = daysInAdvance
        self.nextDueDate = nextDueDate
        self.frequencyPerTimePeriod = frequencyPerTimePeriod
        self.timePeriod = timePeriod
        self.vendorId = vendorId

    def toJSON(self):
        return jsonpickle.encode({"obj": self.__dict__})
        # return json.dumps({"obj": self.__dict__})

    def create(self):
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        query = {"devKey": util.DEVKEY, "sessionId": util.SESSION_ID, "data": self.toJSON()}
        response = requests.post(util.URL + self.urlCreate, data=query, headers=headers)
        data = response.json()
        print(data)


