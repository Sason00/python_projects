import turtle
import tkinter as tk
from tkinter import colorchooser
import time

tools_screen = tk.Tk()
tools_screen.geometry("100x300")
screen = turtle.Screen()
screen.setup(700, 700)
screen.tracer(0)

pen = turtle.Turtle()
pen.shape("circle")
pen.shapesize(stretch_wid=1, stretch_len=1)
pen.pensize(2)
pen.penup()

is_eraser = False
is_stamp = False
color = ((0, 0, 0), "#000000")
shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]


def dragging(x, y):
    pen.goto(x, y)
    pen.pendown()
    pen.ondrag(dragging)


def pen_goto(x, y):
    if not is_stamp:
        try:
            pen.penup()
            pen.goto(x, y)
        except:
            pen.goto(x, y)
    else:
        pen.goto(x, y)
        pen.stamp()


def change_color():
    global color
    color = colorchooser.askcolor()
    print(color)
    pen.color(color[1])
    pen.pencolor(color[1])
    color_button["bg"] = color[1]
    color_button["fg"] = "#" + color[1].replace("#", "")[::-1]


def change_size(size):
    pen.shapesize(size // 5)
    pen.pensize(size)


def use_eraser():
    global is_eraser
    if not is_eraser:
        pen.color("white")
        pen.pencolor("white")
        is_eraser = True
        use_eraser_button["text"] = "use pen"
    else:
        pen.color(color[1])
        pen.pencolor(color[1])
        is_eraser = False
        use_eraser_button["text"] = "use eraser"


def use_stamp(shape):
    global is_stamp
    if not is_stamp:
        try:
            pen.shape(shapes[shape])
        except:
            pass
        pen.penup()
        use_stamp_button["text"] = "use pen"
        is_stamp = True
    else:
        pen.shape("circle")
        pen.pendown()
        use_stamp_button["text"] = "use stamp"
        is_stamp = False


pen.shape()

color_button = tk.Button(tools_screen, text="pick color",
                         bg="black", fg="white", command=change_color)
color_button.pack()
size = tk.IntVar()
entry1 = tk.Entry(tools_screen, textvariable=size)
entry1.pack()
submit_button = tk.Button(tools_screen, text="Submit",
                          command=lambda: change_size(size.get()))
submit_button.pack()
use_eraser_button = tk.Button(
    tools_screen, text="use eraser", command=use_eraser)
use_eraser_button.pack()
stamps_shapes_lists = tk.Listbox(tools_screen)
stamps_shapes_lists.pack()
for i in shapes:
    stamps_shapes_lists.insert(tk.END, i)
use_stamp_button = tk.Button(tools_screen, text="use stamps",
                             command=lambda: use_stamp(stamps_shapes_lists.curselection()[0]))
use_stamp_button.pack()

screen.listen()
screen.onclick(pen_goto)
pen.ondrag(dragging)
while True:
    screen.update()

    time.sleep(0.0001)
