import csv
import tkinter as tk
from tkinter import messagebox

class BookAdd(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Add Book')
        self.geometry('340x440')
        self.configure(bg='#9999ff')
        self.frame = tk.Frame(self, bg='#333333')
        self.btn_frame = tk.Frame(self, bg='#333333')
        self.btn_width = 5
        self.file_path = 'LibrarySystem/data/book.csv'

        self.add_label = tk.Label(
            self.frame, text='Add/Delete', bg='#333333', fg='#FF3399', font=('Arial', 30)
        )
        self.ISBN_label = tk.Label(
            self.frame, text='ISBN', bg='#333333', fg='#FFFFFF', font=('Arial', 16)
        )
        self.ISBN_entry = tk.Entry(
            self.frame, fg='#FFFFFF', font=('Arial', 16)
        )
        self.book_title = tk.Label(
            self.frame, text='NAME', bg='#333333', fg='#FFFFFF', font=('Arial', 16)
        )
        self.book_entry = tk.Entry(
            self.frame, fg='#FFFFFF', font=('Arial', 16)
        )
        self.author_label = tk.Label(
            self.frame, text='AUTHOR', bg='#333333', fg='#FFFFFF', font=('Arial', 16)
        )
        self.author_entry = tk.Entry(
            self.frame, fg='#FFFFFF', font=('Arial', 16)
        )
        self.pub_label = tk.Label(
            self.frame, text='PUBLISHER', bg='#333333', fg='#FFFFFF', font=('Arial', 16)
        )
        self.pub_entry = tk.Entry(
            self.frame, fg='#FFFFFF', font=('Arial', 16)
        )
        self.price_label = tk.Label(
            self.frame, text='PRICE', bg='#333333', fg='#FFFFFF', font=('Arial', 16)
        )
        self.price_entry = tk.Entry(
            self.frame, fg='#FFFFFF', font=('Arial', 16)
        )
        self.status_label = tk.Label(
            self.frame, text='STATUS', bg='#333333', fg='#FFFFFF', font=('Arial', 16)
        )
        self.status_entry = tk.Entry(
            self.frame, fg='#FFFFFF', font=('Arial', 16)
        )
        self.add_btn = tk.Button(
            self.btn_frame, text='Add', font=('Arial', 16), width=self.btn_width, command=self.Add
        )
        self.back_btn = tk.Button(
            self.btn_frame, text='Back', font=('Arial', 16), width=self.btn_width, command=self.Back
        )
        self.del_btn = tk.Button(
            self.btn_frame, text='Delete', font=('Arial', 16), width=self.btn_width, command=self.Delete
        )

        self.add_label.grid(row=0, column=0, columnspan=2, sticky='news', pady=40)
        self.ISBN_label.grid(row=1,column=0, sticky='W'); self.ISBN_entry.grid(row=1, column=1)
        self.book_title.grid(row=2, column=0, sticky='W'); self.book_entry.grid(row=2, column=1)
        self.author_label.grid(row=3, column=0, sticky='W'); self.author_entry.grid(row=3, column=1)
        self.pub_label.grid(row=4, column=0, sticky='W'); self.pub_entry.grid(row=4, column=1)
        self.price_label.grid(row=5, column=0, sticky='W'); self.price_entry.grid(row=5, column=1)
        self.status_label.grid(row=6, column=0, sticky='W'); self.status_entry.grid(row=6, column=1)

        self.del_btn.grid(row=1, column=0, padx= 8,pady=10)
        self.back_btn.grid(row=1, column=1, padx= 7,pady=10)
        self.add_btn.grid(row=1, column=2, padx= 8,pady=10)

        self.frame.pack()
        self.btn_frame.pack()

        self.mainloop()
    
    def Add(self):
        f = open(self.file_path)
        data = csv.reader(f)
        data = list(data)
        check = [self.ISBN_entry.get(), self.book_entry.get(), self.author_entry.get(), self.pub_entry.get(), self.price_entry.get(), self.status_entry.get()]
        if check in data:
            messagebox.showerror(title='Add Fail', message='The book you want to add already exists.')
        else:
            check = [x for x in check if len(x) > 0]
            if len(check) == len(data[0]):
                with open(self.file_path, 'a', newline='\n', encoding='utf-8') as f:
                    wr = csv.writer(f)
                    wr.writerow(check)
                messagebox.showinfo(title='Add Success', message='Successfully added.')
            else:
                messagebox.showerror(title='Add Fail', message='Fill in all the blanks')

    def Delete(self):
        f = open(self.file_path)
        data = csv.reader(f)
        data = list(data)
        check = [self.ISBN_entry.get(), self.book_entry.get(), self.author_entry.get(), self.pub_entry.get(), self.price_entry.get(), self.status_entry.get()]
        if check not in data:
            messagebox.showerror(title='Delete Fail', message="The book you want to delete doesn't exists.")
        else:
            rows_to_keep = [row for row in data if row != check]

            with open(self.file_path, 'w', newline='\n', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerows(rows_to_keep)
            messagebox.showinfo(title='Delete Success', message='Successfully Deleted.')

    def Back(self):
        self.destroy()

if __name__ == '__main__':
    a = BookAdd()