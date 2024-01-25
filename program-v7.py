### Importing tkinter and customtkinter modules. 
import tkinter as tk
from tkinter import *
from customtkinter import *

### Create login button logic as function for when button is 'clicked'
def login_button():
    global invalid_username_label
    global entered_username
    ### Obtaining username and password from entry fields once button has been 'Clicked'
    entered_username = username_entry.get()
    entered_password = password_entry.get()
    
    ### Verifying username and password
    if entered_username == 'matt' and entered_password == 'pass':
        open_dashboard_page()     
    else:
        ### Add error message, use grid to pop up below password entry box by adding an additional row
        invalid_username_label = CTkLabel(root, text="Error. You have entered an invalid username/password or your account has been disabled. \nPlease contact an administrator for further support.")
        invalid_username_label.grid(row=10, column=2, padx=10, pady=2)

def open_dashboard_page():
    ### To avoid creating a class and using frames or using root withdraw/destroy and loading a new page. an approach to remove all grid items then repopulate new items has been decided here as the function logic
    warning_label.grid_forget()
    username_label.grid_forget()
    username_entry.grid_forget()
    password_label.grid_forget()
    password_entry.grid_forget()
    login_button.grid_forget()
    invalid_username_label.grid_forget()

    dashboard_title = CTkLabel(root, text=f"Dashboard Page")
    dashboard_title.grid(row=1, column=2, padx=10, pady=2)

    dashboard_greeting_message = CTkLabel(root, text=f"Welcome to the dashboard {entered_username}.")
    dashboard_greeting_message.grid(row=2, column=2, padx=10, pady=2)

    users_in_system_label = CTkLabel(root, text="There is X items outstanding")
    users_in_system_label.grid(row=3, column=2, padx=10, pady=2)

    users_in_system_label = CTkLabel(root, text="36 users in the system")
    users_in_system_label.grid(row=1, column=3, padx=10, pady=2)
   
    assets_in_system_label = CTkLabel(root, text="22 assets in the system")
    assets_in_system_label.grid(row=2, column=3, padx=10, pady=2, sticky="nsew")

    logout_button = CTkButton(root, text="Logout")
    logout_button.grid(row=1, column=1, pady=2)

### root variable for loading tkinter window with title
root = tk.Tk()
root.title("ISMS Login")

### Resolution with boolean resizable values
root.geometry("800x400")
root.resizable(False, False)

### customtkinter label and text displaying welcome and warning message.
warning_label = CTkLabel(root, text="Welcome to the ISMS system. \nUnauthorised access is strictly prohibited and can result in sever penalties. Please ensure you have permission to access this system")
warning_label.grid(row=0, column=2, padx=10, pady=2)

### customtkinter label and text displaying enter username message.
username_label = CTkLabel(root, text="Username:")
username_label.grid(row=3, column=2, padx=10, pady=2)
username_entry = CTkEntry(root)
username_entry.grid(row=4, column=2, pady=2)

### customtkinter label and text displaying enter password message.
password_label = CTkLabel(root, text="Password:")
password_label.grid(row=6, column=2, pady=2)
password_entry = CTkEntry(root, show='*')
password_entry.grid(row=7, column=2, pady=2)

### customtkinter login button calling login_button function with command function.
login_button = CTkButton(root, text="Login", command=login_button)
login_button.grid(row=9, column=2, pady=2)

### Run the tkinter program
root.mainloop()
