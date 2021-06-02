from tkinter import *
from tkinter.filedialog import askopenfilename
import os

f = open("C:\\Users\\Ariel\\Desktop\\json files and other files\\paths.txt", "r")
labels = []


def choose_files():
    Tk().withdraw()

    filename = askopenfilename(initialdir="C:\\Users\\Ariel\\Desktop",
                               title="Select file")
    with open("C:\\Users\\Ariel\\Desktop\\json files and other files\\paths.txt", "a+") as file:
        file.write(filename + ",")
    labels.append(Label(screen, text=filename).pack())


def run_files():
    for j in ff.split(","):
        os.startfile(j)
        print(j)


def delete_history():
    global labels
    open("C:\\Users\\Ariel\\Desktop\\json files and other files\\paths.txt", "w").write("")
    for g in labels:
        g.pack_forget()
    labels = []


screen = Tk()


button1 = Button(screen, text="pick here an aplication",
                 command=choose_files).pack()
button2 = Button(screen, text="run chosen aplications",
                 command=run_files).pack()
button3 = Button(screen, text="delete the old paths",
                 command=delete_history).pack()
ff = f.read()
for i in ff.split(","):
    labels.append(Label(screen, text=i).pack())
screen.mainloop()
