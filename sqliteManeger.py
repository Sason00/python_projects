import tkinter as tk
from tkinter import ttk, filedialog
import sqlite3
import os


con = None


def showAllTables():
    cursor = con.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = list(cursor)
    for i in tables:
        if not(i[0] in values.get()):
            print(i[0])
            tblList.insert(tk.END, i[0])


def openNewDB():
    location = filedialog.asksaveasfilename(
        initialdir="desktop", title="Select Folder")
    folder, newFileName = "/".join(location.split("/")
                                   [0:-1]), location.split("/")[-1]
    open(folder + "/" + newFileName, "w+")
    print(folder, newFileName)


def opneExists():
    global con
    location = filedialog.askopenfilename(
        initialdir="desktop", title="Select Folder")
    folder, newFileName = "/".join(location.split("/")
                                   [0:-1]), location.split("/")[-1]
    print(folder, newFileName)
    con = sqlite3.connect(folder + "/" + newFileName)
    mainScreen.forget()
    editDBScreen.pack()
    showAllTables()


screen = tk.Tk()

mainScreen = tk.Frame(screen)

heading1 = tk.Label(mainScreen, text="Welcome to sqlite Maneger",
                    font=("arial", 26, "bold"))
heading1.grid(row=0, column=0, columnspan=2)

opneNewDB = ttk.Button(
    mainScreen, text="Open New sqlite Data Base", command=openNewDB)
opneNewDB.grid(row=1, column=0, sticky="W")

opneExistsDB = ttk.Button(
    mainScreen, text="Open Exists sqlite Data Base", command=opneExists)
opneExistsDB.grid(row=2, column=0, sticky="W")

mainScreen.pack()

editDBScreen = tk.Frame(screen)

heading2 = tk.Label(editDBScreen, text="Edit",
                    font=("arial", 26, "bold"))
heading2.grid(row=0, column=0, columnspan=2)

printTbl = ttk.Button(
    editDBScreen, text="show All Tables", command=showAllTables)
printTbl.grid(row=1, column=0)

values = tk.Variable(value=[])
tblList = tk.Listbox(editDBScreen, listvariable=values)
tblList.grid(row=1, column=1)


screen.mainloop()
