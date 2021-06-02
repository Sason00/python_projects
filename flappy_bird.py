import turtle
import time
import random

screen = turtle.Screen()
screen.setup(650, 500)
screen.tracer(0)

gameover = False
top_cones = []
top_cones_wid = [20, 50, 52, 33, 39, 44, 22, 27, 40]
buttom_cones = []
buttom_cones_wid = [20, 52, 47, 33, 35, 27, 30, 44]
r = 100

player = turtle.Turtle()
player.speed(0)
player.penup()
player.shape("square")
player.color("#008822")
player.goto(-250, 0)


def top_cone():
    global r
    r = random.randrange(0, 100)
    if r <= 10:
        buttom_cone()
        ran1 = random.randrange(0, len(top_cones_wid))
        new_cone = turtle.Turtle()
        new_cone.speed(0)
        new_cone.penup()
        new_cone.shape("square")
        new_cone.shapesize(stretch_wid=top_cones_wid[ran1]/2, stretch_len=0.5)
        print(top_cones_wid[ran1]/2)
        new_cone.goto(325, 230)
        top_cones.append(new_cone)
        top_cones_wid.append(ran1)


def buttom_cone():
    ran2 = random.randrange(0, len(buttom_cones_wid))
    new_cone2 = turtle.Turtle()
    new_cone2.speed(0)
    new_cone2.penup()
    new_cone2.shape("square")
    new_cone2.shapesize(stretch_wid=buttom_cones_wid[ran2]/2, stretch_len=0.5)
    new_cone2.goto(325, -230)
    buttom_cones.append(new_cone2)
    buttom_cones_wid.append(ran2)


def move_left():
    player.setx(player.xcor() - 10)


def move_right():
    player.setx(player.xcor() + 10)


def move_up():
    player.sety(player.ycor() + 10)


def move_down():
    player.sety(player.ycor() - 10)


screen.listen()
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")
screen.onkeypress(move_up, "Up")
screen.onkeypress(move_down, "Down")

while not gameover:
    screen.update()
    top_cone()
    # for i in range(len(top_cones)-1):
    #    top_cones[i].setx(top_cones[i].xcor() - 4)
    #    for T in top_cones_wid:
    #        if (player.pos() - T <= T):  # and (player.distance(t) <= t):
    #            print("hi")
    for j in range(len(top_cones)-1):
        buttom_cones[j].setx(buttom_cones[j].xcor() - 4)

    if player.xcor() <= -315:
        player.setx(-315)

    elif player.xcor() >= 305:
        player.setx(305)

    elif player.ycor() <= -230:
        player.sety(-230)

    elif player.ycor() >= 235:
        player.sety(235)

    time.sleep(0.05)
