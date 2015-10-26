from tkinter import *
from tkinter.scrolledtext import ScrolledText


class GUI(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        master.title("ContactsList")
        self.grid()
        self.listBox = Listbox(self).grid(row=0, column=0, columnspan=2)
        self.addButton = Button(self, text="Add Contact", command=self.addContactView()).grid(row=1, column=0)
        self.exitButton = Button(self, text="Exit", command=self.quit).grid(row=1, column=1)

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
                          command=self.addContact(name=nameEntry.get(), line=lineEntry.get(),
                                                  Email=EmailEntry.get()) and window.destroy)
        okButton.grid(column=0)
        cancelButton = Button(window, text="Cancel", command=window.destroy)
        cancelButton.grid(column=1)

    def addContact(self, **args):
        pass




