import turtle
import time
import datetime

gameover = False
bullets = []
Times = 1
spaces_ships = []

screen = turtle.Screen()
screen.setup(650, 500)
screen.tracer(0)
screen.bgcolor("black")

player = turtle.Turtle()
player.shape("square")
player.shapesize(stretch_wid=1.5, stretch_len=0.5)
player.color("white")
player.penup()
player.speed(0)
player.goto(0, -205)

ship_dx = 5


def move_right():
    x = player.xcor()
    x += 15
    if x >= 320:
        x = 320
    player.setx(x)


def move_left():
    x = player.xcor()
    x -= 15
    if x <= -305:
        x = -305
    player.setx(x)


def shoot():
    if len(bullets) == 0:
        bullet = turtle.Turtle()
        bullet.penup()
        bullet.color("white")
        bullet.shape("square")
        bullet.shapesize(stretch_wid=1, stretch_len=0.05)
        bullet.setpos(player.xcor(), player.ycor())
        bullet.speed(0)
        bullets.append(bullet)


def create_space_ship(color, x, y):
    global Times

    ship = turtle.Turtle()
    ship.color(color)
    ship.shape("square")
    ship.penup()
    ship.goto(x + 50, y)
    spaces_ships.append(ship)


for i in range(7):
    create_space_ship("gray", -200 * -(i/10), 400)
for i in range(7):
    create_space_ship("blue", -200 * -(i/10), 360)
for i in range(7):
    create_space_ship("green", -200 * -(i/10), 320)
for i in range(7):
    create_space_ship("red", -200 * -(i/10), 280)
for i in range(7):
    create_space_ship("pink", -200 * -(i/10), 240)


def move_ships():
    global ship_dx
    for t in spaces_ships:
        t.setx(t.xcor() + ship_dx)
        for r in range(len(spaces_ships)):
            if t.xcor() > 200:
                spaces_ships[r].sety(spaces_ships[r].ycor() - 10)
                ship_dx *= -1
            elif t.xcor() < -200:
                spaces_ships[r].sety(spaces_ships[r].ycor() - 10)
                ship_dx *= -1
    print(len(spaces_ships))


screen.listen()
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")
screen.onkeypress(shoot, "space")

while not gameover:
    screen.update()
    if len(bullets) > 0:
        bullets[0].sety(bullets[0].ycor() + 10)
        if bullets[0].ycor() >= 250:
            bullets[0].hideturtle()
            bullets = []
        for f in spaces_ships:
            try:
                if bullets[0].distance(f) <= 20:
                    bullets[0].hideturtle()
                    f.hideturtle()
                    bullets = []
                    a = spaces_ships.index(f)
                    print(a)
                    spaces_ships.remove(spaces_ships[a])
                    break
            except:
                pass

    move_ships()

    time.sleep(0.05)
