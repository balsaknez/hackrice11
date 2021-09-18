import requests
import json
import utility as util


class Vendor:
    urlCreate = '/api/v2/Crud/Create/Vendor.json'

    def __init__(self,
                 name,
                 entity="Vendor",
                 isActive="",
                 shortName="",
                 nameOnCheck="",
                 companyName="",
                 accNumber="",
                 taxId="",
                 track1099=False,
                 address1="",
                 address2="",
                 address3="",
                 address4="",
                 addressCity="",
                 addressState="",
                 addressZip="",
                 addressCountry="",
                 email="",
                 fax="",
                 phone="",
                 paymentEmail="",
                 paymentPhone="",
                 description="",
                 contactFirstName="",
                 contactLastName="",
                 accountType=""
                 ):
        self.entity = entity
        self.name = name
        self.accountType = accountType
        self.contactLastName = contactLastName
        self.contactFirstName = contactFirstName
        self.description = description
        self.paymentPhone = paymentPhone
        self.paymentEmail = paymentEmail
        self.phone = phone
        self.fax = fax
        self.email = email
        self.addressCountry = addressCountry
        self.addressZip = addressZip
        self.addressState = addressState
        self.addressCity = addressCity
        self.address4 = address4
        self.address3 = address3
        self.address2 = address2
        self.address1 = address1
        self.track1099 = track1099
        self.taxId = taxId
        self.accNumber = accNumber
        self.companyName = companyName
        self.nameOnCheck = nameOnCheck
        self.shortName = shortName
        self.isActive = isActive
        self.id = ""

    def toJSON(self):
        return json.dumps({"obj": self.__dict__})

    def create(self):
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        query = {"devKey": util.DEVKEY, "sessionId": util.SESSION_ID, "data": self.toJSON()}
        response = requests.post(util.URL + self.urlCreate, data=query, headers=headers)
        data = response.json()
        self.id = data['response_data']['id']
        self.isActive = "1"
        self.nameOnCheck = self.name


me = Vendor(name='asd')
util.login()
me.create()
