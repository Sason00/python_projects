import turtle
import time
from multiprocessing import Process

screen = turtle.Screen()
screen.setup(450, 450)
screen.tracer(0)

tasks = []
clicks = []
is_start = False

button1_colors = ("#0e1ecf", "#378fed")
button2_colors = ("#186b27", "#2ec74a")
button3_colors = ("#ab0000", "#f71e1e")
button4_colors = ("#afb504", "#f6fc30")

button1 = turtle.Turtle()
button1.shape("square")
button1.penup()
button1.shapesize(stretch_wid=5, stretch_len=5)
button1.color(button1_colors[0])
button1.goto(0, 100)

button2 = turtle.Turtle()
button2.shape("square")
button2.penup()
button2.shapesize(stretch_wid=5, stretch_len=5)
button2.color(button2_colors[0])
button2.goto(100, 0)

button3 = turtle.Turtle()
button3.shape("square")
button3.penup()
button3.shapesize(stretch_wid=5, stretch_len=5)
button3.color(button3_colors[0])
button3.goto(0, -100)

button4 = turtle.Turtle()
button4.shape("square")
button4.penup()
button4.shapesize(stretch_wid=5, stretch_len=5)
button4.color(button4_colors[0])
button4.goto(-100, 0)

start_button = turtle.Turtle()
start_button.shape("square")
start_button.penup()
start_button.shapesize(stretch_wid=5, stretch_len=5)


def clicked(button):
    if is_start:
        if button == "button1":
            print(button, "clicked")
            clicks.append(button)
        elif button == "button2":
            print(button, "clicked")
            clicks.append(button)
        elif button == "button3":
            print(button, "clicked")
            clicks.append(button)
        elif button == "button4":
            print(button, "clicked")
            clicks.append(button)
    else:
        print("game isn't started yet")


def start_game():
    is_start = True


button1.onclick(lambda z, b: Process(target=clicked("button1")))
button2.onclick(lambda u, i: Process(target=clicked("button2")))
button3.onclick(lambda o, p: Process(target=clicked("button3")))
button4.onclick(lambda j, k: Process(target=clicked("button4")))
start_button.onclick(lambda m, n: start_game())

while True:
    screen.update()

    # button1.color(button1_colors[0])
    # button2.color(button2_colors[0])
    # button3.color(button3_colors[0])
    # button4.color(button4_colors[0])
    # time.sleep(0.05)
