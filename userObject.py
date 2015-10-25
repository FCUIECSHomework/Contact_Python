class userObject:
    def __init__(self, jsonObject=None):
        self.name = jsonObject.get("name")
        self.line = jsonObject.get("line")
        self.Email = jsonObject.get("Email")
        self.uuid = jsonObject.get("uuid")
        self.telephone = jsonObject.get("telephone")

    def __str__(self):
        print(self.getUUID() + ":")
        print("Name:	" + self.getName())
        print("Email:	" + self.getEmail())
        print("Line:	" + self.GetLine())
        print("Telephone:")
        for phone in self.getTelephone():
            print("	" + phone)

    def __repr__(self):
        return self.__str__()

    def setName(self, name=None):
        if name is not None:
            self.name = name

    def setline(self, line=None):
        if line is not None:
            self.line = line

    def setEmail(self, Email=None):
        if Email is not None:
            self.Email = Email

    def addTelephone(self, telephone=None):
        if telephone is not None:
            self.telephone.add(telephone)

    def getName(self):
        return self.name

    def getLine(self):
        return self.line

    def getEmail(self):
        return self.Email

    def getUUID(self):
        return self.UUID

    def getTelephone(self):
        return self.telephone

    def printTelephone(self):
        for phone in self.telephone:
            print(phone)