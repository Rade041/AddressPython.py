import tkinter as tk

small = ('Helvetica', 18)
large = ('Helvetica', 24)
Class AddressBookApp(tk.Tk):
    def __init__(self):
        self.title('Address Book')

        #creating widgets
        self.label = tk.Label(text='Addressbook', font=large)
        self.list = tk.Listbox(selectmode=tk.single, foint=small. width=30)
        self.entry = tk.Entry(font=small, width=30)
        self.add_btn = tk.Button(text="Contact List", font=large)
        self.update_btn = tk.Button(text="Update", font=large)
        self.delete_btn = tk.Button(text="Delete", font=large)
        self.add_btn = tk.Button(text="Add Contact", font=large)
        self.update_btn = tk.Button(text="Update", font=large)
        self.delete_btn = tk.Button(text="Delete", font=large)

