import tkinter as tk
from tkinter import ttk

screen = tk.Tk()
screen.resizable(0, 0)

entry_value = tk.StringVar()
global out_put
out_put = ""
is_calc = False

def add(sim):
    global is_calc
    if is_calc:
        entry_value.set("")
        is_calc = False
    out_put = entry_value.get()
    out_put = out_put + sim
    entry_value.set(out_put)

def calc(n):
    global is_calc
    if n == "1":
        entry_value.set(str(eval(entry_value.get())))
        is_calc = True
    elif n == "2":
        entry_value.set("")

def root():
    global is_calc
    out_put = entry_value.get()
    entry_value.set(int(out_put) ** 0.5)
    is_calc = True

output = tk.Entry(screen, textvariable=entry_value)
output.grid(columnspan=4, rowspan=1)

b1 = ttk.Button(screen, text="1", command=lambda:add("1"))
b1.grid(column=0, row=1)
b2 = ttk.Button(screen, text="2", command=lambda:add("2"))
b2.grid(column=1, row=1)
b3 = ttk.Button(screen, text="3", command=lambda:add("3"))
b3.grid(column=2, row=1)
b4 = ttk.Button(screen, text="4", command=lambda:add("4"))
b4.grid(column=0, row=2)
b5 = ttk.Button(screen, text="5", command=lambda:add("5"))
b5.grid(column=1, row=2)
b6 = ttk.Button(screen, text="6", command=lambda:add("6"))
b6.grid(column=2, row=2)
b7 = ttk.Button(screen, text="7", command=lambda:add("7"))
b7.grid(column=0, row=3)
b8 = ttk.Button(screen, text="8", command=lambda:add("8"))
b8.grid(column=1, row=3)
b9 = ttk.Button(screen, text="9", command=lambda:add("9"))
b9.grid(column=2, row=3)
plus = ttk.Button(screen, text="+", command=lambda:add("+"))
plus.grid(column=3, row=1)
minus = ttk.Button(screen, text="-", command=lambda:add("-"))
minus.grid(column=3, row=2)
times = ttk.Button(screen, text="*", command=lambda:add("*"))
times.grid(column=3, row=3)
devide = ttk.Button(screen, text="/", command=lambda:add("/"))
devide.grid(column=3, row=4)
point = ttk.Button(screen, text=".", command=lambda:add("."))
point.grid(column=0, row=4)
b0 = ttk.Button(screen, text="0", command=lambda:add("0"))
b0.grid(column=1, row=4)
equal = ttk.Button(screen, text="=", command=lambda:calc("1"))
equal.grid(column=2, row=4)
clear = ttk.Button(screen, text="c", command=lambda:calc("2"))
clear.grid(column=3, row=5)
squared = ttk.Button(screen, text="^", command=lambda:add("**"))
squared.grid(column=0, row=5)
root = ttk.Button(screen, text="√", command=root)
root.grid(column=1, row=5)
modulo = ttk.Button(screen, text="%", command=lambda:add("%"))
modulo.grid(column=2, row=5)
screen.mainloop() 