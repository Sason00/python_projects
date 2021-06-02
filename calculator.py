import tkinter as tk

output = ""


def show_output(s):
    global output
    output = output + s
    entry_value.set(output)


def calculate():
    global output
    try:
        if output == "-0":
            entry_value.set("-0")
            output = ""
        else:
            output = str(eval(output))
            entry_value.set(output)
            output = ""
    except:
        pass


screen = tk.Tk()

entry_value = tk.StringVar()

outPut = tk.Entry(screen, textvariable=entry_value,
                  insertwidth=5).grid(columnspan=4, rowspan=1)
but7 = tk.Button(screen, text="7", command=lambda: show_output(
    "7"), width=6, height=3).grid(row=1, column=0)
but8 = tk.Button(screen, text="8", command=lambda: show_output(
    "8"), width=6, height=3).grid(row=1, column=1)
but9 = tk.Button(screen, text="9", command=lambda: show_output(
    "9"), width=6, height=3).grid(row=1, column=2)
butx = tk.Button(screen, text="*",
                 command=lambda: show_output("*"), width=6, height=3).grid(row=1, column=3)
but4 = tk.Button(screen, text="4", command=lambda: show_output(
    "4"), width=6, height=3).grid(row=2, column=0)
but5 = tk.Button(screen, text="5", command=lambda: show_output(
    "5"), width=6, height=3).grid(row=2, column=1)
but6 = tk.Button(screen, text="6", command=lambda: show_output(
    "6"), width=6, height=3).grid(row=2, column=2)
but_m = tk.Button(screen, text="-",
                  command=lambda: show_output("-"), width=6, height=3).grid(row=2, column=3)
but1 = tk.Button(screen, text="1", command=lambda: show_output(
    "1"), width=6, height=3).grid(row=3, column=0)
but2 = tk.Button(screen, text="2", command=lambda: show_output(
    "2"), width=6, height=3).grid(row=3, column=1)
but3 = tk.Button(screen, text="3", command=lambda: show_output(
    "3"), width=6, height=3).grid(row=3, column=2)
but_p = tk.Button(screen, text="+",
                  command=lambda: show_output("+"), width=6, height=3).grid(row=3, column=3)
but_devide = tk.Button(
    screen, text="/", command=lambda: show_output("/"), width=6, height=3).grid(row=4, column=0)
but0 = tk.Button(screen, text="0", command=lambda: show_output(
    "0"), width=6, height=3).grid(row=4, column=1)
but_float = tk.Button(
    screen, text=".", command=lambda: show_output("."), width=6, height=3).grid(row=4, column=2)
equal = tk.Button(
    screen, text="=", command=calculate, width=6, height=3).grid(row=4, column=3)
screen.mainloop()
