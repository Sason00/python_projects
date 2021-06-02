import tkinter as tk

screen = tk.Tk()
screen.title("loggin")
screen.geometry("190x170")

usernames = []
passwords = []

tk.Label(screen, text="loggin").pack()

tk.Label(screen, text="").pack()

tk.Label(screen, text="Username:").pack()
username = tk.Entry(screen).pack()

tk.Label(screen, text="Password:").pack()
password = tk.Entry(screen).pack()

sign_in_button = tk.Button(screen, text="sign in").pack()
screen.mainloop()
