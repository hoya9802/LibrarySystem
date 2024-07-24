import csv
import tkinter as tk
from function import change_value, csv_to_list
from tkinter import messagebox
from tkinter import ttk
from datetime import datetime, timedelta

class InOut(tk.Tk):
    def __init__(self, NAME, ID):
        super().__init__()
        self.title('')
        self.NAME = NAME; self.ID = ID
        self.file_path = 'LibrarySystem/data/check_in_out.csv'
        self.book_path = 'LibrarySystem/data/book.csv'
        self.btn_width = 6
        self.b_list = []

        self.frame = tk.Frame(self)
        self.frame.pack(padx=20, pady=20, fill='both', expand=True)

        self.search_frame = tk.Frame(self.frame)
        self.search_frame.grid(row=0, column=0, sticky='ew', pady=10)
        
        self.search_label = tk.Label(self.search_frame, text="BOOK ISBN:")
        self.search_label.pack(side='left')

        self.search_entry = tk.Entry(self.search_frame)
        self.search_entry.pack(side='left', fill='x', expand=True)

        self.tree = ttk.Treeview(self.frame, show='headings')
        self.tree.grid(row=1, column=0, sticky='news')

        self.scrollbar = ttk.Scrollbar(self.frame, orient="vertical", command=self.tree.yview)
        self.scrollbar.grid(row=1, column=1, sticky='ns')

        self.tree.configure(yscrollcommand=self.scrollbar.set)

        self.frame.grid_rowconfigure(1, weight=1)
        self.frame.grid_columnconfigure(0, weight=1)

        self.status_label = tk.Label(self, text="", padx=20, pady=10, width=17)
        self.status_label.pack()

        self.btn_frame = tk.Frame(self)
        self.in_btn = tk.Button(self.btn_frame, text='Check in', font=('Arial', 16), width=self.btn_width, command=self.check_in)
        self.out_btn = tk.Button(self.btn_frame, text='Check out', font=('Arial', 16), width=self.btn_width, command=self.check_out)
        self.in_btn.grid(row=0, column=1, padx=5)
        self.out_btn.grid(row=0, column=0, padx=3)
        self.btn_frame.pack()

        self.display_csv()
        self.configure(bg='#9999ff')
        self.mainloop()

    def display_csv(self):
        cnt = 0
        try:
            with open(self.file_path, 'r', newline='') as f:
                csv_reader = csv.reader(f)
                header = next(csv_reader)
                self.tree.delete(*self.tree.get_children())
                self.tree["columns"] = header
                for col in header:
                    self.tree.heading(col, text=col)
                    self.tree.column(col, width=120)
                for row in csv_reader:
                    if row[0] == self.ID:
                        cnt += 1
                        self.b_list.append(row)
                        self.tree.insert("", "end", values=row)
                self.status_label.config(text=f"{self.NAME}'s borrowed {cnt} books")
        except Exception as e:
            self.status_label.config(text=f"Error Code: {str(e)}")

    def check_in(self):
        csv_list = csv_to_list(self.file_path)
        get_num = self.search_entry.get()
        if get_num in [x[1] for x in self.b_list]:
            rows_to_keep = [row for row in csv_list if get_num not in row]
            with open(self.file_path, 'w', newline='\n', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerows(rows_to_keep)

            change_value(self.book_path, get_num, 'available')

            messagebox.showinfo(title='CheckIn success', message='Successfully check in')
        else:
            messagebox.showerror(title='CheckIn Fail', message='Try to check ISBN again')

    def check_out(self):
        get_num = self.search_entry.get()
        if self.search_entry.get() in [x[1] for x in self.b_list]:
            messagebox.showerror(title='CheckOut Fail', message="You've already checked out this book")
        else:
            data = csv_to_list(self.book_path)
            for d in data[1:]:
                if get_num == d[0] and d[-1] == 'available':
                    today = datetime.today()
                    seven_days_later = today + timedelta(days=14)
                    with open(self.file_path, 'a', newline='\n', encoding='utf-8') as f:
                        wr = csv.writer(f)
                        wr.writerow([self.ID, self.search_entry.get(), seven_days_later.strftime("%Y-%m-%d")])
                    
                    change_value(self.book_path, get_num, 'unavailable')
                    messagebox.showinfo(title='CheckOut success', message='Successfully check out')    
                    break
            else:
                messagebox.showerror(title='CheckOut Fail', message="ISBN doesn't exist.")

if __name__ == '__main__':
    a = InOut('Charlotte','user30')
