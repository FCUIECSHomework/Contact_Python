from tkinter import *
from tkinter.scrolledtext import ScrolledText
import tkinter.messagebox as messageBox
from tkinter.filedialog import *
from jsonContact import *


class GUI(Frame):
    def __init__(self, master=None, file=None):
        Frame.__init__(self, master)
        master.title("ContactsList")
        self.grid()
        self.listBox = Listbox(self, width=50)
        self.widgetInit()
        self.uuidList = []
        self.jsonObject = JsonContact(file)
        self.loadContactsList()
        self.current = None
        self.poll()

    def widgetInit(self):
        self.listBox.grid(row=0, column=0, columnspan=2)
        Button(self, text="Add Contact", command=lambda: self.addContactView()).grid(row=1, column=0)
        Button(self, text="Exit", command=self.quit).grid(row=1, column=1)

    def addContactView(self):
        window = Toplevel()
        window.focus_set()
        window.title("Add Contact")
        window.resizable(width=FALSE, height=FALSE)

        Label(window, text="Name ").grid(row=0, column=0)
        name = Entry(window, width=30)
        name.grid(row=0, column=1)

        Label(window, text="Line ").grid(row=1, column=0)
        line = Entry(window, width=30)
        line.grid(row=1, column=1)

        Label(window, text="Email ").grid(row=2, column=0)
        Email = Entry(window, width=30)
        Email.grid(row=2, column=1)

        Label(window, text="Phone ").grid(row=3, column=0)
        phone = ScrolledText(window, width=37)
        phone.grid(row=3, column=1)

        okButton = Button(window, text="Finish",
                          command=lambda: self.addContact(window, name=name.get(), line=line.get(), Email=Email.get(),
                                                          Telephone=phone.get(1.0, END)))
        okButton.grid(row=4)
        cancelButton = Button(window, text="Cancel", command=window.destroy)
        cancelButton.grid(row=4, column=1, sticky=E)

    def editContactView(self, infoWindow, Contact):
        window = Toplevel()
        window.focus_set()
        window.title("Edit Contact")
        window.resizable(width=FALSE, height=FALSE)

        Label(window, text="Name ").grid(row=0, column=0)
        name = Entry(window, width=30)
        name.grid(row=0, column=1)
        name.insert(0, Contact["name"])

        Label(window, text="Line ").grid(row=1, column=0)
        line = Entry(window, width=30)
        line.grid(row=1, column=1)
        line.insert(0, Contact["line"])

        Label(window, text="Email ").grid(row=2, column=0)
        Email = Entry(window, width=30)
        Email.grid(row=2, column=1)
        Email.insert(0, Contact["Email"])

        Label(window, text="Phone ").grid(row=3, column=0)
        telephone = ScrolledText(window, width=37)
        telephone.grid(row=3, column=1)
        for i in Contact["telephone"]:
            telephone.insert(INSERT, str(i) + "\n")

        okButton = Button(window, text="Finish",
                          command=lambda: self.editContact(window, infoWindow, uuid=Contact["uuid"], name=name.get(),
                                                           line=line.get(),
                                                           Email=Email.get(),
                                                           Telephone=telephone.get(1.0, END)))
        okButton.grid(row=4)
        cancelButton = Button(window, text="Cancel", command=window.destroy)
        cancelButton.grid(row=4, column=1, sticky=E)

    def showContactInfo(self, uuid=None):
        window = Toplevel()
        window.focus_set()
        window.title("Contact")
        window.resizable(width=FALSE, height=FALSE)
        theContact = self.jsonObject.getContact(uuid)

        Label(window, text="Name: ").grid(row=0, column=0)
        name = Label(window, text=theContact.get('name'), width=25)
        name.grid(row=0, column=1, columnspan=2)

        Label(window, text="Line: ").grid(row=1, column=0)
        line = Label(window, text=theContact.get('line'), width=25)
        line.grid(row=1, column=1, columnspan=2)

        Label(window, text="Email: ").grid(row=2, column=0)
        Email = Label(window, text=theContact.get('Email'), width=25)
        Email.grid(row=2, column=1, columnspan=2)

        Label(window, text="Phone: ").grid(row=3, column=0)
        i = 3
        for phone in theContact["telephone"]:
            Label(window, text=phone, width=25).grid(row=i, column=1, columnspan=2)
            i += 1

        editButton = Button(window, text="Edit", command=lambda: self.editContactView(window, theContact))
        editButton.grid(row=i + 1, column=0)
        deleteButton = Button(window, text="Delete", command=lambda: self.delContact(window, uuid))
        deleteButton.grid(row=i + 1, column=1)
        closeButton = Button(window, text="Close", command=window.destroy)
        closeButton.grid(row=i + 1, column=2)


    def addContact(self, window, **args):
        self.jsonObject.registerContact(name=args["name"], line=args["line"], Email=args["Email"],
                                        telephone=args["Telephone"])
        self.listReload()
        window.destroy()

    def delContact(self, theWindow, uuid=None):
        sure = messageBox.askokcancel(message="Make sure to delete?")
        if sure:
            self.jsonObject.removeContact(uuid)
            self.listReload()
            theWindow.destroy()

    def editContact(self, theWindow, infoWindow, **args):
        sure = messageBox.askokcancel(message="Make sure to edit?")
        if sure:
            theWindow.destroy()
            infoWindow.destroy()
            self.jsonObject.editContact(uuid=args["uuid"], name=args["name"], line=args["line"], Email=args["Email"],
                                        telephone=args["Telephone"])
            self.listReload()

    def loadContactsList(self):
        nameList = []
        self.uuidList = []
        for i in self.jsonObject.getAllContacts():
            nameList.append(i["name"])
            self.uuidList.append(i["uuid"])
        for i in range(0, len(nameList)):
            self.listBox.insert(i, nameList[i])

    def listReload(self):
        self.jsonObject = self.jsonObject.reload()
        del self.listBox
        self.listBox = Listbox(self, width=50)
        self.listBox.grid(row=0, column=0, columnspan=2)
        self.loadContactsList()


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
