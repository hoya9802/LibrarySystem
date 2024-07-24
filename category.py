import tkinter as tk
from add import BookAdd
from tkinter import messagebox
from bookList import BookList
from userList import UserList
from checkInOut import InOut

class CategoryWindow(tk.Tk):
    def __init__(self, NAME, AUTH, ID):
        super().__init__()
        self.NAME = NAME; self.AUTH = AUTH; self.ID = ID
        self.title('Main Page')
        self.geometry('340x440')
        self.configure(bg='#9999ff')

        self.frame = tk.Frame(self, bg='#333333')
        self.cat_label = tk.Label(
            self.frame, text='Category', bg='#333333', fg='#FF3399', font=('Arial', 30)
        )
        self.user_label = tk.Label(
            self.frame, text='Name: %s'%self.NAME, bg='#333333', fg='#FFFF33', font=('Arial', 15)
        )
        self.button1 = tk.Button(
            self.frame, text='1. 도서목록', bg='#333333', fg='#000000', font=('Arial', 20), command=BookList
        )
        self.button2 = tk.Button(
            self.frame, text='2. 도서추가', bg='#333333', fg='#000000', font=('Arial', 20), command=lambda: self.Check_Auth(BookAdd)
        )
        self.button3 = tk.Button(
            self.frame, text='3. 도서대여/반납', bg='#333333', fg='#000000', font=('Arial', 20), command=lambda: InOut(self.NAME, self.ID)
        )
        self.button4 = tk.Button(
            self.frame, text='4. 회원관리', bg='#333333', fg='#000000', font=('Arial', 20), command=lambda: self.Check_Auth(UserList)
        )

        self.cat_label.grid(row=0, column=0, columnspan=2, sticky='news', pady=40)
        self.user_label.grid(row=1, column=1, sticky='E')
        self.button1.grid(row=2, column=0, columnspan=2, sticky='news', pady=10)
        self.button2.grid(row=3, column=0, columnspan=2, sticky='news', pady=10)
        self.button3.grid(row=4, column=0, columnspan=2, sticky='news', pady=10)
        self.button4.grid(row=5, column=0, columnspan=2, sticky='news', pady=10)
        self.frame.pack()

        self.mainloop()

    def Check_Auth(self, cls):
        if self.AUTH == 'ADMIN':
            cls()
        else:
            messagebox.showerror(title='Access Fail', message='Access Deny')


if __name__ == '__main__':
    a = CategoryWindow('test', 'ADMIN', 'admin1')
