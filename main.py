# coding=utf-8
import jsonContact as jc


def printSelectTable():
    print("	(1)List Contact")
    print("	(2)New Contact")
    print("	(3)Edit Contact")
    print("	(4)Delete Contact")
    print("	(5)Exit")
    print("input your select:", end=" ")


while True:
    ContactsList = jc.JsonContact("test.json")
    printSelectTable()
    select = input()
    if select == '1':
        userObjectArray = ContactsList.getAllContacts()
        for userObject in userObjectArray:
            print(userObject)
    elif select == '2':
        print("Please input user data:")
        name = input("Name: ")
        line = input("Line: ")
        Email = input("Email: ")
        telephone = []
        while True:
            pnumber = input("Telephone(-1 to stop): ")
            if pnumber != '-1':
                telephone.append(pnumber)
            else:
                break
        ContactsList.registerContact(name=name, line=line, Email=Email, telephone=telephone)
    elif select == '3':
        uuid = input("Please input user uuid: ")
        name = input("Name: ")
        line = input("Line: ")
        Email = input("Email: ")
        telephone = []
        while True:
            pnumber = input("Telephone(-1 to stop): ")
            if pnumber != '-1':
                telephone.append(pnumber)
            else:
                break
        ContactsList.editContact(uuid, name=name, line=line, Email=Email, telephone=telephone)
    elif select == '4':
        uuid = input("uuid: ")
        ContactsList.removeContact(uuid)
    elif select == '5':
        break
    else:
        print("Please recheck your input!")