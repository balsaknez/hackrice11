import requests

URL = "https://app-sandbox.bill.com"
USERNAME = "hackathons.ricebdc2021+user1@gmail.com"
PASSWORD = "Bill.com@Rice21"
DEVKEY = "01TPNONUZDOETDBFC644"
ORGID = "00801MJNMIGKVAUS206m"
SESSION_ID = ""
USERS_ID = ""


def login(device_id = ""):
    global SESSION_ID, USERS_ID
    query = {"userName": USERNAME, "password": PASSWORD, "orgId": ORGID, "devKey": DEVKEY, "device_id" : device_id}
    loginUrl = "/api/v2/Login.json"
    #print(query)
    response = requests.post(URL + loginUrl, data=query)
    data = response.json()
    #print(data)
    SESSION_ID = data['response_data']['sessionId']
    USERS_ID = data['response_data']['usersId']
