import tkinter as tk
from tkinter import ttk
import os

screen = tk.Tk()


def downlaod():
    global sv1
    module = sv1.get()
    print(os.system("pip install " + str(module)))
    print(module)


def update():
    print(os.system("python -m pip install --upgrade pip"))
    # python -m pip install --upgrade pip


def uninstall():
    global sv1
    module = sv1.get()
    print(os.system("pip uninstall " + str(module)))
    print(module)


def show_downloads():
    print(os.system("pip list"))


sv1 = tk.StringVar()
sv2 = tk.StringVar()

lebal1 = ttk.Label(screen, text="enter module name:").grid(row=0, column=0)
entry1 = ttk.Entry(screen, textvariable=sv1).grid(row=0, column=1)
button_download = ttk.Button(screen, text="download",
                            command=downlaod).grid(row=0, column=2)
lebal2 = ttk.Label(screen, text="enter module name:").grid(row=1, column=0)
entry2 = ttk.Entry(screen, textvariable=sv2).grid(row=1, column=1)
button_uninstall = ttk.Button(
    screen, text="uninstall", command=uninstall).grid(row=1, column=2)

button_update = ttk.Button(screen, text="update",
                          command=update).grid(row=3, column=0)
button_show_downloads = ttk.Button(
    screen, text="show downloads", command=show_downloads).grid(row=3, column=1)

screen.mainloop()
