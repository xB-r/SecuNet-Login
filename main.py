import tkinter as tk
import multiprocessing
import subprocess
import time
import random
import schedule
from cryptography.fernet import Fernet

flat = tk.FLAT
sunken = tk.SUNKEN
raised = tk.RAISED
groove = tk.GROOVE
ridge = tk.RIDGE

left = tk.LEFT
right = tk.RIGHT
top = tk.TOP
bottom = tk.BOTTOM

key = Fernet.generate_key()
cipher_suite = Fernet(key)

random_code = random.randint(100000, 1000000)
print(random_code)
def auth_code_gen():
    code_window = tk.Tk()
    code_window.title("Today's Code")
    code_display = tk.Label(
        master=code_window,
        text=random_code,
        fg="white",
        bg="#004c9e",
        width=30,
        height=3,
        relief=ridge,
        borderwidth=2
    )
    code_display.pack()
    code_window.mainloop()

def main():

    def login_page():
        subprocess.run(["python", "loginpage.py"])

    def register_auth():
        subprocess.run(["python", "registerauthentication.py"])


    # assigned frames for layout and window created
    welcome_window = tk.Tk()
    welcome_window.title("SecuNet")
    welcome_frame = tk.Frame(master=welcome_window, bg="black")
    welcome_frame.grid(row=1, column=1, padx=4, pady=4)
    register_frame = tk.Frame(master=welcome_window, bg="black")
    login_frame = tk.Frame(master=welcome_window, bg="black")

    welcome_title = tk.Label(
        master=welcome_frame,
        text="SecuNet Login Systems",
        fg="white",
        bg="#004c9e",
        width=30,
        height=3,
        relief=ridge,
        borderwidth=2
    )

    welcome_subtitle = tk.Label(
        master=welcome_frame,
        text="Please select from the options below.",
        fg="white",
        bg="#004c9e",
        width=30,
        relief=ridge,
        borderwidth=2
    )

    register_button = tk.Button(
        master=register_frame,
        text="Register",
        fg="white",
        bg="#6600ff",
        height=2,
        width=20,
        command=register_auth
    )

    login_button = tk.Button(
        master=login_frame,
        text="Login",
        fg="white",
        bg="#6600FF",
        height=2,
        width=20,
        command=login_page
    )

    welcome_frame.pack(fill=tk.BOTH, expand=True)
    register_frame.pack(fill=tk.BOTH, expand=True)
    login_frame.pack(fill=tk.BOTH, expand=True)
    welcome_title.pack(padx=2, pady=2)
    welcome_subtitle.pack(padx=2)
    register_button.pack(side=left, padx=2, pady=2)
    login_button.pack(side=right)

    welcome_window.mainloop()

def schedule_task():
    auth_code_gen()
    schedule.every(86400).seconds.do(auth_code_gen)  # day = 86400 seconds
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == '__main__':
    main_page = multiprocessing.Process(target=main)
    auth_code_generator_process = multiprocessing.Process(target=schedule_task)

    main_page.start()
    auth_code_generator_process.start()

    main_page.join()
    auth_code_generator_process.join()