# coding=utf-8
from GUI import *


Tk().withdraw()
result = messageBox.askquestion("開啟通訊錄", "是否已經有通訊錄檔案？\n按下「是」來開啟檔案；按下「否」來使用空白的通訊錄！", icon='question')
if result == "yes":
    filename = askopenfilename(title="開啟通訊錄檔案", filetypes=[('通訊錄(Json)', ".json"), ('所有檔案', '.*')])
else:
    filename = asksaveasfilename(title="另存通訊錄", filetypes=[('通訊錄(Json)', ".json"), ('所有檔案', '.*')])
    if filename != '':
        if filename[:-4:] != ".json":
            filename += ".json"
        with open(filename, 'w') as file:
            json.dump(dict(), file)
            file.close()
Tk().destroy()

if filename != '':
    root = Tk()
    root.resizable(width=FALSE, height=FALSE)
    app = GUI(master=root, file=filename)
    app.mainloop()
    app.focus_force()
