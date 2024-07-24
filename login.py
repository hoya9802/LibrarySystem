import tkinter as tk
import pandas as pd
import category
from tkinter import messagebox

class LoginApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Login Form')
        self.geometry('340x440')
        self.configure(bg='#9999ff')

        self.frame = tk.Frame(self, bg='#333333')
        
        self.login_label = tk.Label(
            self.frame, text='Library System', bg='#333333', fg='#FF3399', font=('Arial', 30)
        )
        self.username_label = tk.Label(
            self.frame, text='User ID', bg='#333333', fg='#FFFF33', font=('Arial', 16)
        )
        self.username_entry = tk.Entry(
            self.frame, fg='#FFFFFF', font=('Arial', 16)
        )
        self.password_label = tk.Label(
            self.frame, text='Password', fg='#FFFF33', font=('Arial', 16)
        )
        self.password_entry = tk.Entry(
            self.frame, show='*', font=('Arial', 16)
        )
        self.click_button = tk.Button(
            self.frame, text='Login', font=('Arial', 16), command=self.login
        )
        self.version_label = tk.Label(
            self.frame, text='Version: 1.0', bg='#333333', fg='#FFFFFF', font=('Arial', 10)
        )

        self.login_label.grid(row=0, column=0, columnspan=2, sticky='news', pady=40)
        self.username_label.grid(row=1, column=0)
        self.username_entry.grid(row=1, column=1, pady=10)
        self.password_label.grid(row=2, column=0)
        self.password_entry.grid(row=2, column=1, pady=20)
        self.click_button.grid(row=3, column=0, columnspan=2, pady=20)
        self.version_label.grid(row=4, column=1, sticky='E')

        self.frame.pack()
        self.mainloop()

    def login(self):
        csv_id = pd.read_csv('LibrarySystem/data/ID.csv')
        check = [self.username_entry.get(), "'" + self.password_entry.get() + "'"]
        for d in csv_id.values:
            if check in d[:2]:
                category.CategoryWindow(d[2], d[5], d[0])
                break
        else:
            messagebox.showerror(title='Login Fail', message='Try Again')

if __name__ == '__main__':
    a = LoginApp().mainloop()