print('sinh viên: VÕ THẾ HUY')
print('MSV: 235752021610031')
from tkinter import *

window = Tk()
window.title("Welcome to LikeGeeks app")  
window.geometry('350x200') 

lbl = Label(window, text="Hello")
lbl.grid(column=0, row=0) 

def clicked():
    lbl.configure(text="Button was clicked !!")

btn = Button(window, text="Click Me", command=clicked, bg="blue", fg="white")
btn.grid(column=1, row=0)  # Đặt Button tại vị trí (1, 0)

def key_pressed(event):
    lbl.configure(text=f"Key '{event.char}' was pressed!")

window.bind('<Key>', key_pressed)

window.mainloop()
