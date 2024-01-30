import tkinter as tk

flat = tk.FLAT
sunken = tk.SUNKEN
raised = tk.RAISED
groove = tk.GROOVE
ridge = tk.RIDGE

left = tk.LEFT
right = tk.RIGHT
top = tk.TOP
bottom = tk.BOTTOM

login_window = tk.Tk()
login_window.title("SecuNet Login Page")
login_frame = tk.Frame(master=login_window, bg="black")
username_frame = tk.Frame(master=login_window, bg="black")
password_frame = tk.Frame(master=login_window, bg="black")

login_title = tk.Label(
    master=login_frame,
    text="Please enter your username and password below.",
    fg="white",
    bg="#004c9e",
    width=38,
    height=3,
    relief=ridge,
    borderwidth=2
)

username_title = tk.Label(
    master=username_frame,
    text="username: ",
    fg="white",
    bg="black",
    width=10,
    height=1,
    bd=4,
    borderwidth=2
)

username_entry = tk.Entry(
    master=username_frame,
    bg="black",
    bd=4,
    cursor="arrow",
    fg="white",
    borderwidth=2
)

password_title = tk.Label(
    master=password_frame,
    text="password: ",
    fg="white",
    bg="black",
    width=10,
    height=1,
    bd=4,
    borderwidth=2
)

password_entry = tk.Entry(
    master=password_frame,
    bg="black",
    bd=4,
    cursor="arrow",
    fg="white",
    show="*",
    borderwidth=2
)

login_frame.grid(row=1, column=1, padx=4, pady=4)
username_frame.grid(row=2, column=1)
username_title.grid(row=1, column=1)
username_entry.grid(row=1, column=2)
password_frame.grid(row=3, column=1)
password_title.grid(row=1, column=1)
password_entry.grid(row=1, column=2)
login_title.pack()

login_window.mainloop()