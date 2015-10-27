from tkinter import *
from tkinter.scrolledtext import ScrolledText
from jsonContact import *


class GUI(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        master.title("ContactsList")
        self.grid()
        self.listBox = Listbox(self, width=50, selectmode=EXTENDED)
        self.listBox.grid(row=0, column=0, columnspan=2)
        self.addButton = Button(self, text="Add Contact", command=lambda: self.addContactView())
        self.addButton.grid(row=1, column=0)
        self.exitButton = Button(self, text="Exit", command=self.quit)
        self.exitButton.grid(row=1, column=1)
        self.uuidList = []
        self.jsonObject = None
        self.loadContactsList()
        self.current = None
        self.poll()

    def addContactView(self):
        window = Toplevel(self)
        window.focus_set()
        window.title("Add Contact")
        name = Label(window, text="Name ")
        name.grid(row=0, column=0)
        nameEntry = Entry(window, width=30)
        nameEntry.grid(row=0, column=1)
        line = Label(window, text="Line ")
        line.grid(row=1, column=0)
        lineEntry = Entry(window, width=30)
        lineEntry.grid(row=1, column=1)
        Email = Label(window, text="Email ")
        Email.grid(row=2, column=0)
        EmailEntry = Entry(window, width=30)
        EmailEntry.grid(row=2, column=1)
        telephone = Label(window, text="Phone ")
        telephone.grid(row=3, column=0)
        telephoneEntry = ScrolledText(window, width=37)
        telephoneEntry.grid(row=3, column=1)

        okButton = Button(window, text="Finish",
                          command=lambda: self.addContact(window, name=nameEntry.get(), line=lineEntry.get(),
                                                          Email=EmailEntry.get(), Telephone=telephoneEntry.get(1.0, END)))
        okButton.grid(column=0)
        cancelButton = Button(window, text="Cancel", command=window.destroy)
        cancelButton.grid(column=1)

    def addContact(self, window, **args):
        self.jsonObject.registerContact(name=args["name"], line=args["line"], Email=args["Email"], telephone=args["Telephone"])
        self.jsonObject = self.jsonObject.reload()
        window.destroy()

    def loadContactsList(self):
        self.listBox.delete(0, END)
        self.jsonObject = JsonContact("test.json")
        nameList = []
        for i in self.jsonObject.jsonObject.values():
            nameList.append(i["name"])
            self.uuidList.append(i["uuid"])
        for i in range(0, len(nameList)):
            self.listBox.insert(i, nameList[i])

    def showContactInfo(self, uuid=None):
        window = Toplevel(self)
        window.focus_set()
        window.title("Contact")
        theContact = self.jsonObject.getContact(uuid)
        name = Label(window, text="Name: ")
        name.grid(row=0, column=0)
        jsonName = Label(window, text=theContact.get('name'))
        jsonName.grid(row=0, column=1, columnspan=2)

        line = Label(window, text="Line: ")
        line.grid(row=1, column=0)
        jsonLine = Label(window, text=theContact.get('line'))
        jsonLine.grid(row=1, column=1, columnspan=2)

        Email = Label(window, text="Email: ")
        Email.grid(row=2, column=0)
        jsonEmail = Label(window, text=theContact.get('Email'))
        jsonEmail.grid(row=2, column=1, columnspan=2)


        telephone = Label(window, text="Phone: ")
        telephone.grid(row=3, column=0)
        i = 3
        for pnumber in theContact["telephone"]:
            telephoneNumber = Label(window, text=pnumber)
            telephoneNumber.grid(row=i, column=1, columnspan=2)
            i += 1

        editButton = Button(window, text="Edit", command=lambda: window.destroy)
        editButton.grid(row=i + 1, column=0)
        deleteButton = Button(window, text="Delete", command=window.destroy)
        deleteButton.grid(row=i + 1, column=1)
        closeButton = Button(window, text="Close", command=window.destroy)
        closeButton.grid(row=i + 1, column=2)

    def poll(self):
        now = self.listBox.curselection()
        if now != self.current:
            self.listHasChanged(now)
            self.current = now
        self.after(250, self.poll)

    def listHasChanged(self, selection):
        select = str(selection)[1]
        if select != ')':
            self.showContactInfo(self.uuidList[int(select)])

