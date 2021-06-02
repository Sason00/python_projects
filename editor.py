from tkinter import filedialog
from tkinter import Tk
text = ""
filename = ""

n = 0
input1 = input("if you want to edit a file type \"pick file\" or \"pf\" ")
if input1 == "pick file" or input1 == "pf":
    window = Tk()
    filename = filedialog.askopenfilename(
        initialdir="Desktop", title="Select file",
        filetypes=(("txt files", "*.txt"), ("python files", "*.py"), ("html files", "*.html"), ("all files", "*.*")))
    window.destroy()


print("to exit type \"exit()\" \n")

if filename != "":
    for i in open(filename, "r").readlines():
        text = text + i
        n += 1
        print(str(n) + ">>>" + i.replace("\n", "", 1))

while "exit()" not in text:
    n += 1
    line = input(str(n) + ">>>")
    text = text + line + "\n"

text = text.replace("exit()", "", 1)
text = text.replace("	", "    ", 1)
if input1 == "pick file" or input1 == "pf":
    open(filename, "w+").write(text)
else:
    input2 = input("Name of the file: ")
    if "." not in input2:
        input2 = input2 + ".txt"
    open(input2, "w+").write(text)
