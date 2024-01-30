import tkinter as tk
from tkinter import *
from tkinter import ttk
import subprocess
import main
from main import *

flat = tk.FLAT
sunken = tk.SUNKEN
raised = tk.RAISED
groove = tk.GROOVE
ridge = tk.RIDGE

def register_page():
    print("nothing")

def get_auth_code_and_verify():
    auth_code = auth_code_entry.get()
    print("fetched", auth_code)
    print(main.random_code, "test")

    if main.random_code == auth_code:
        access_granted_window = tk.Tk()
        access_granted_window.title("Access Control")
        access_granted_message = tk.Label(
            master=access_granted_window,
            text="Access Granted",
            fg="white",
            bg="black",
            width=20,
            height=3,
            relief=ridge,
            borderwidth=2
        )
        access_granted_message.pack()
        access_granted_window.after(5000, lambda:access_granted_window.destroy())
        print("correct")
    else:
        error_window = tk.Tk()
        error_window.title("Access Control")
        error_message = tk.Label(
            master=error_window,
            text="Incorrect Code!",
            fg="white",
            bg="black",
            width=20,
            height=3,
            relief=ridge,
            borderwidth=2
        )
        error_message.pack()
        error_window.after(5000, lambda:error_window.destroy())

auth_window = tk.Tk()
auth_window.title("Admin Authentication Page")
auth_title_frame = tk.Frame(master=auth_window, bg="black")
auth_entry_frame = tk.Frame(master=auth_window, bg="black")

auth_title = tk.Label(
    master=auth_title_frame,
    text="Please enter admin passcode below.",
    fg="white",
    bg="#004c9e",
    width=31,
    height=3,
    relief=ridge,
    borderwidth=2
)

auth_subtitle = tk.Label(
    master=auth_entry_frame,
    text="AuthCode: ",
    fg="white",
    bg="black",
    width=10,
    height=1,
    bd=4,
    borderwidth=2
)

auth_code_entry = tk.Entry(
    master=auth_entry_frame,
    bg="black",
    bd=4,
    cursor="arrow",
    fg="white",
    borderwidth=2,
    # show="*"
)

submit_button = tk.Button(
    master=auth_entry_frame,
    text="Submit",
    fg="white",
    bg="#6600ff",
    height=2,
    width=20,
    command=get_auth_code_and_verify
)

auth_title_frame.grid(row=1, column=1, padx=4, pady=4)
auth_entry_frame.grid(row=2, column=1, padx=4, pady=4)
auth_subtitle.grid(row=1, column=1, padx=4, pady=4)
auth_code_entry.grid(row=1, column=2, padx=4, pady=4)
submit_button.grid(row=1, column=3, padx=4, pady=4)
auth_title.pack()

auth_window.mainloop()