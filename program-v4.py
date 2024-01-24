import tkinter as tk
from tkinter import *
from customtkinter import *

def login_button():
    entered_username = username_entry.get()
    entered_password = password_entry.get()
    
    if entered_username == 'matt' and entered_password == 'pass':
        print()
    else:
        invalid_username_label = CTkLabel(root, text="Invalid username or password")
        invalid_username_label.grid(row=10, column=2, padx=10, pady=2)

root = tk.Tk()
root.title("ISMS Login")

root.geometry("800x400")
root.resizable(False, False)

warning_label = CTkLabel(root, text="Welcome to the ISMS system. \nUnauthorised access is strictly prohibited and can result in sever penalties. Please ensure you have permission to access this system")
warning_label.grid(row=0, column=2, padx=10, pady=2)

username_label = CTkLabel(root, text="Username:")
username_label.grid(row=3, column=2, padx=10, pady=2)
username_entry = CTkEntry(root)
username_entry.grid(row=4, column=2, pady=2)

password_label = CTkLabel(root, text="Password:")
password_label.grid(row=6, column=2, pady=2)
password_entry = CTkEntry(root, show='*')
password_entry.grid(row=7, column=2, pady=2)

login_button = CTkButton(root, text="Login", command=login_button)
login_button.grid(row=9, column=2, pady=2)

root.mainloop()
