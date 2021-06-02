import turtle
import time
import random
import tkinter.messagebox

psilot = 0
screen_width = 800
screen_height = 700
screen = turtle.Screen()
screen.setup(width=screen_width, height=screen_height)
screen.tracer(0)

player = turtle.Turtle()
player.penup()
player.speed(0)
player.goto(0, -300)
player.shape("square")
player.shapesize(stretch_wid=1, stretch_len=5)

psila_1 = turtle.Turtle()
psila_1.penup()
psila_1.speed(0)
psila_1.goto(380, 0)
psila_1.color("red")
psila_1.shape("square")

psila_2 = turtle.Turtle()
psila_2.penup()
psila_2.speed(0)
psila_2.goto(380, -30)
psila_2.color("red")
psila_2.shape("square")

psila_3 = turtle.Turtle()
psila_3.penup()
psila_3.speed(0)
psila_3.goto(380, -60)
psila_3.color("red")
psila_3.shape("square")

class gg:
    i = -1
    blocks_x = -350
    blocks_y = 320
    gameover = False

def rand():
    random_num = random.random() * 10
    print(random_num)
    if random_num >= 5:
        return -1
    elif random_num < 5:
        return 1

ball = turtle.Turtle()
ball.penup()
ball.speed(0)
ball.goto(0, 0)
ball.shape("square")
dx = 4 * rand()
dy = -4 

blocks = []


def Blocks(color):
    global blocks
    if (gg.i == 12
        or gg.i == 25
        or gg.i == 38
        or gg.i == 51
        or gg.i == 64
        or gg.i == 77):

        gg.blocks_x = -350
        gg.blocks_y -= 40
    gg.i += 1
    blocks.append(turtle.Turtle())
    blocks[gg.i].penup()
    blocks[gg.i].speed(0)
    blocks[gg.i].shape("square")
    blocks[gg.i].color(color)
    blocks[gg.i].shapesize(stretch_wid=1, stretch_len=2)
    blocks[gg.i].goto(gg.blocks_x, gg.blocks_y)
    gg.blocks_x += 60


for i in range(13):
    Blocks("black")

for i in range(13):
    Blocks("gray")

for i in range(13):
    Blocks("#6496f4")

for i in range(13):
    Blocks("blue")

for i in range(13):
    Blocks("green")

for i in range(13):
    Blocks("red")

for i in range(13):
    Blocks("pink")

def delete_blocks(w):
    blocks_to_del = blocks[w]
    blocks_to_del.hideturtle()
    blocks.remove(blocks_to_del)

def move_right():
    x = player.xcor()
    x += 20
    if x >= 350:
        x = 350
    player.setx(x)


def move_left():
    x = player.xcor()
    x -= 20
    if x <= -350:
        x = -350
    player.setx(x)


screen.listen()
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")

while not gg.gameover:
    screen.update()

    ball.setx(ball.xcor() + dx)
    ball.sety(ball.ycor() + dy)

    if ball.xcor() >= 400 or ball.xcor() <= -400:
        dx *= -1
    if ball.ycor() >= 350:
        dy *= -1
    if ball.ycor() <= -350:
        if psilot < 2:
            psilot += 1
            if psilot == 1:
                psila_1.color("white")
            if psilot == 2:
                psila_2.color("white")
        else:
            psila_3.color("white")
            screen.update()
            gg.gameover = True
            tkinter.messagebox.showinfo("game over", "Game Over!")
        ball.goto(0, 0)
    if ball.ycor() == -300 and (ball.xcor() + 10 <= player.xcor() + 50 and ball.xcor() + 10 >= player.xcor() - 50):
        dy *= -1

    for w in range(0, len(blocks) + 15, 1):
        try:
            if ball.ycor() == blocks[w].ycor() and (ball.xcor() + 10 <= blocks[w].xcor() + 20 and ball.xcor() + 10 >= blocks[w].xcor() - 20):
                delete_blocks(w)
                dy *= -1
        except:
            pass
    time.sleep(0.0001)
