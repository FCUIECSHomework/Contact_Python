# coding=utf-8
from GUI import *
from tkinter.filedialog import askopenfilename

Tk().withdraw()
filename = askopenfilename(title="開啟通訊錄檔案", filetypes=[('通訊錄(Json)', ".json"), ('所有檔案', '.*')])
Tk().destroy()

if filename != '':
    root = Tk()
    root.resizable(width=FALSE, height=FALSE)
    app = GUI(master=root, file=filename)
    app.mainloop()
    app.focus_force()
