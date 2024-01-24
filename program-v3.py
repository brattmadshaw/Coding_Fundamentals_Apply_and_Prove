import tkinter as tk
from tkinter import *
from customtkinter import *

print("Welcome to the ISMS system. Unauthorised access is strictly prohibited and can result in sever penalties. Please ensure you have permission to access this system")

username = input("Please enter your username: ")
password = input("Please enter your password: ")

if username == 'matt' and password == 'pass':
    print("Login correct")
    print("Welcome to the ISMS Dashboard")
else:
    ("Invalid username or password.")

root = tk.Tk()
root.title("ISMS Login")

username_label = tk.Label(root, text="Username:")
username_label.grid()
username_entry = tk.Entry(root)
username_entry.grid()

password_label = tk.Label(root, text="Password:")
password_label.grid()
password_entry = tk.Entry(root)
password_entry.grid()

login_button = tk.Button(root, text="Login")
login_button.grid()

root.mainloop()
