import tkinter as tk

screen = tk.Tk()


turn = "X"
turns = 0


def is_someone_won():
    if b1["text"] == "X" and b2["text"] == "X" and b3["text"] == "X":
        print("X won")
    elif b4["text"] == "X" and b5["text"] == "X" and b6["text"] == "X":
        print("X won")
    elif b7["text"] == "X" and b8["text"] == "X" and b9["text"] == "X":
        print("X won")
    elif b1["text"] == "X" and b4["text"] == "X" and b7["text"] == "X":
        print("X won")
    elif b2["text"] == "X" and b5["text"] == "X" and b8["text"] == "X":
        print("X won")
    elif b3["text"] == "X" and b6["text"] == "X" and b9["text"] == "X":
        print("X won")
    elif b1["text"] == "X" and b5["text"] == "X" and b9["text"] == "X":
        print("X won")
    elif b3["text"] == "X" and b5["text"] == "X" and b7["text"] == "X":
        print("X won")
    elif b1["text"] == "O" and b2["text"] == "O" and b3["text"] == "O":
        print("O won")
    elif b4["text"] == "O" and b5["text"] == "O" and b6["text"] == "O":
        print("O won")
    elif b7["text"] == "O" and b8["text"] == "O" and b9["text"] == "O":
        print("O won")
    elif b1["text"] == "O" and b4["text"] == "O" and b7["text"] == "O":
        print("O won")
    elif b2["text"] == "O" and b5["text"] == "O" and b8["text"] == "O":
        print("O won")
    elif b3["text"] == "O" and b6["text"] == "O" and b9["text"] == "O":
        print("O won")
    elif b1["text"] == "O" and b5["text"] == "O" and b9["text"] == "O":
        print("O won")
    elif b3["text"] == "O" and b5["text"] == "O" and b7["text"] == "O":
        print("O won")


def clicked(b):
    global turn, turns
    if b["text"] == "":
        b["text"] = turn
        if turn == "X":
            turn = "O"
        elif turn == "O":
            turn = "X"
        turns += 1
        is_someone_won()


b1 = tk.Button(screen, text="", width=10, height=5,
               command=lambda: clicked(b1))
b2 = tk.Button(screen, text="", width=10, height=5,
               command=lambda: clicked(b2))
b3 = tk.Button(screen, text="", width=10, height=5,
               command=lambda: clicked(b3))

b4 = tk.Button(screen, text="", width=10, height=5,
               command=lambda: clicked(b4))
b5 = tk.Button(screen, text="", width=10, height=5,
               command=lambda: clicked(b5))
b6 = tk.Button(screen, text="", width=10, height=5,
               command=lambda: clicked(b6))

b7 = tk.Button(screen, text="", width=10, height=5,
               command=lambda: clicked(b7))
b8 = tk.Button(screen, text="", width=10, height=5,
               command=lambda: clicked(b8))
b9 = tk.Button(screen, text="", width=10, height=5,
               command=lambda: clicked(b9))

b1.grid(row=0, column=0)
b2.grid(row=0, column=1)
b3.grid(row=0, column=2)

b4.grid(row=1, column=0)
b5.grid(row=1, column=1)
b6.grid(row=1, column=2)

b7.grid(row=2, column=0)
b8.grid(row=2, column=1)
b9.grid(row=2, column=2)

screen.mainloop()
