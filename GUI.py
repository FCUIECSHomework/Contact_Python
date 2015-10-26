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
                                                          Email=EmailEntry.get()))
        okButton.grid(column=0)
        cancelButton = Button(window, text="Cancel", command=window.destroy)
        cancelButton.grid(column=1)

    def addContact(self, window, **args):
        window.destroy()

    def loadContactsList(self):
        self.listBox.delete(0, END)
        jsonObject = JsonContact("test.json")
        nameList = []
        uuidList = []
        for i in jsonObject.jsonObject.values():
            nameList.append(i["name"])
            uuidList.append(i["uuid"])
        print(nameList)
        for i in range(0, len(nameList)):
            print(i)
            print(nameList[int(i)])
            self.listBox.insert(i, nameList[i])

    def showContactInfo(self, uuid=None):
        window = Toplevel(self)
        window.focus_set()
        window.title("Contact")
        theContact = JsonContact.getContact(uuid)
        name = Label(window, text="Name: " + theContact["name"])
        name.grid(row=0)
        line = Label(window, text="Line: " + theContact["line"])
        line.grid(row=1)
        Email = Label(window, text="Email: " + theContact["Email"])
        Email.grid(row=2)
        telephone = Label(window, text="Phone: ")
        telephone.grid(row=3, column=0)
        i = 4
        for pnumber in theContact["telephone"]:
            telephoneNumber = Label(window, text="        " + pnumber)
            telephoneNumber.grid(row=i)
            i += 1

        editButton = Button(window, text="Edit", command=lambda: window.destroy)
        editButton.grid(row=i + 1, column=0)
        deleteButton = Button(window, text="Delete", command=window.destroy)
        deleteButton.grid(row=i + 2, column=1)
        closeButton = Button(window, text="Close", command=window.destroy)
        closeButton.grid(row=i + 3, column=1)

    def poll(self):
        now = self.listBox.curselection()
        if now != self.current:
            self.listHasChanged(now)
            self.current = now
        self.after(250, self.poll)

    def listHasChanged(self, selection):
        print("selection is" + selection)
