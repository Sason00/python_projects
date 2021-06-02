import tkinter as tk
from tkinter import ttk, messagebox
import random

screen = tk.Tk()
screen.resizable(0, 0)

rules = """
The computer choose four numbers and the you, the Guesser, tries to guess it.

At each turn you tries a to guess the numbers, and the computer tells how close it is to the answer by giving:

    *The number of A - numbers correct in the right position.
    *The number of B - numbers correct but in the wrong position.

The Guesser tries to guess the answer in less than 8 turns.

There are not two same numbers in the same turn.
"""

goal = ""
turn = 1
guesses = []
ABs = []


def set_new_goal():
    global goal
    goal = ""
    for i in range(4):
        num = random.randrange(0, 10)
        while str(num) in goal:
            num = random.randrange(0, 10)
        goal = goal + str(num)
    # print(goal)


set_new_goal()


def init():
    global goal, turn, guesses, ABs
    goal = ""
    turn = 1
    for i in range(len(guesses)):
        guesses[i].destroy()
        ABs[i].destroy()
    guesses = []
    ABs = []
    set_new_goal()


def enter_guess(guess):
    global turn
    guess = guess[:4]
    A = 0
    B = 0
    not_good = ""
    guesses.append(tk.Label(screen, text=str(guess)))
    guesses[len(guesses) - 1].grid(row=1 + turn, column=1)
    for i in range(len(guess)):
        if guess[i] == goal[i]:
            A += 1
        else:
            not_good = not_good + guess[i]
    for i in not_good:
        if i in goal:
            B += 1
    ABs.append(tk.Label(screen, text=str(A) + "A" + str(B) + "B"))
    ABs[len(ABs) - 1].grid(row=1 + turn, column=2)
    turn += 1
    if A == 4:
        ask = messagebox.askyesno("You Won", "Do You Want To Playn Again?")
        if(ask):
            init()
    elif turn == 9:
        ask = messagebox.askyesno(
            "You Lose", "The Number Was " + goal + "\nDo You Want To Playn Again?")
        if ask:
            init()
        else:
            screen.destroy()


def show_rules():
    rules_screen = tk.Toplevel(screen)

    text = tk.Label(rules_screen, text=rules,
                    justify=tk.LEFT, font=("Arial", 12))
    text.pack()

    exit_button = ttk.Button(rules_screen, text="Exit",
                             command=rules_screen.destroy)
    exit_button.pack()

    rules_screen.mainloop()


menu = tk.Menu(screen)
screen.config(menu=menu)
file_menu_1 = tk.Menu(menu, tearoff=0)
example_1 = menu.add_cascade(label="Game", menu=file_menu_1)
file_menu_1.add_command(label="start a new game", command=init)
file_menu_2 = tk.Menu(menu, tearoff=0)
alerts = menu.add_cascade(label="Help", menu=file_menu_2)
file_menu_2.add_command(label="rules", command=show_rules)

tk.Label(screen, text="input:").grid(row=0, column=0)

player_guess = tk.StringVar()
player_input = ttk.Entry(screen, textvariable=player_guess)
player_input.bind("<Return>", lambda x: enter_guess(player_guess.get()))
player_input.grid(row=0, column=1, columnspan=2)

submit_button = ttk.Button(
    screen, text="Enter", command=lambda: enter_guess(player_guess.get()))
submit_button.grid(row=0, column=3)

tk.Label(screen, text="Guess").grid(row=1, column=1)
tk.Label(screen, text="Result").grid(row=1, column=2)

for i in range(1, 9):
    tk.Label(screen, text=str(i)).grid(row=1 + i, column=0)

screen.mainloop()
