import turtle
import time
import random

screen = turtle.Screen()
screen.setup(420, 600)
screen.tracer(0)

player = turtle.Turtle()
player.shape("turtle")
player.speed(0)
player.penup()
player.left(90)
player.shapesize(stretch_len=3, stretch_wid=3)
player.setpos(0, -150)

cop = turtle.Turtle()
cop.shape("turtle")
cop.color("#34aced")
cop.speed(0)
cop.penup()
cop.left(90)
cop.shapesize(stretch_len=3.5, stretch_wid=3.5)
cop.setpos(0, -250)

cop_cooldown = 0

train_color = ["red", "orange", "blue", "grey"]
trains = []
create_trains_cooldown = 0


def left():
    if player.xcor() == 100:
        player.setpos(0, -150)
    elif player.xcor() == 0:
        player.setpos(-100, -150)


def right():
    if player.xcor() == -100:
        player.setpos(0, -150)
    elif player.xcor() == 0:
        player.setpos(100, -150)


def create_trains():
    global create_trains_cooldown
    if create_trains_cooldown >= 90:
        t1 = turtle.Turtle()
        t1.shape("square")
        t1.color("red")
        choise = random.choice((100, 0, -100))
        t1.penup()
        t1.setpos(choise, 300)
        t1.shapesize(stretch_len=3, stretch_wid=6)
        t1.color(random.choice(train_color))
        trains.append(t1)
        if choise == 100:
            t2 = turtle.Turtle()
            t2.shape("square")
            t2.color("red")
            choise = random.choice((0, -100))
            t2.penup()
            t2.setpos(choise, 300)
            t2.shapesize(stretch_len=3, stretch_wid=6)
            t2.color(random.choice(train_color))
            trains.append(t2)
        elif choise == 0:
            t2 = turtle.Turtle()
            t2.shape("square")
            t2.color("red")
            choise = random.choice((100, -100))
            t2.penup()
            t2.setpos(choise, 300)
            t2.shapesize(stretch_len=3, stretch_wid=6)
            t2.color(random.choice(train_color))
            trains.append(t2)
        elif choise == -100:
            t2 = turtle.Turtle()
            t2.shape("square")
            t2.color("red")
            choise = random.choice((100, 0))
            t2.penup()
            t2.setpos(choise, 300)
            t2.shapesize(stretch_len=3, stretch_wid=6)
            t2.color(random.choice(train_color))
            trains.append(t2)
        create_trains_cooldown = 0


screen.listen()
screen.onkeypress(left, "Left")
screen.onkeypress(left, "a")
screen.onkeypress(right, "Right")
screen.onkeypress(right, "d")

while True:
    screen.update()

    cop_cooldown += 1
    create_trains_cooldown += 1
    create_trains()

    if cop_cooldown >= 900:
        cop_cooldown = 0
        cop.sety(-400)

    for i in trains:
        i.sety(i.ycor() - 5)
        if i.xcor() == player.xcor() and i.ycor() == player.ycor():
            print("hit!!!")
            if cop_cooldown <= 500:
                print("game over")
            else:
                cop.setpos(0, -250)
                print(cop.ycor())
        if i.ycor() <= -350:
            i.hideturtle()
            trains.remove(i)

    time.sleep(0.005)
