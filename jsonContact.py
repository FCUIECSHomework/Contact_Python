import json
import uuid
from userObject import *

class JsonContact:
    def __init__(self, filename=None):
        self.jsonObject = None
        self.filename = filename
        self.loadJsonFile()

    def loadJsonFile(self):
        try:
            with open(self.filename) as jsonFile:
                self.jsonObject = json.load(jsonFile)
        except:
            print("Error: Fail to load JSON file. Does the file exist?")

    def writeJsonFile(self):
        try:
            with open(self.filename, 'w') as jsonFile:
                json.dump(self.jsonObject, jsonFile, sort_keys=False, indent=4)
        except:
            print("Error: Fail to write JSON file. Does the file exist?")
        self.loadJsonFile()

    def getAllKeys(self):
        return self.jsonObject.keys()

    def getAllContacts(self):
        self.writeJsonFile()
        userObjectArray = []
        for i in self.jsonObject.keys():
            userObjectArray.append(userObject(jsonObject=self.jsonObject.get(i)))
        return userObjectArray


    def registerContact(self, **contactElement):
        newContactUUID = uuid.uuid4()
        newContact = {}
        if "name" in contactElement:
            newContact.update({"name": contactElement["name"]})
        if "line" in contactElement:
            newContact.update({"line": contactElement["line"]})
        if "Email" in contactElement:
            newContact.update({"Email": contactElement["Email"]})
        if "telephone" in contactElement:
            newContact.update({"telephone": contactElement["telephone"]})
        newContact.update({"uuid": newContactUUID})
        self.jsonObject.update({newContactUUID: newContact})
        self.writeJsonFile()

    def removeContact(self, uuid=None):
        self.jsonObject.pop(uuid)
        self.writeJsonFile()

    def editContact(self, uuid=None, **contactElement):
        if uuid not in self.jsonObject:
            print("Error: No User Found!Wrong UUID?")
        else:
            if "name" in contactElement:
                self.jsonObject[uuid]["name"] = contactElement["name"]
            if "line" in contactElement:
                self.jsonObject[uuid]["line"] = contactElement["line"]
            if "Email" in contactElement:
                self.jsonObject[uuid]["Email"] = contactElement["Email"]
            if "telephone" in contactElement:
                self.jsonObject[uuid]["telephone"] = contactElement["telephone"]
            self.writeJsonFile()
