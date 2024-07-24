import tkinter as tk
from tkinter import ttk
from function import display_csv_data, search

class BookList(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Book Viewer')

        self.frame = tk.Frame(self)
        self.frame.pack(padx=20, pady=20, fill='both', expand=True)

        self.search_frame = tk.Frame(self.frame)
        self.search_frame.grid(row=0, column=0, sticky='ew', pady=10)
        
        self.search_label = tk.Label(self.search_frame, text="Search:")
        self.search_label.pack(side='left')
        
        self.search_entry = tk.Entry(self.search_frame)
        self.search_entry.pack(side='left', fill='x', expand=True)
        
        self.search_button = tk.Button(self.search_frame, text="Search", command=self.on_search_button_click)
        self.search_button.pack(side='right')
        
        self.tree = ttk.Treeview(self.frame, show='headings')
        self.tree.grid(row=1, column=0, sticky='news')

        self.scrollbar = ttk.Scrollbar(self.frame, orient="vertical", command=self.tree.yview)
        self.scrollbar.grid(row=1, column=1, sticky='ns')

        self.tree.configure(yscrollcommand=self.scrollbar.set)

        self.frame.grid_rowconfigure(1, weight=1)
        self.frame.grid_columnconfigure(0, weight=1)

        self.status_label = tk.Label(self, text="", padx=20, pady=10)
        self.status_label.pack()

        display_csv_data(self.tree, self.status_label, 'LibrarySystem/data/book.csv', 'Books')
        
        self.configure(bg='#9999ff')
        self.mainloop()

    def on_search_button_click(self):
        search(self.tree, self.search_entry, self.status_label)

if __name__ == '__main__':
    a = BookList()
