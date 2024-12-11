print('sinh viên: VÕ THẾ HUY')
print('MSV: 235752021610031')
from tkinter import *

def NewFile():
    print("New File!") 
    lbl_message.config(text="You selected: New File!") 

def OpenFile():
    print("Open File!")
    lbl_message.config(text="You selected: Open File!")

def ExitApp():
    print("Exit Application!")
    lbl_message.config(text="You selected: Exit Application!")
    root.quit()

def InsText():
    print("Insert Text!")
    lbl_message.config(text="You selected: Insert Text!")

def InsPic():
    print("Insert Picture!")
    lbl_message.config(text="You selected: Insert Picture!")

def About():
    print("This is a simple example of a menu")
    lbl_message.config(text="You selected: About...")

root = Tk()
root.title("Menu Example")

menu = Menu(root)
root.config(menu=menu)

filemenu = Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New", command=NewFile)
filemenu.add_command(label="Open", command=OpenFile)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=ExitApp)

insertmenu = Menu(menu, tearoff=0)
menu.add_cascade(label="Insert", menu=insertmenu)
insertmenu.add_command(label="Text", command=InsText)
insertmenu.add_command(label="Picture", command=InsPic)

helpmenu = Menu(menu, tearoff=0)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=About)

lbl_message = Label(root, text="Welcome!", font=("Arial", 14), pady=20)
lbl_message.pack()

root.mainloop()
