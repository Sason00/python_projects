import tkinter as tk
import turtle
import time
import random


is_right_pressed = False
is_left_pressed = False
is_up_pressed = False
is_down_pressed = False

player_pick = "C:\\Users\\Ariel\\Desktop\\python projects\\tunk_games_photos\\pixil-frame-0.gif"

screen = turtle.Screen()
screen.setup(600, 600)
screen.tracer(0)
screen.addshape(player_pick)


player = turtle.Turtle()
player.penup()
player.speed(0)
player.shapesize(stretch_wid=2, stretch_len=2)
player.shape(player_pick)

pen = turtle.Turtle()
pen2 = turtle.Turtle()

bullet = []
enemys = []
heading = 0
chance = 97
kills = 0
money = 0


def create_enemy():
    e = turtle.Turtle()
    e.speed(0)
    e.penup()
    e.color("red")
    e.shapesize(stretch_wid=2, stretch_len=2)
    e.goto(random.randrange(-300, 300), random.randrange(-300, 300))
    enemys.append(e)


def up1():
    global is_up_pressed
    is_up_pressed = True

def up2():
    global is_up_pressed
    is_up_pressed = False

def down1():
    global is_down_pressed
    is_down_pressed = True

def down2():
    global is_down_pressed
    is_down_pressed = False

def right1():
    global is_right_pressed
    is_right_pressed = True

def right2():
    global is_right_pressed
    is_right_pressed = False

def left1():
    global is_left_pressed
    is_left_pressed = True

def left2():
    global is_left_pressed
    is_left_pressed = False



def fire(x, y):
    print(x, y)
    if len(bullet) <= 4:
        player.setheading(player.towards(x, y))
        b = turtle.Turtle()
        b.speed(0)
        b.penup()
        b.setpos(player.xcor(), player.ycor())
        b.color("#e67300")
        b.shape("square")
        b.shapesize(stretch_wid=0.5, stretch_len=1)
        b.setheading(b.towards(x, y))
        bullet.append(b)


def aim(x, y):
    print(x, y)
    player.setheading(player.towards(x, y))


def write():
    try:
        global pen
        global pen2
        pen.speed(0)
        pen.hideturtle()
        pen.penup()
        pen.goto(250, 250)
        pen.color("black")
        pen.write("kills: " + str(kills), align="center",
                font=("Arial", 18, "normal"))

        pen2.speed(0)
        pen2.hideturtle()
        pen2.penup()
        pen2.goto(-250, 250)
        pen2.color("black")
        pen2.write("money: " + str(money), align="center",
                font=("Arial", 18, "normal"))
    except:
        pass


screen.listen()
# arrows
screen.onkeypress(right1, "Right")
screen.onkeypress(left1, "Left")
screen.onkeypress(up1, "Up")
screen.onkeypress(down1, "Down")
screen.onkeyrelease(right2, "Right")
screen.onkeyrelease(left2, "Left")
screen.onkeyrelease(up2, "Up")
screen.onkeyrelease(down2, "Down")
# normal
screen.onkeypress(right1, "d")
screen.onkeypress(left1, "a")
screen.onkeypress(up1, "w")
screen.onkeypress(down1, "s")
screen.onkeyrelease(right2, "d")
screen.onkeyrelease(left2, "a")
screen.onkeyrelease(up2, "w")
screen.onkeyrelease(down2, "s")
screen.onclick(fire)
screen.onclick(aim, 3)

while True:
    screen.update()

    if is_down_pressed:
        player.sety(player.ycor() - 10)
    if is_up_pressed:
        player.sety(player.ycor() + 10)
    if is_right_pressed:
        player.setx(player.xcor() + 10)
    if is_left_pressed:
        player.setx(player.xcor() - 10)

    if player.xcor() >= 300:
        player.setx(300)
    if player.xcor() <= -300:
        player.setx(-300)
    if player.ycor() >= 300:
        player.sety(300)
    if player.ycor() <= -300:
        player.sety(-300)
    for i in bullet:
        i.forward(20)
        if i.xcor() >= 300:
            i.hideturtle()
            try:
                bullet.remove(i)
            except:
                pass
        if i.xcor() <= -300:
            i.hideturtle()
            try:
                bullet.remove(i)
            except:
                pass
        if i.ycor() >= 300:
            i.hideturtle()
            try:
                bullet.remove(i)
            except:
                pass
        if i.ycor() <= -300:
            i.hideturtle()
            try:
                bullet.remove(i)
            except:
                pass

    if (random.random() * 100) > chance:
        create_enemy()

    for i in enemys:
        for j in bullet:
            if i.distance(j) <= 20:
                i.hideturtle()
                try:
                    enemys.remove(i)
                except:
                    pass
                kills += 1

        i.setheading(i.towards(player.xcor(), player.ycor()))
        i.forward(3)

        if player.distance(i) <= 20:
            print("game over\nyour score is " + str(kills))
            screen.bye()
            time.sleep(1.5)

    if kills % 15 == 0 and kills != 0:
        chance -= 2
    try:
        pen.clear()
        pen2.clear()
    except:
        pass
    write()

    money = int(kills/10)

    time.sleep(0.05)
