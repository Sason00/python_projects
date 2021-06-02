import turtle
import random
import time

point = []
gameover = False
screen_width = 800
screen_height = 400
screen = turtle.Screen()
screen.setup(width=screen_width, height=screen_height)
screen.tracer(0)

player = turtle.Turtle()
player.speed(0)
player.shape("circle")
player.color("black")
player.penup()
player.goto(0, 0)


class gg:
    i = -1


def player_right():
    x = player.xcor()
    x += 10
    if x >= 390:
        x = 390
    player.setx(x)


def player_left():
    x = player.xcor()
    x -= 10
    if x <= -390:
        x = -390
    player.setx(x)


def player_forward():
    y = player.ycor()
    y += 10
    if y >= 200:
        y = 190
    player.sety(y)


def player_backward():
    y = player.ycor()
    y -= 10
    if y <= -200:
        y = -190
    player.sety(y)


def random_point():
    r = random.random() * 500
    if r <= 5:
        gg.i += 1
        point.append(turtle.Turtle())
        point[gg.i].speed(0)
        point[gg.i].shape("circle")
        point[gg.i].color("red")
        point[gg.i].penup()
        point_x = int(random.randrange(-40, 40))
        point_y = int(random.randrange(-20, 20))
        point[gg.i].goto(point_x * 10, point_y * 10)
        print(r)


def delete_points(points):
    point_to_del = point[points]
    point_to_del.color("white")
    print("hi")
    point.remove(point_to_del)
    gg.i -= 1


screen.listen()
screen.onkeypress(player_forward, "Up")
screen.onkeypress(player_right, "Right")
screen.onkeypress(player_left, "Left")
screen.onkeypress(player_backward, "Down")

while not gameover:
    f = len(point)
    screen.update()
    random_point()
    if gg.i >= 0:
        for w in range(f):
            try:
                if player.xcor() == point[w].xcor() and player.ycor() == point[w].ycor():
                    delete_points(w)
            except:
                pass
    player.forward(0)
    time.sleep(0.05)
