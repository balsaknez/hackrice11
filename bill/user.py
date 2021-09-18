import jsonpickle
import utility as util
import requests


class UserProfile:
    urlRead = "/api/v2/List/Profile.json"

    def __init__(self):
        self.start = 0
        self.max = 999

    def toJSON(self):
        return jsonpickle.encode(self.__dict__)

    def getUserProfileId(self):
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        query = {"devKey": util.DEVKEY, "sessionId": util.SESSION_ID, "data": self.toJSON()}
        response = requests.post(util.URL + self.urlRead, data=query, headers=headers)
        data = response.json()
        return data['response_data'][0]['id'] # returning approver userprofile id


class User:
    urlCreate = "/api/v2/Crud/Create/User.json"

    def __init__(self,
                 profileId,
                 firstName,
                 lastName,
                 email,
                 isActive="1",
                 timezoneId="3",
                 entity = "User"):
        self.entity = entity
        self.timezoneId = timezoneId
        self.isActive = isActive
        self.email = email
        self.lastName = lastName
        self.firstName = firstName
        self.profileId = profileId
        self.id = ""

    def toJSON(self):
        #return jsonpickle.encode(self.__dict__)
        return jsonpickle.encode({"obj": self.__dict__})

    def create(self):
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        query = {"devKey": util.DEVKEY, "sessionId": util.SESSION_ID, "data": self.toJSON()}
        response = requests.post(util.URL + self.urlCreate, data=query, headers=headers)
        print(query)
        data = response.json()
        print(data)
        self.id = data['response_data']['id']
