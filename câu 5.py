print('sinh viên: VÕ THẾ HUY')
print('MSV: 235752021610031')
import tkinter as tk


root = tk.Tk()


v = tk.IntVar()
v.set(1) 
languages = [
    ("Python", 1),
    ("Perl", 2),
    ("Java", 3),
    ("C++", 4),
    ("C", 5)
]

def ShowChoice():
    print("Lựa chọn của bạn là:", v.get())


use_indicator = True  


tk.Label(root,
         text="""Choose your favourite
programming language:""",
         justify=tk.LEFT,
         padx=20).pack()


for language, val in languages:
    if use_indicator:
        # Dùng indicator (nút bấm thay vì radio button)
        tk.Radiobutton(root,
                       text=language,
                       indicatoron=0,  
                       width=20,       
                       padx=20,        
                       variable=v,
                       command=ShowChoice,
                       value=val).pack(anchor=tk.W)
    else:
        
        tk.Radiobutton(root,
                       text=language,
                       padx=20,
                       variable=v,
                       command=ShowChoice,
                       value=val).pack(anchor=tk.W)


root.mainloop()

