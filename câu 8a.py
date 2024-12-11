print('sinh viên: VÕ THẾ HUY')
print('MSV: 235752021610031')
from tkinter import *

def create_personal_info_form():
    root = Tk()
    root.title("Personal Information")

    Label(root, text="Họ và tên:", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=5, sticky=W)
    Entry(root, width=30).grid(row=0, column=1, padx=10, pady=5)

    Label(root, text="Ngày tháng năm sinh:", font=("Arial", 12)).grid(row=1, column=0, padx=10, pady=5, sticky=W)
    Entry(root, width=30).grid(row=1, column=1, padx=10, pady=5)

    Label(root, text="MSSV:", font=("Arial", 12)).grid(row=2, column=0, padx=10, pady=5, sticky=W)
    Entry(root, width=30).grid(row=2, column=1, padx=10, pady=5)

    Label(root, text="Ngành học:", font=("Arial", 12)).grid(row=3, column=0, padx=10, pady=5, sticky=W)
    Entry(root, width=30).grid(row=3, column=1, padx=10, pady=5)

    Button(root, text="Thoát", command=root.quit, font=("Arial", 12)).grid(row=4, column=1, pady=10)

    root.mainloop()

create_personal_info_form()
