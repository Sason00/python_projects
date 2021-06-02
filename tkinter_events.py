import tkinter as tk

screen = tk.Tk()

def left_click(x):
    tk.Label(screen, text="left_click").pack()

def middle_click(y):
    tk.Label(screen, text="middle_click").pack()

def right_click(z):
    tk.Label(screen, text="right_click").pack()

screen.bind("<Button-1>", left_click)
screen.bind("<Button-2>", middle_click)
screen.bind("<Button-3>", right_click)


