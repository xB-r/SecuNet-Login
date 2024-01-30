import tkinter as tk

flat = tk.FLAT
sunken = tk.SUNKEN
raised = tk.RAISED
groove = tk.GROOVE
ridge = tk.RIDGE

register_window = tk.Tk()
register_window.title("SecuNet Register Page")
register_frame = tk.Frame(master=register_window, bg="black")
username_frame = tk.Frame(master=register_window, bg="black")
password_frame = tk.Frame(master=register_window, bg="black")

register_title = tk.Label(
    master=register_frame,
    text="Please enter desired username and password below.",
    fg="white",
    bg="#004c9e",
    width=38,
    height=3,
    relief=ridge,
    borderwidth=2
)